#!/usr/bin/env bash

set -ex


cd hello-hugo
  dpkg -i ./hugo_extended_0.74.3_Linux-64bit.deb

  cd hugo-helloworld
    hugo -D
  cd ..
cd ..
