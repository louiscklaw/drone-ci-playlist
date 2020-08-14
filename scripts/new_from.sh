#!/usr/bin/env bash

set -x
rm -rf * .*

TEST=`echo $PWD|rev |cut -d'/' -f1 |rev`
git branch -D poc/$TEST
git checkout -b poc/$TEST

set -ex

rsync -avz --exclude 'node_modules' ../$1/ .
