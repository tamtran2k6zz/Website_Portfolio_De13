#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
mkdir -p certs
if [ -e certs/server.key ]; then echo 'Certificate already exists; refusing to overwrite.' >&2; exit 1; fi
openssl req -x509 -nodes -newkey rsa:3072 -sha256 -days 30 \
  -keyout certs/server.key -out certs/server.crt \
  -subj '/CN=localhost' -addext 'subjectAltName=DNS:localhost,IP:127.0.0.1'
# Nginx runs as UID 101. Protect the host directory, allow container process to read the bind-mounted key.
chmod 700 certs
chmod 644 certs/server.key certs/server.crt
echo 'Created a self-signed certificate valid for 30 days. Private key stays gitignored.'
