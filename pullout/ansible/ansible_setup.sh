#!/bin/bash

# This script was originally made by Krištapavičius Anupras for virtualization project with team members:
# Janiūnas Domas
# Krištapavičius Anupras
# Narbutas Renaldas
# Trubila Kipras

# It was slightly modified to fit our project.

GREEN='\e[1;32m'
YELLOW='\e[1;33m'
RED='\e[1;31m'
ORANGE='\e[1;35m'
CRESET='\e[0m'

# Get opennebula repo and install opennebula tools
wget -q -O- https://downloads.opennebula.org/repo/repo.key | sudo apt-key add -
echo "deb [trusted=yes] https://downloads.opennebula.org/repo/5.6/Ubuntu/18.04 stable opennebula" | sudo tee /etc/apt/sources.list.d/opennebula.list
sudo apt update
sudo apt install -y opennebula-tools ansible sshpass python3-passlib python3-psycopg2



# Generate ssh key and save password with ssh-agent and ssh-add so you don't need to git retype pass every time
echo -e "\nGenerate and add ssh key"
eval `ssh-agent -s`
ssh-keygen -f ~/.ssh/id_rsa
echo "Please enter password for your SSH key: "
ssh-add
echo ""



ENDPOINT=https://grid5.mif.vu.lt/cloud3/RPC2

# --------------------------------------------------
# CLIENT Creation
while true; do
    # Skip if empty input
    read -p "Enter client-vm user (empty to skip): " CLIENT_USER
    if [ -z "$CLIENT_USER" ]; then
        echo -e "${YELLOW}Skipping client-vm${CRESET}"
        CLIENT_CREATED=false
        break
    fi

    # Get password and echo for newline
    read -p "Enter $CLIENT_USER password: " -s CLIENT_PASS
    echo ""

    # Create vm with template id
    CLIENT_REZ=$(onetemplate instantiate 2427 --name "client-vm" --user "$CLIENT_USER" --password "$CLIENT_PASS" --endpoint $ENDPOINT)
    CLIENT_ID=$(echo $CLIENT_REZ |cut -d ' ' -f 3)

    # Check if vm was created
    reg='^[0-9]+$'
    if ! [[ "$CLIENT_ID" =~ $reg ]]; then
        echo "$CLIENT_REZ"
        echo -e "${RED}Could not create client-vm for user $CLIENT_USER${CRESET}"
    else
        echo -e "${GREEN}Successfuly created client-vm id: $CLIENT_ID${CRESET}"
        CLIENT_CREATED=true
        break
    fi
done

echo ""

# --------------------------------------------------
# DATABASE Creation
while true; do
    read -p "Enter database-vm user (empty to skip): " DATA_USER
    # Skip if empty input
    if [ -z "$DATA_USER" ]; then
        echo -e "${YELLOW}Skipping database-vm${CRESET}"
        DATA_CREATED=false
        break
    fi
    # Get password and echo for newline
    read -p "Enter $DATA_USER password: " -s DATA_PASS
    echo ""

    # Create vm with template id
    DATA_REZ=$(onetemplate instantiate 2426 --name "database-vm" --user "$DATA_USER" --password "$DATA_PASS" --endpoint $ENDPOINT)
    DATA_ID=$(echo $DATA_REZ |cut -d ' ' -f 3)

    # Check if vm was created
    reg='^[0-9]+$'
    if ! [[ "$DATA_ID" =~ $reg ]]; then
        echo "$DATA_REZ"
        echo -e "${RED}Could not create database-vm for user $DATA_USER${CRESET}"
    else
        echo -e "${GREEN}Successfuly created database-vm id: $DATA_ID${CRESET}"
        DATA_CREATED=true
        break
    fi
done

echo ""

# If no vm's were created, exit
if ! $DATA_CREATED && ! $CLIENT_CREATED; then
    echo -e "${RED}No vm's were created, exiting${CRESET}"
    exit 1
fi

# --------------------------------------------------
# Wait for vms to start
echo "(Press 'w' to increase wait time or 's' to lower wait time)"
echo "(Press any other key to skip)"
SEC_LEFT=45
while [ $SEC_LEFT -gt 0 ]; do
    echo -ne "${YELLOW}Waiting ${RED}$SEC_LEFT ${YELLOW}seconds for VM to run \r"
    
    # Wait for 1 second or until user presses a key
    read -t 1 -n 1 KEY_PRESS
    if [ $? -eq 0 ]; then
        if [ "$KEY_PRESS" == 'w' ]; then
            echo -e "\n${YELLOW}Wait time increased by 10 seconds."
            ((SEC_LEFT+=10))
        elif [ "$KEY_PRESS" == 's' ]; then
            echo -e "\n${YELLOW}Wait time decreased by 10 seconds."
            ((SEC_LEFT-=10))
        else
            echo -e "\n${YELLOW}Countdown skipped by user."
            break
        fi
    fi

    ((SEC_LEFT--))
done


# --------------------------------------------------
# Download info about vm's and extract info from it
if $CLIENT_CREATED; then
    echo "Retrieving info about client-vm"
    onevm show $CLIENT_ID --user $CLIENT_USER --password $CLIENT_PASS --endpoint $ENDPOINT > client-vm-info.txt
    CLIENT_SSH_CON=$(cat client-vm-info.txt | grep CONNECT\_INFO1| cut -d '=' -f 2 | tr -d '"')
    CLIENT_PRIVATE_IP=$(cat client-vm-info.txt | grep PRIVATE\_IP| cut -d '=' -f 2 | tr -d '"')
    CLIENT_PUBLIC_IP=$(cat client-vm-info.txt | grep PUBLIC\_IP| cut -d '=' -f 2 | tr -d '"')
    CLIENT_PORT_22=$(cat client-vm-info.txt | grep 'TCP_PORT_FORWARDING=' | sed 's/.*="\([0-9]\+\):22.*/\1/')
    echo -e "${GREEN}Successfully retrieved info about client-vm\n\
        SSH Connection: $CLIENT_SSH_CON\n\
        Client private ip: $CLIENT_PRIVATE_IP\n\
        Client public ip: $CLIENT_PUBLIC_IP\n\
        Client port for 22: $CLIENT_PORT_22${CRESET}"
fi

if $DATA_CREATED; then
    echo "Retrieving info about database-vm"
    onevm show $DATA_ID --user $DATA_USER --password $DATA_PASS --endpoint $ENDPOINT > database-vm-info.txt
    DATABASE_SSH_CON=$(cat database-vm-info.txt | grep CONNECT\_INFO1| cut -d '=' -f 2 | tr -d '"')
    DATABASE_PRIVATE_IP=$(cat database-vm-info.txt | grep PRIVATE\_IP| cut -d '=' -f 2 | tr -d '"')
    DATABASE_PUBLIC_IP=$(cat database-vm-info.txt | grep PUBLIC\_IP| cut -d '=' -f 2 | tr -d '"')
    DATABASE_PORT_22=$(cat database-vm-info.txt | grep 'TCP_PORT_FORWARDING=' | sed 's/.*="\([0-9]\+\):22.*/\1/')
    DATABASE_PORT_80=$(cat database-vm-info.txt | grep 'TCP_PORT_FORWARDING=' | sed 's/.* \([0-9]\+\):80.*/\1/')
    echo -e "${GREEN}Successfully retrieved info about database-vm\n\
        SSH Connection: $DABASE_SSH_CON\n\
        Private ip: $DATABASE_PRIVATE_IP\n\
        Public_ip: $DATABASE_PUBLIC_IP\n\
        Generated port for 22: $DATABASE_PORT_22\n\
        Generated port for 80: $DATABASE_PORT_80${CRESET}"
fi


# --------------------------------------------------
# Initial password set in vm template
SUDO_PASS=iloveunix

# Copying ssh keys to vm's using private ip except client
# Client is on vnet1 and can only be accessed through public ip with generated port on port 22
if $CLIENT_CREATED; then
    echo "Copying ssh key to client-vm at $CLIENT_USER@$CLIENT_PUBLIC_IP"
    sshpass -p "$SUDO_PASS" ssh-copy-id -o StrictHostKeyChecking=no -f -p "$CLIENT_PORT_22" "$CLIENT_USER@$CLIENT_PUBLIC_IP"
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Successfully copied ssh key to client-vm\n${CRESET}"
    else
        echo -e "${RED}Failed to copy ssh key to client-vm.${CRESET}"
        echo "(press 'y' to continue or any other key to exit)"
        read -n 1 -s KEY_PRESS
        if [ "$KEY_PRESS" != 'y' ]; then
            echo -e "${RED}Exiting${CRESET}"
            exit 1
        fi
    fi
fi
if $DATA_CREATED; then
    echo "Copying ssh key to database-vm at $DATA_USER@$DATABASE_PRIVATE_IP"
    sshpass -p "$SUDO_PASS" ssh-copy-id -o StrictHostKeyChecking=no -f "$DATA_USER@$DATABASE_PRIVATE_IP"
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Successfully copied ssh key to database-vm\n${CRESET}"
    else
        echo -e "${RED}Failed to copy ssh key to database-vm.${CRESET}"
        echo "(press 'y' to continue or any other key to exit)"
        read -n 1 -s KEY_PRESS
        if [ "$KEY_PRESS" != 'y' ]; then
            echo -e "${RED}Exiting${CRESET}"
            exit 1
        fi
    fi
fi


# --------------------------------------------------
# Create vault and store variables used in playbooks
echo "Setting up ansible vault"

while true; do
    read -p "Enter new sudo password: " -s NEW_SUDO_PASS
    echo ""
    read -p "Reenter new sudo password: " -s NEW_SUDO_PASS2
    echo ""
    if [ "$NEW_SUDO_PASS" == "$NEW_SUDO_PASS2" ]; then
        echo -e "${GREEN}New sudo password successfully added to vault.yml${CRESET}"
        break
    else
        echo -e "${RED}Passwords do not match, please try again${CRESET}"
    fi
done

echo ""
# Need to add -- because the string starts with "---" and messes up printf
printf -- "---\nsudo_pass: \"$SUDO_PASS\"\nnew_sudo_pass: \"$NEW_SUDO_PASS\"\n" > vault.yml
printf "database_private_ip: \"$DATABASE_PRIVATE_IP\"\ndatabase_public_ip: \"$DATABASE_PUBLIC_IP\"\n" >> vault.yml
printf "database_port_80: \"$DATABASE_PORT_80\"\n" >> vault.yml
printf "client_ssh: \"$CLIENT_SSH_CON\"\ndatabase_ssh: \"$DATABASE_SSH_CON\"\n" >> vault.yml

# Set database password
# if $DATA_CREATED; then
#     while true; do
#         read -p "Enter new database password: " -s DATABASE_PASSWORD
#         echo ""
#         read -p "Reenter new database password: " -s DATABASE_PASSWORD2
#         echo ""
#         if [ "$DATABASE_PASSWORD" == "$DATABASE_PASSWORD2" ]; then
#             printf "database_password: \"$DATABASE_PASSWORD\"" >> vault.yml
#             echo -e "${GREEN}Database password successfully added to vault.yml${CRESET}"
#             break
#         else
#             echo -e "${RED}Passwords do not match, please try again${CRESET}"
#         fi
#     done
# fi
# echo ""

ansible-vault encrypt vault.yml
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Successfully set up vault.yml\n${CRESET}"
else
    echo "${RED}Vault encryption failed, are you sure you want to continue?${CRESET}"
    echo "(press 'y' to continue or any other key to exit)"
    read -n 1 -s KEY_PRESS
    if [ "$KEY_PRESS" != 'y' ]; then
        echo -e "${RED}Exiting${CRESET}"
        exit 1
    fi
fi
echo ""

# --------------------------------------------------
# Create hosts file
echo "Creating hosts file"
echo "" > hosts
if $DATA_CREATED; then
    printf "[database]\n$DATA_USER@$DATABASE_PRIVATE_IP\n\n" >> hosts
fi
# Client needs port 22 because it is on vnet1 and uses public ip
if $CLIENT_CREATED; then
    printf "[clients]\n$CLIENT_USER@$CLIENT_PUBLIC_IP ansible_port=$CLIENT_PORT_22"  >> hosts
fi
echo -e "${GREEN}Successfully created hosts file\n${CRESET}"

# --------------------------------------------------
# Ping to see if everything is working
echo "Pinging remote machines with ansible"
ansible all -m ping -i hosts
if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}Successfully pinged all machines\n${CRESET}"
else
    echo ""
    echo -e "${RED}Ping failed, are you sure you want to continue${CRESET}"
    echo "(press 'y' to continue or any other key to exit)"
    read -n 1 -s KEY_PRESS
    if [ "$KEY_PRESS" != 'y' ]; then
        echo -e "${RED}Exiting${CRESET}"
        exit 1
    fi
fi

# --------------------------------------------------
# Run playbooks
if $CLIENT_CREATED; then
    echo "Running client.yaml playbook"
    ansible-playbook pullout.yaml -i hosts --ask-vault-pass
        if [ $? -eq 0 ]; then
        echo -e "${GREEN}Successfully finished\n${CRESET}"
    else
        echo -e "${ORANGE}Failed. Try again later with\nansible-playbook client.yaml -i hosts --ask-vault-pass\n${CRESET}"
    fi
fi
if $DATA_CREATED; then
    echo "Running database.yaml playbook"
    ansible-playbook database.yaml -i hosts --ask-vault-pass
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Successfully finished\n${CRESET}"
    else
        echo -e "${ORANGE}Failed. Try again later with\nansible-playbook database.yaml -i hosts --ask-vault-pass\n${CRESET}"
    fi
fi

echo "[ Client ] $CLIENT_SSH_CON"
echo "[ Database ] $DATABASE_SSH_CON"
echo "To sync client with database write:"
echo "[1] pullout --init ${DATABASE_PUBLIC_IP}:${DATABASE_PORT_80}"
echo "[2] pullout --sync"