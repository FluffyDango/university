#!/bin/bash
set -e

# sudo hostnamectl set-hostname node0
# sudo visudo # ADD LINES:
# rena9048 ALL=(ALL) NOPASSWD: /usr/bin/tee /proc/sys/vm/drop_caches
# rena9048 ALL=(ALL) NOPASSWD: /usr/bin/ceph df *
# rena9048 ALL=(ALL) NOPASSWD: /usr/bin/ceph osd df *
# rena9048 ALL=(ALL) NOPASSWD: /usr/bin/ceph -s
# rena9048 ALL=(ALL) NOPASSWD: /usr/bin/ceph status
# rena9048 ALL=(ALL) NOPASSWD: /usr/bin/ceph daemon osd.*
# HELPFUL
# export TERM=xterm
# sudo journalctl -u ceph-osd@$OSD_ID -n 50 --no-pager
# sudo ceph-osd -i "$OSD_ID" --mkfs --mkkey --osd-uuid $(uuidgen) --no-mon-config

DATA_DEV="/dev/vdb"
CLUSTER_NODES=("node0" "node1" "node2" "node3")
MON_HOSTS="node0,node1,node2,node3"
PUBLIC_NETWORK="10.0.0.0/8"
PREPARED_MOUNT="/mnt/data"

# Keeping these static allows for cluster connections to work smootly.
# A unique id for the whole cluster
FSID="a7f64266-0894-4f1e-a635-d0aeaca0e993"
# shared secret key used by all monitor daemons
MON_KEY="AQD7kyJmAAAAABAA55f4gX5sY4z8J5+X5X5X5g=="
# Authentication for admin user used when running "ceph" command
ADMIN_KEY="AQD7kyJmAAAAABAABBBBBBBBBBBBBBBBBBBBBB=="

sudo apt update
sudo apt install -y gnupg2 wget software-properties-common sysstat

sudo wget -q -O /usr/share/keyrings/ceph-release.asc "https://download.ceph.com/keys/release.asc"
echo "deb [signed-by=/usr/share/keyrings/ceph-release.asc] https://download.ceph.com/debian-pacific/ bullseye main" | sudo tee /etc/apt/sources.list.d/ceph.list
sudo apt update
sudo apt install -y ceph ceph-mon ceph-osd ceph-common radosgw uuid-runtime ceph-mgr

sudo sed -i '/127.0.1.1/d' /etc/hosts
sudo sed -i 's/ENABLED="false"/ENABLED="true"/' /etc/default/sysstat
sudo systemctl restart sysstat

# Add btrfs next to filestore for btrfs testing
sudo tee /etc/ceph/ceph.conf <<EOF
[global]
fsid = $FSID
mon_initial_members = ${CLUSTER_NODES[*]}
mon_host = $MON_HOSTS
public_network = $PUBLIC_NETWORK
auth_cluster_required = cephx
auth_service_required = cephx
auth_client_required = cephx
osd_pool_default_size = 2
osd_max_object_name_len = 1024
osd_max_object_namespace_len = 64

osd_objectstore = filestore
enable_experimental_unrecoverable_data_corrupting_features = filestore
osd_check_max_object_name_len_on_startup = false
osd_journal_size = 1024

[client.rgw.$(hostname)]
host = $(hostname)
keyring = /var/lib/ceph/radosgw/ceph-rgw.$(hostname)/keyring
log file = /var/log/ceph/ceph-rgw-$(hostname).log
rgw frontends = beast port=9000
EOF

# Monitor Keyring
sudo ceph-authtool --create-keyring /tmp/ceph.mon.keyring --name=mon. --add-key="$MON_KEY" --cap mon 'allow *'
# Admin Keyring, allow everything. Security not important for testing.
sudo ceph-authtool --create-keyring /etc/ceph/ceph.client.admin.keyring --name=client.admin --add-key="$ADMIN_KEY" --cap mon 'allow *' --cap osd 'allow *' --cap mgr 'allow *' --cap mds 'allow *'
# Import Admin key into Mon (Monitoring) keyring
sudo ceph-authtool /tmp/ceph.mon.keyring --import-keyring /etc/ceph/ceph.client.admin.keyring
sudo chown ceph:ceph /tmp/ceph.mon.keyring

MON_DIR="/var/lib/ceph/mon/ceph-$(hostname)"
sudo mkdir -p "$MON_DIR"

# Creates a topology map so that cluster can connect
monmaptool --create --fsid "$FSID" --clobber /tmp/monmap
for node in "${CLUSTER_NODES[@]}"; do
  NODE_IP=$(getent hosts "$node" | awk '{ print $1 }')
  monmaptool --add "$node" "$NODE_IP" /tmp/monmap
done

# Setup monitoring, file "done" acts as a flag.
if [ ! -f "$MON_DIR/done" ]; then
  sudo ceph-mon --mkfs -i $(hostname) --monmap /tmp/monmap --keyring /tmp/ceph.mon.keyring
  sudo touch "$MON_DIR/done"
  sudo chown -R ceph:ceph "$MON_DIR"
fi

sudo systemctl enable --now ceph-mon@$(hostname)

MGR_DIR="/var/lib/ceph/mgr/ceph-$(hostname)"
sudo mkdir -p "$MGR_DIR"
sudo ceph auth get-or-create mgr.$(hostname) mon 'allow profile mgr' osd 'allow *' mds 'allow *' | sudo tee "$MGR_DIR/keyring"
sudo chown -R ceph:ceph "$MGR_DIR"
sudo systemctl enable --now ceph-mgr@$(hostname)

echo "Waiting for cluster connections to be available..."
# We loop until we can successfully run 'ceph -s', which means the cluster is forming.
# This prevents the OSD creation step from failing if the monitors aren't ready yet.
until sudo ceph -s >/dev/null 2>&1; do
  echo "Waiting for other nodes to join..."
  sleep 5
done
echo "Cluster is reachable"

OSD_ID=$(sudo ceph --name client.admin --keyring /etc/ceph/ceph.client.admin.keyring osd create)
OSD_DIR="/var/lib/ceph/osd/ceph-$OSD_ID"

sudo mkdir -p "$OSD_DIR"

if ! mountpoint -q "$PREPARED_MOUNT"; then
  echo "ERROR: $PREPARED_MOUNT is not mounted"
  exit 1
fi
sudo mount --bind "$PREPARED_MOUNT" "$OSD_DIR"

sudo ceph-osd -i "$OSD_ID" --mkfs --mkkey --osd-uuid $(uuidgen) --no-mon-config
sudo ceph auth del osd.$OSD_ID
sudo systemctl disable --now ceph-osd@$OSD_ID
sudo ceph auth add osd.$OSD_ID osd 'allow *' mon 'allow profile osd' -i "$OSD_DIR/keyring"
sudo chown -R ceph:ceph "$OSD_DIR"
sudo systemctl enable --now ceph-osd@$OSD_ID

RGW_DIR="/var/lib/ceph/radosgw/ceph-rgw.$(hostname)"
sudo mkdir -p "$RGW_DIR"

sudo ceph-authtool --create-keyring "$RGW_DIR/keyring"
sudo chmod +r "$RGW_DIR/keyring"
sudo ceph-authtool "$RGW_DIR/keyring" -n "client.rgw.$(hostname)" --gen-key
sudo ceph auth add "client.rgw.$(hostname)" -i "$RGW_DIR/keyring" osd 'allow rwx' mon 'allow rw'

sudo systemctl enable --now ceph-radosgw@rgw.$(hostname)

sudo ceph config set mon auth_allow_insecure_global_id_reclaim false
sudo ceph mon enable-msgr2

echo "Done"
