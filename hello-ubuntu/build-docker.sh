#!/usr/bin/env bash

set -ex


docker build -t logickee/ubuntu-basic .

docker push logickee/ubuntu-basic
