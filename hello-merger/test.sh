#!/usr/bin/env sh

set -x

id

pwd

cd

pwd

apt-get update

apt-get install -y git
apt-get install -y python3 python3-pip

python3 -m pip install pipenv

cd hello-merger/old_util
  pipenv sync
  pipenv run python3 ./merge.py
cd -
