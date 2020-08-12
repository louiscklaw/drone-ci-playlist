#!/usr/bin/env bash

set -ex

export DRONE_BRANCH=test/helloworld-rpi

rm -rf /tmp/test_git_dir

git clone https://$GITHUB_TOKEN@github.com/louiscklaw/drone-ci-playlist.git /tmp/test_git_dir

cd /tmp/test_git_dir
  git checkout $DRONE_BRANCH
cd -

cd hello-merger
  pipenv run python3 ./src/main.py /tmp/test_git_dir
cd -



# cd /tmp/test_git_dir

#   git remote set-url origin https://$GITHUB_TOKEN@github.com/louiscklaw/drone-ci-playlist.git

#   git push
