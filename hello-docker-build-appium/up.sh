#!/usr/bin/env bash

set -ex

docker run -it --env-file .env.docker -v $PWD:/root -v /var/run/docker.sock:/var/run/docker.sock --rm logickee/ubuntu-docker bash
