#!/usr/bin/env sh

set -x

# id

# pwd

# cd

# pwd

# apt-get update
# apt-get install -y git
# apt-get install -y python3 python3-pip
apt-get install -y entr

# python3 -m pip install pipenv

# cd util
#   pipenv sync
# cd -

pipenv run python3 ./test/test.py
