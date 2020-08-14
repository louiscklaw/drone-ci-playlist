#!/usr/bin/env bash

set -ex

if [[ -e /etc/docker/daemon.json ]]; then
  echo 'daemon.json already exists, skipping... '

else
  echo "update daemon.json"
  cat <<EOT >> /etc/docker/daemon.json
{
  "default-address-pools":
  [
    {"base":"10.10.0.0/16","size":24}
  ]
}
EOT
fi
