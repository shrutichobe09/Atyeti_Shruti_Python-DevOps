#!/bin/bash
apt update && apt install -y unzip curl jq gnupg

VAULT_VERSION="1.15.0"

# Download Vault
curl -fsSL https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip -o vault.zip
unzip vault.zip
mv vault /usr/local/bin/
chmod +x /usr/local/bin/vault

useradd --system --home /etc/vault.d --shell /bin/false vault
mkdir -p /etc/vault.d /opt/vault/data
chown -R vault:vault /etc/vault.d /opt/vault

# Vault Config
cat <<EOF > /etc/vault.d/vault.hcl
storage "raft" {
  path    = "/opt/vault/data"
  node_id = "vault-1"
}

listener "tcp" {
  address     = "0.0.0.0:8200"
  tls_disable = "true"
}

seal "gcpckms" {
  project     = "rosy-resolver-465404-b2"
  region      = "us-central1"
  key_ring    = "vault-keyring"
  crypto_key  = "vault-key"


ui            = true
disable_mlock = true
api_addr      = "http://0.0.0.0:8200"
cluster_addr  = "http://0.0.0.0:8201"
EOF

chown -R vault:vault /etc/vault.d

cat <<EOF > /etc/systemd/system/vault.service
[Unit]
Description=Vault Server
After=network.target

[Service]
User=vault
Group=vault
ExecStart=/usr/local/bin/vault server -config=/etc/vault.d/vault.hcl
ExecReload=/bin/kill --signal HUP \$MAINPID
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reexec
systemctl enable vault
systemctl start vault
