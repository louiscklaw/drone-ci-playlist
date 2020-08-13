#!/usr/bin/env bash

set -ex

python3 scripts/build_main_drone.py

sleep 0.5

echo 'rebuild main drone done'
