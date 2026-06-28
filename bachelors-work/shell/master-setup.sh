#!/bin/bash
set -e

# curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# unzip awscliv2.zip
# sudo ./aws/install
#
# rm awscliv2.zip
# rm -r aws

# Generate default rsa key to access the nodes through ssh without password
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa

export TERM=xterm

printf '%s\n' \
  '10.0.0.25 node0' \
  '10.0.0.87 node1' \
  '10.0.0.86 node2' \
  '10.0.0.48 node3' | sudo tee -a /etc/hosts

for node in node0 node1 node2 node3; do
  ssh-keyscan -H $node >>~/.ssh/known_hosts
done

for node in node0 node1 node2 node3; do
  ssh-copy-id rena9048@$node
done

wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
sudo mv mc /usr/bin/
mc alias set myminio http://node0:80 minioadmin minioadmin

wget https://github.com/minio/warp/releases/latest/download/warp_Linux_x86_64.tar.gz
tar -xzf warp_Linux_x86_64.tar.gz
chmod +x warp
sudo mv warp /usr/bin/

sudo apt install jq -y
