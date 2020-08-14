#!/usr/bin/env bash

set -ex

echo 'hello pre-push check'

cd /home/logic/_workspace/drone-ci-playlist
  mv .drone.yml .drone.yml.origional

  scripts/build_main_drone.sh

  HELLO=$(git status | grep -i "modified:   ./.drone.yml")
  if [[ -z "$HELLO"]]; then
    echo "main .drone.yml is updated, passing..."
  else
    echo 'main .drone.yml is not update, escape !'
    cd -
    exit -1
  fi

cd -