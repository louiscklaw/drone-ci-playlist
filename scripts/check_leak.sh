#!/usr/bin/env bash

set -x

sudo rm -rf .ssh
sudo rm -rf .npm
sudo rm -rf .config

set -ex

python3 check-leak/main.py
