#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive

set -ex

apt-get update
apt-get install -yq git
apt-get install -yq software-properties-common
apt-get install -yq lsb-release

# not necessary for a build in fresh docker image
# apt-get remove docker docker-engine docker.io

apt-get install -yq apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"
apt-get install -yq docker-ce
