#!/bin/bash

set -e

# Script for installing:
# Prometheus
# Node exporter
# Grafana

# https://github.com/prometheus/prometheus/releases
PROMETHEUS_VER=3.7.3
# https://github.com/prometheus/node_exporter/releases
NODE_EXPORTER_VER=1.10.2

SCRIPT_DIR="$(cd -- "$(dirname -- "$0")" && pwd)"

if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root"
    exit 1
fi

install_prometheus() {
    echo "======================================="
    echo "    Installing Prometheus              "
    echo "======================================="
    wget https://github.com/prometheus/prometheus/releases/download/v${PROMETHEUS_VER}/prometheus-${PROMETHEUS_VER}.linux-amd64.tar.gz
    tar xvfz prometheus-*.tar.gz
    cd prometheus-*linux-amd64
    mv prometheus /usr/local/bin/
    mv promtool /usr/local/bin/
    cd ..
    rm -r prometheus-*
    id -u prometheus || useradd -rs /bin/false prometheus
    mkdir -p /etc/prometheus
    mkdir -p /var/lib/prometheus
    [ ! -f /etc/prometheus/prometheus.yml ] && cp "$SCRIPT_DIR/../configs/prometheus.yml" /etc/prometheus/
    chown -R prometheus:prometheus /etc/prometheus
    chown -R prometheus:prometheus /var/lib/prometheus
    chown prometheus:prometheus /usr/local/bin/prometheus
    chown prometheus:prometheus /usr/local/bin/promtool
    [ ! -f /etc/systemd/system/prometheus.service ] && cp "$SCRIPT_DIR/../configs/prometheus.service" /etc/systemd/system/prometheus.service
    systemctl daemon-reload
    systemctl enable --now prometheus
}

install_node_exporter() {
    echo "======================================="
    echo "    Installing Node exporter           "
    echo "======================================="
    wget https://github.com/prometheus/node_exporter/releases/download/v${NODE_EXPORTER_VER}/node_exporter-${NODE_EXPORTER_VER}.linux-amd64.tar.gz
    tar xvfz node_exporter-*.tar.gz
    cd node_exporter*.linux-amd64
    mv node_exporter /usr/local/bin/
    cd ..
    rm -r node_exporter*
    id -u node_exporter || useradd -rs /bin/false node_exporter
    [ ! -f /etc/systemd/system/node_exporter.service ] && cp "$SCRIPT_DIR/../configs/node_exporter.service" /etc/systemd/system/node_exporter.service
    systemctl daemon-reload
    systemctl enable --now node_exporter
}

install_grafana() {
    echo "======================================="
    echo "    Installing Grafana                 "
    echo "======================================="
    apt update
    apt install -y apt-transport-https gnupg2 curl
    mkdir -p /etc/apt/keyrings/
    curl -fsSL https://apt.grafana.com/gpg.key | gpg --dearmor -o /etc/apt/keyrings/grafana.gpg
    echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | tee /etc/apt/sources.list.d/grafana.list
    apt-get update
    apt-get install -y grafana
    systemctl enable --now grafana-server
}

#install_prometheus
install_node_exporter
#install_grafana
