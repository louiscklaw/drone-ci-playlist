#!/usr/bin/env bash

set -ex

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -yq software-properties-common

add-apt-repository -y ppa:freecad-maintainers/freecad-stable
apt-get install -yq freecad freecad-python3

mkdir -p /usr/lib/freecad-python3/Mod

for i in $(find . -name '*.FCStd'); do
  python3 freecad_open_test.py $i;
done
