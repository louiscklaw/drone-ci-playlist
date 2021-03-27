#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive

set -x

apt-get update
apt-get install -yq software-properties-common
apt-get install -yq lsb-release

docker build .
