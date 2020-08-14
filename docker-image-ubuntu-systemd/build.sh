#!/usr/bin/env bash

set -ex

docker build . -t logickee/ubuntu-with-systemd

docker run -it logickee/ubuntu-with-systemd bash
