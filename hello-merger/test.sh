#!/usr/bin/env sh

set -x

# id

# pwd

# cd

# pwd

# sudo apt-get update
# sudo apt-get install -y git
# sudo apt-get install -y python3 python3-pip
# sudo apt-get install -y entr rsync
# python3 -m pip install pipenv

# cd util
#   pipenv sync
# cd -

rsync -avzh /root/hello-merger/ /tmp/hello-merger

rm -rf /tmp/test_git_dir

cd /tmp
  mkdir -p test_git_dir
  cd test_git_dir
    git init

    git config --global user.email "drone_test@louislabs.com"
    git config --global user.name "drone_test"

    git checkout -b master
    echo content_master > test_file.txt
    git add test_file.txt
    git commit test_file.txt -m"init commit to master,"

    git checkout -b develop
    echo content_develop > test_file.txt
    git add test_file.txt
    git commit test_file.txt -m"init commit to develop,"

    git checkout -b test/test_adding_content
    echo content_test_adding_content > test_file.txt
    git add test_file.txt
    git commit test_file.txt -m"init commit to test_adding_content,"

    git branch

  cd ..

pwd

cd hello-merger
  pipenv run python3 ./test/test.py /tmp/test_git_dir
  # pipenv run python3 ./src/main.py /tmp/test_git_dir
cd ..
