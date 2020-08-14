#!/usr/bin/env bash

set -ex

cd travis-build-docker-image
  docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD
  docker push logickee/drone-docker-builder
  docker logout
cd ..

# done
