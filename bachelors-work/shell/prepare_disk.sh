#!/bin/bash
set -e

DATA_DEV="/dev/vdb"
FS_TYPE="ext4"
MOUNT_POINT="/mnt/data"

if [ "$FS_TYPE" == "zfs" ]; then
  sudo apt install -y linux-headers-$(uname -r) zfs-dkms zfsutils-linux
  sudo modprobe zfs
elif [ "$FS_TYPE" == "xfs" ]; then
  sudo apt install -y xfsprogs
elif [ "$FS_TYPE" == "btrfs" ]; then
  sudo apt install -y btrfs-progs
fi

if grep -q "$MOUNT_POINT" /proc/mounts; then
  echo "Unmounting $MOUNT_POINT..."
  sudo umount "$MOUNT_POINT"
fi

if command -v zpool >/dev/null; then
  if sudo zpool list | grep -q "pool"; then
    echo "Destroying existing ZFS pool..."
    sudo zpool destroy -f pool
  fi
fi
echo "Wiping signatures..."
sudo wipefs --all --force "$DATA_DEV"

sudo mkdir -p "$MOUNT_POINT"

case $FS_TYPE in
xfs)
  echo "Formatting XFS..."
  sudo mkfs.xfs -f -i size=2048 "$DATA_DEV"
  sudo mount -o noatime,inode64 "$DATA_DEV" "$MOUNT_POINT"
  ;;

ext4)
  echo "Formatting EXT4..."
  sudo mkfs.ext4 -F -I 1024 "$DATA_DEV"
  sudo mount -o noatime,user_xattr "$DATA_DEV" "$MOUNT_POINT"
  ;;

btrfs)
  echo "Formatting BTRFS..."
  # Larger metadata node size (multiple inodes in one package) and no duplication
  sudo mkfs.btrfs -f -n 32k -m single "$DATA_DEV"
  # Disable Copy-On-Write mechanism
  sudo mount -o noatime,nodatacow "$DATA_DEV" "$MOUNT_POINT"
  ;;

zfs)
  echo "Creating ZFS Pool..."
  sudo zpool create -f \
    -O mountpoint="$MOUNT_POINT" \
    -O atime=off \
    -O redundant_metadata=most \
    -O dnodesize=auto \
    -O xattr=sa \
    pool "$DATA_DEV"
  ;;

*)
  echo "Error: Unknown Filesystem: $FS_TYPE"
  exit 1
  ;;
esac
