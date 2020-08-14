#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive

set -x

apt-get install -yq software-properties-common
apt-get install -yq lsb-release

cd hello-docker-build

  apt-get remove docker docker-engine docker.io
  apt-get install -y apt-transport-https ca-certificates curl software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"
  apt-get update
  apt-get install -y docker-ce

  docker build -t logickee/drone-docker-builder .

  docker login
  docker push

cd
