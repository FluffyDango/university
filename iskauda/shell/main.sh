#!/bin/bash

GREEN='\e[1;32m'
YELLOW='\e[1;33m'
RED='\e[1;31m'
CRESET='\e[0m'

# Install opennebula tools and ansible
wget -q -O- https://downloads.opennebula.org/repo/repo.key | sudo apt-key add -
echo "deb [trusted=yes] https://downloads.opennebula.org/repo/5.6/Ubuntu/18.04 stable opennebula" | sudo tee /etc/apt/sources.list.d/opennebula.list
sudo apt update
sudo apt install -y opennebula-tools
sudo apt install -y ansible
sudo apt install -y sshpass
sudo apt install -y python3-passlib



# Generate ssh key and save password with ssh-agent and ssh-add so you don't need to git retype pass every time
echo -e "\nGenerate and add ssh key"
eval `ssh-agent -s`
ssh-keygen -f ~/.ssh/id_rsa
echo "Please enter password for your SSH key: "
ssh-add
echo ""



ENDPOINT=https://grid5.mif.vu.lt/cloud3/RPC2

# Instantiate webserver-vm
while true; do
    read -p "Enter webserver-vm user (empty to skip): " WEB_USER
    if [ -z "$WEB_USER" ]; then
        echo -e "${YELLOW}Skipping webserver-vm${CRESET}"
        WEB_CREATED=false
        break
    fi
    read -p "Enter $WEB_USER password: " -s WEB_PASS
    echo ""
    WEB_REZ=$(onetemplate instantiate 2401 --name "webserver-vm" --user "$WEB_USER" --password "$WEB_PASS" --endpoint $ENDPOINT)
    WEB_ID=$(echo $WEB_REZ |cut -d ' ' -f 3)

    reg='^[0-9]+$'
    if ! [[ "$WEB_ID" =~ $reg ]]; then
        echo "$WEB_REZ"
        echo -e "${RED}Could not create webserver-vm for user $WEB_USER${CRESET}"
    else
        echo -e "${GREEN}Successfuly created webserver-vm id: $WEB_ID${CRESET}"
        WEB_CREATED=true
        break
    fi
done

echo ""

# Instantiate database-vm
while true; do
    read -p "Enter database-vm user (empty to skip): " DATA_USER
    if [ -z "$DATA_USER" ]; then
        echo -e "${YELLOW}Skipping database-vm${CRESET}"
        DATA_CREATED=false
        break
    fi
    read -p "Enter $DATA_USER password: " -s DATA_PASS
    echo ""
    DATA_REZ=$(onetemplate instantiate 2401 --name "database-vm" --user "$DATA_USER" --password "$DATA_PASS" --endpoint $ENDPOINT)
    DATA_ID=$(echo $DATA_REZ |cut -d ' ' -f 3)

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

# Instantiate client-vm
while true; do
    read -p "Enter client-vm user (empty to skip): " CLIENT_USER
    if [ -z "$CLIENT_USER" ]; then
        echo -e "${YELLOW}Skipping client-vm${CRESET}"
        CLIENT_CREATED=false
        break
    fi
    read -p "Enter $CLIENT_USER password: " -s CLIENT_PASS
    echo ""
    CLIENT_REZ=$(onetemplate instantiate 2421 --name "client-vm" --user "$CLIENT_USER" --password "$CLIENT_PASS" --endpoint $ENDPOINT)
    CLIENT_ID=$(echo $CLIENT_REZ |cut -d ' ' -f 3)

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

# Wait for vms to start
echo "(Press any key to skip)"
SEC_LEFT=45
while [ $SEC_LEFT -gt 0 ]; do
    echo -ne "${YELLOW}Waiting ${RED}$SEC_LEFT ${YELLOW}seconds for VM to run\r"
    
    read -t 1 -n 1 key
    if [ $? -eq 0 ]; then
        echo -e "\n${YELLOW}Countdown skipped by user."
        break
    fi

    ((SEC_LEFT--))
done
echo -e "${GREEN}\nI have waited for long enough\n${CRESET}"



# Copy private ips and connections strings from files
if $WEB_CREATED; then
    echo -e "Retrieving info about webserver-vm"
    onevm show $WEB_ID --user $WEB_USER --password $WEB_PASS --endpoint $ENDPOINT > $WEB_ID.txt
    WEB_CON=$(cat $WEB_ID.txt | grep CONNECT\_INFO1| cut -d '=' -f 2 | tr -d '"'|sed 's/'$WEB_USER'/root/')
    WEB_IP=$(cat $WEB_ID.txt | grep PRIVATE\_IP| cut -d '=' -f 2 | tr -d '"')
    WEB_PUBLIC_IP=$(cat $WEB_ID.txt | grep PUBLIC\_IP| cut -d '=' -f 2 | tr -d '"')
    WEB_PORT_80=$(cat $WEB_ID.txt | grep 'TCP_PORT_FORWARDING=' | sed 's/.* \([0-9]\+\):80.*/\1/')
    WEB_PORT_3389=$(cat $WEB_ID.txt | grep 'TCP_PORT_FORWARDING=' | sed 's/.* \([0-9]\+\):3389.*/\1/')
    echo -e "${GREEN}Successfully retrieved info about webserver-vm\nPrivate_ip: $WEB_IP\nPublic_ip: $WEB_PUBLIC_IP\nPort_80: $WEB_PORT_80:80\nPort 3389: $WEB_PORT_3389:3389\n${CRESET}"
fi

if $DATA_CREATED; then
    echo "Retrieving info about database-vm"
    onevm show $DATA_ID --user $DATA_USER --password $DATA_PASS --endpoint $ENDPOINT > $DATA_ID.txt
    DATA_CON=$(cat $DATA_ID.txt | grep CONNECT\_INFO1| cut -d '=' -f 2 | tr -d '"'|sed 's/'$DATA_USER'/root/')
    DATA_IP=$(cat $DATA_ID.txt | grep PRIVATE\_IP| cut -d '=' -f 2 | tr -d '"')
    DATA_PUBLIC_IP=$(cat $DATA_ID.txt | grep PUBLIC\_IP| cut -d '=' -f 2 | tr -d '"')
    DATA_PORT_80=$(cat $DATA_ID.txt | grep 'TCP_PORT_FORWARDING=' | sed 's/.* \([0-9]\+\):80.*/\1/')
    echo -e "${GREEN}Successfully retrieved info about database-vm\nPrivate ip: $DATA_IP\n${CRESET}"
fi

if $CLIENT_CREATED; then
    echo "Retrieving info about client-vm"
    onevm show $CLIENT_ID --user $CLIENT_USER --password $CLIENT_PASS --endpoint $ENDPOINT > $CLIENT_ID.txt
    CLIENT_CON=$(cat $CLIENT_ID.txt | grep CONNECT\_INFO1| cut -d '=' -f 2 | tr -d '"'|sed 's/'$CLIENT_USER'/root/')
    CLIENT_IP=$(cat $CLIENT_ID.txt | grep PRIVATE\_IP| cut -d '=' -f 2 | tr -d '"')
    CLIENT_PUBLIC_IP=$(cat $CLIENT_ID.txt | grep PUBLIC\_IP| cut -d '=' -f 2 | tr -d '"')
    CLIENT_PORT_22=$(cat $CLIENT_ID.txt | grep 'TCP_PORT_FORWARDING=' | sed 's/.* \([0-9]\+\):22.*/\1/')
    CLIENT_PORT_3389=$(cat $CLIENT_ID.txt | grep 'TCP_PORT_FORWARDING=' | sed 's/.* \([0-9]\+\):3389.*/\1/')
    echo -e "${GREEN}Successfully retrieved info about client-vm\nPrivate ip: $CLIENT_IP\n${CRESET}"
fi



# Initial password set in vm template
SUDO_PASS=password

# Copy ssh key to remote machines
if $WEB_CREATED; then
    echo "Copying ssh key to websever-vm at $WEB_USER@$WEB_IP"
    sshpass -p "$SUDO_PASS" ssh-copy-id -o StrictHostKeyChecking=no -f "$WEB_USER@$WEB_IP"
    echo -e "${GREEN}Successfully copied ssh key to webserver-vm\n${CRESET}"
fi
if $DATA_CREATED; then
    echo "Copying ssh key to database-vm at $DATA_USER@$DATA_IP"
    sshpass -p "$SUDO_PASS" ssh-copy-id -o StrictHostKeyChecking=no -f "$DATA_USER@$DATA_IP"
    echo -e "${GREEN}Successfully copied ssh key to database-vm\n${CRESET}"
fi
if $CLIENT_CREATED; then
    echo "Copying ssh key to client-vm at $CLIENT_USER@$CLIENT_IP"
    sshpass -p "$SUDO_PASS" ssh-copy-id -o StrictHostKeyChecking=no -f -p "$CLIENT_PORT_22" "$CLIENT_USER@$CLIENT_PUBLIC_IP"
    echo -e "${GREEN}Successfully copied ssh key to client-vm\n${CRESET}"
fi



#Create vault and store sudo password for vm's
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
printf -- "---\nsudo_pass: \"$SUDO_PASS\"\nnew_sudo_pass: \"$NEW_SUDO_PASS\"\n" > vault.yml
printf "webserver_private_ip: \"$WEB_IP\"\nwebserver_public_ip: \"$WEB_PUBLIC_IP\"\nwebserver_port: \"$WEB_PORT_80\"\n" >> vault.yml
printf "database_private_ip: \"$DATA_IP\"\ndatabase_public_ip: \"$DATA_PUBLIC_IP\"\ndatabase_port_80: \"$DATA_PORT_80\"\n" >> vault.yml

if $DATA_CREATED; then
    while true; do
        read -p "Enter new database password: " -s DATABASE_PASSWORD
        echo ""
        read -p "Reenter new database password: " -s DATABASE_PASSWORD2
        echo ""
        if [ "$DATABASE_PASSWORD" == "$DATABASE_PASSWORD2" ]; then
            printf "database_password: \"$DATABASE_PASSWORD\"" >> vault.yml
            echo -e "${GREEN}Database password successfully added to vault.yml${CRESET}"
            break
        else
            echo -e "${RED}Passwords do not match, please try again${CRESET}"
        fi
    done
fi
echo ""

while true; do
    ansible-vault encrypt vault.yml
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Successfully set up vault.yml\n${CRESET}"
        break
    else
        echo "${RED}Vault encryption failed, please try again${CRESET}"
    fi
done
echo -e ""

echo "Creating hosts file"
echo "" > hosts
if $WEB_CREATED; then
    printf "[webservers]\n$WEB_USER@$WEB_IP\n\n" >> hosts
fi
if $DATA_CREATED; then
    printf "[database]\n$DATA_USER@$DATA_IP\n\n" >> hosts
fi
if $CLIENT_CREATED; then
    printf "[clients]\n$CLIENT_USER@$CLIENT_IP" >> hosts
fi
echo -e "${GREEN}Successfully created hosts file\n"

echo "Pinging remote machines with ansible"
ansible all -m ping -i ./hosts
echo ""



if $WEB_CREATED; then
    echo "Running webserver.yaml playbook"
    ansible-playbook ../ansible/webserver.yaml -i ./hosts --ask-vault-pass
fi
if $DATA_CREATED; then
    echo "Running database.yaml playbook"
    ansible-playbook ../ansible/database.yaml -i ./hosts --ask-vault-pass
fi
if $CLIENT_CREATED; then
    echo "Running client.yaml playbook"
    ansible-playbook ../ansible/client.yaml -i ./hosts --ask-vault-pass

    echo "[ Linux ] Connect to client-vm with rdesktop $CLIENT_PUBLIC_IP:$CLIENT_PORT_3389"
    echo "[ Windows ] Connect to client-vm with mstsc.exe /v:$CLIENT_PUBLIC_IP:$CLIENT_PORT_3389"
    echo "Connect to website with www.iskauda.com:$WEB_PORT_80"
    echo "Or with https://$WEB_PUBLIC_IP:$WEB_PORT_80"
fi