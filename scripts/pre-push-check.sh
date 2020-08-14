#!/usr/bin/env bash

echo 'linting drone.yml files'
drone fmt /home/logic/_workspace/drone-ci-playlist/hello-docker-build/.drone.yml

echo 'hello pre-push check'

cd /home/logic/_workspace/drone-ci-playlist
  mv .drone.yml .drone.yml.origional || true

  scripts/build_main_drone.sh

  HELLO=$(git status | grep -i "modified:   .drone.yml")

  rm -rf .drone.yml
  mv .drone.yml.origional .drone.yml || true

  if [[ -z $HELLO ]]; then
    echo ""
    echo "main .drone.yml is updated, passing..."
    echo ""
  else
    echo ""
    echo ' !!! main .drone.yml is not update, escape !!! '
    echo ""
    cd -
    exit -1
  fi

cd -