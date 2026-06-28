#!/bin/bash
DATAPATH_ID=0000000000000001
CONTROLLER_IP=10.1.0.213
CONTROLLER_PORT=6653
BRIDGE=br0
PHY_IF=eth0
VLAN_IF=vlan0
VLAN_TAG=100
TRUNKS="100,200"
GATEWAY=10.0.0.1
BROADCAST=10.255.255.255

apt update
apt install -y openvswitch-switch
systemctl enable --now openvswitch-switch

ovs-vsctl add-br "$BRIDGE" \
    -- set bridge "$BRIDGE" other-config:datapath-id=${DATAPATH_ID} \
    -- add-port "$BRIDGE" "$PHY_IF" -- set interface "$BRIDGE" ofport_request=1 \
    -- add-port "$BRIDGE" "$VLAN_IF" -- set interface "$VLAN_IF" ofport_request=2 \
    -- set port "$PHY_IF" vlan_mode=native-untagged tag=$VLAN_TAG \
    -- set port "$PHY_IF" trunks=$TRUNKS \
    -- set-controller "$BRIDGE" tcp:${CONTROLLER_IP}:${CONTROLLER_PORT} \
    -- set-fail-mode "$BRIDGE" standalone

IP_CIDR=$(ip -o -4 addr show dev "${PHY_IF}" | awk '{print $4}')
ip addr flush dev "$PHY_IF"
ip addr add $IP_CIDR brd $BROADCAST dev "$VLAN_IF"
ip route add default via "$GATEWAY" dev "$BRIDGE"
ip link set "$BRIDGE" up
ip link set "$VLAN_IF" up

cat <<'EOF' >> ~/.bashrc
alias ll='ls -lA'
dump-flows () {
  ovs-ofctl -OOpenFlow13 --names --no-stat dump-flows "$@" \
    | sed 's/cookie=0x5adc15c0, //'
}
save-flows () {
  ovs-ofctl -OOpenFlow13 --no-names --sort dump-flows "$@"
}
diff-flows () {
  ovs-ofctl -OOpenFlow13 diff-flows "$@" | sed 's/cookie=0x5adc15c0 //'
}
EOF

# Command to watch pings
# sudo tcpdump -n -i eth0 icmp

