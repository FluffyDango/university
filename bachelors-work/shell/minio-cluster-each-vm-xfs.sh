#!/bin/bash
set -e

# sudo visudo # ADD LINES:
# rena9048 ALL=(ALL) NOPASSWD: /usr/bin/tee /proc/sys/vm/drop_caches
# export TERM=xterm

DATA_DEV=/dev/vdb
MOUNT=/mnt/data
CLUSTER_NODES=("node0" "node1" "node2" "node3")
MINIO_ROOT_USER="minioadmin"
MINIO_ROOT_PASSWORD="minioadmin"
MINIO_PORT=9000
MINIO_CONSOLE_PORT=9001
RUN_USER=minio-user

sudo apt update
sudo apt install -y curl sysstat

sudo sed -i 's/ENABLED="false"/ENABLED="true"/' /etc/default/sysstat
sudo systemctl restart sysstat

if ! id "$RUN_USER" &>/dev/null; then
  sudo useradd -r -s /sbin/nologin "$RUN_USER"
  echo "Created user: $RUN_USER"
else
  echo "User $RUN_USER already exists"
fi
sudo chown -R "$RUN_USER:$RUN_USER" "$MOUNT"

curl -fsSL https://dl.min.io/server/minio/release/linux-amd64/minio -o /tmp/minio
sudo mv /tmp/minio /usr/local/bin/minio
sudo chmod 0755 /usr/local/bin/minio

sudo mkdir -p /etc/minio
sudo tee /etc/minio/minio.env <<EOF
MINIO_ROOT_USER=${MINIO_ROOT_USER}
MINIO_ROOT_PASSWORD=${MINIO_ROOT_PASSWORD}
MINIO_ADDRESS=:${MINIO_PORT}
MINIO_OPTS="--console-address :9001"
MINIO_VOLUMES="http://node{0...3}:${MINIO_PORT}${MOUNT}"
EOF

sudo tee /etc/systemd/system/minio.service <<'EOF'
[Unit]
Description=MinIO
Documentation=https://min.io/docs/minio/linux/index.html
Wants=network-online.target
After=network-online.target
AssertFileIsExecutable=/usr/local/bin/minio

[Service]
WorkingDirectory=/usr/local

User=minio-user
Group=minio-user

EnvironmentFile=-/etc/minio/minio.env

ExecStartPre=/bin/bash -c 'if [ -z "${MINIO_VOLUMES}" ]; then echo "MINIO_VOLUMES not set in environment file"; exit 1; fi'
ExecStartPre=/bin/bash -c 'if [ -z "${MINIO_ROOT_USER}" ]; then echo "MINIO_ROOT_USER not set in environment file"; exit 1; fi'
ExecStartPre=/bin/bash -c 'if [ -z "${MINIO_ROOT_PASSWORD}" ]; then echo "MINIO_ROOT_PASSWORD not set in environment file"; exit 1; fi'
ExecStart=/usr/local/bin/minio server $MINIO_OPTS $MINIO_VOLUMES

Restart=always
RestartSec=5
LimitNOFILE=65536
LimitFSIZE=infinity
OOMScoreAdjust=-999
TimeoutStopSec=infinity
SendSIGKILL=no

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now minio
