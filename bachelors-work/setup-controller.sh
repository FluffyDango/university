#!/bin/bash
set -euo pipefail

YELLOW='\e[1;33m'
GREEN='\e[1;32m'
RED='\e[1;31m'
CRESET='\e[0m'

CREATE_VM_IDS_FILE="created_vm_ids.txt"
VM_INFO_FILE="vm_info.txt"
DEFAULT_SUDO_PASS=temp
ENDPOINT="https://grid5.mif.vu.lt/cloud3/RPC2"

main() {
  apt_update_and_install
  read -p "Enter username: " USERNAME
  read -p "Enter $USERNAME password: " -s PASSWORD
  echo ""
  create_vms
  setup_ssh
  setup_ansible
}

apt_update_and_install() {
  echo "deb http://download.opennebula.org/repo/7.0/debian-bullseye bionic main" | sudo tee /etc/apt/sources.list.d/opennebula-repo.list
  sudo apt update && sudo apt upgrade -y
  sudo apt install -y vim ansible sshpass python3-passlib
}

create_vms() {
  # If already exists, then remove it
  if [ -s "$VM_INFO_FILE" ]; then
    rm $CREATE_VM_IDS_FILE
  fi

  INDEX=0
  while [ $INDEX -lt 3 ]; do
    REZ=$(onetemplate instantiate 2922 --name "debian13_${INDEX}" --user "$USERNAME" --password "$PASSWORD" --endpoint $ENDPOINT)
    VM_ID=$(echo $REZ | cut -d ' ' -f 3)
    reg='^[0-9]+$'
    if ! [[ "$VM_ID" =~ $reg ]]; then
      log_message_red "Could not create VM for user $USERNAME"
    else
      log_message_green "Successfully created VM id: $VM_ID with name debian13_$INDEX"
      echo "$VM_ID" >>"$CREATE_VM_IDS_FILE"
      ((INDEX++))
    fi
  done

  # Wait for VMs to start
  echo "(Press any key to skip)"
  SEC_LEFT=45
  while [ $SEC_LEFT -gt 0 ]; do
    log_message_yellow "Waiting ${RED}$SEC_LEFT ${YELLOW}seconds for VM to run"
    read -t 1 -n 1 key
    if [ $? -eq 0 ]; then
      log_message_yellow "Countdown skipped by user."
      break
    fi
    ((SEC_LEFT--))
  done
  log_message_green "\nWaiting finished.\n"
}

setup_ssh() {
  echo -e "\nGenerate and add ssh key"
  eval $(ssh-agent -s)
  SSH_KEY_FILE=~/.ssh/id_rsa
  if [ ! -f "$SSH_KEY_FILE" ]; then
    log_message_yellow "No existing SSH key found, generating a new one..."
    ssh-keygen -f $SSH_KEY_FILE
    echo ""
  else
    log_message_green "Existing SSH key found, reusing it..."
    eval $(ssh-agent -s)
    ssh-add $SSH_KEY_FILE
    echo ""
  fi

  CREATE_VM_IDS=()
  while IFS= read -r line; do
    CREATE_VM_IDS+=("$line")
  done <"$CREATE_VM_IDS_FILE"

  # If already exists, then remove it
  if [ -s "$VM_INFO_FILE" ]; then
    rm $VM_INFO_FILE
  fi

  for id in "${CREATE_VM_IDS[@]}"; do
    VM_INFO=$(onevm show $id --user $USERNAME --password $PASSWORD --endpoint $ENDPOINT)
    SSH_CONNECTION_COMMAND=$(echo "$VM_INFO" | grep CONNECT\_INFO1 | cut -d '=' -f 2 | tr -d '"' | sed 's/'$USERNAME'/root/')
    PRIVATE_IP=$(echo "$VM_INFO" | grep PRIVATE\_IP | cut -d '=' -f 2 | tr -d '"')
    VM_NAME=$(echo "$VM_INFO") # To do
    INFO_LINE="${VM_NAME},${id},${PRIVATE_IP},${SSH_CONNECTION_COMMAND}"
    log_message_green "Successfully retrieved info about $id\n${INFO_LINE}"
    echo "$INFO_LINE" >>$VM_INFO_FILE

    log_message_debug "Copying ssh key to websever-vm at $WEB_USER@$WEB_IP"
    sshpass -p "$DEFAULT_SUDO_PASS" ssh-copy-id -o StrictHostKeyChecking=no -f "$USERNAME@$PRIVATE_IP"
    log_message_green "Successfully copied ssh key to webserver-vm\n"
  done
}

setup_ansible() {
  echo "Setting up ansible vault"

  while true; do
    read -p "Enter new sudo password for VMs: " -s NEW_SUDO_PASS
    echo ""
    read -p "Reenter new sudo password for VMs: " -s NEW_SUDO_PASS2
    echo ""
    if [ "$NEW_SUDO_PASS" == "$NEW_SUDO_PASS2" ]; then
      log_message_green "New sudo password successfully added to vault.yml"
      break
    else
      log_message_red "Passwords do not match, please try again"
    fi
  done

  log_message_debug "Creating hosts file and setting vault.yml"
  echo "[cluster]" >hosts
  printf -- "---\ndefault_sudo_pass: \"$DEFAULT_SUDO_PASS\"\nnew_sudo_pass: \"$NEW_SUDO_PASS\"\n" >vault.yml
  while IFS= read -r line; do
    IFS=',' read -ra info <<<"$line"
    VM_NAME="${info[0]}"
    PRIVATE_IP="${info[2]}"
    echo "${VM_NAME}_private_ip: \"${PRIVATE_IP}\"\n${VM_NAME}_port: \"$VM_NAME\"\n" >>vault.yml # Port todo
    echo "${USERNAME}@${PRIVATE_IP}" >>hosts
  done <"${VM_INFO_FILE}"
  log_message_green "Successfully created hosts file\n"

  while true; do
    ansible-vault encrypt vault.yml
    if [ $? -eq 0 ]; then
      log_message_green "Successfully set up vault.yml\n"
      break
    else
      log_message_red "Vault encryption failed, please try again"
    fi
  done
  echo ""

  echo "Pinging remote machines with ansible"
  ansible all -m ping -i ./hosts
  echo ""
}

run_ansible_playbooks() {
  log_message_debug "Running playbook"
  ansible-playbook ./ansible/zsh-setup.yml -i ./hosts --ask-vault-pass

  # Print out connection to the VMs
  while IFS= read -r line; do
    IFS=',' read -ra info <<<"$line"
    VM_NAME="${info[0]}"
    SSH_CONNECTION_COMMAND="${info[3]}"
    echo "SSH Connection ${VM_NAME}: ${SSH_CONNECTION_COMMAND}"
  done <"$VM_INFO_FILE"
}

log_message_debug() {
  echo -e "[DEBUG $(date +'%H:%M:%S')] $1" >&2
}
log_message_yellow() {
  echo -e "${YELLOW}${1}${CRESET}" >&2
}
log_message_green() {
  echo -e "${GREEN}${1}${CRESET}" >&2
}
log_message_red() {
  echo -e "${RED}${1}${CRESET}" >&2
}

main
