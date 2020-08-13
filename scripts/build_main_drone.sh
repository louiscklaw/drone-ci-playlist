#!/usr/bin/env bash

set -ex


pwd

sudo chmod 775 .ssh

python3 check-leak/main.py

python3 scripts/build_main_drone.py
sleep 0.5

echo 'rebuild main drone done'
