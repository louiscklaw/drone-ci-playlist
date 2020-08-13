#!/usr/bin/env bash

set -x

sudo rm -rf .ssh
sudo rm -rf .npm
sudo rm -rf .config

set -ex

script/check_leak.sh

python3 scripts/build_main_drone.py
sleep 0.5

echo 'rebuild main drone done'
