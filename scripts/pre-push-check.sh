#!/usr/bin/env bash

set -e

echo 'hello pre-push check'

cd /home/logic/_workspace/drone-ci-playlist
  mv .drone.yml .drone.yml.origional || true

  scripts/build_main_drone.sh

  HELLO=$(git status | grep -i "modified:   .drone.yml")
  if [[ -z $HELLO ]]; then
    echo "main .drone.yml is updated, passing..."
  else
    echo 'main .drone.yml is not update, escape !'
    rm -rf .drone.yml
    mv .drone.yml.origional .drone.yml || true
    cd -
    exit -1
  fi

cd -