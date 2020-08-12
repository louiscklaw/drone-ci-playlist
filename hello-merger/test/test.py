#!/usr/bin/env python

import os
import sys
import logging
import traceback
from pprint import pprint


from subprocess import check_output

TEST_DIR = os.path.dirname(__file__)
PROJ_HOME = os.path.join(TEST_DIR,'..')
SRC_DIR = os.path.join(PROJ_HOME,'src')

sys.path.append(SRC_DIR)

from main import *

PATH_TO_HANDLE = sys.argv[1]

def check_file_content():
  return check_output(['cat','/tmp/test_git_dir/test_file.txt'], cwd=PATH_TO_HANDLE).decode('utf-8').strip()

def test_get_active_branch():
  print(getActiveBranch(PATH_TO_HANDLE))

def test_checkout_master():
  checkoutMaster(PATH_TO_HANDLE)
  result = check_output(['cat','/tmp/test_git_dir/test_file.txt'], cwd=PATH_TO_HANDLE).decode('utf-8')

  assert result.strip() == 'content_master'

def test_checkout_develop():
  checkoutDevelop(PATH_TO_HANDLE)
  result = check_output(['cat','/tmp/test_git_dir/test_file.txt'], cwd=PATH_TO_HANDLE).decode('utf-8')

  assert result.strip() == 'content_develop'

def test_checkout_branch():
  test_checkout_master()
  test_checkout_develop()

def test_merger_test_to_develop():
  tryMerge('test/test_adding_content','develop',PATH_TO_HANDLE)
  assert check_file_content() == 'content_test_adding_content'


def test_merger_develop_to_master():
  tryMerge('develop','master',PATH_TO_HANDLE)
  assert check_file_content() == 'content_test_adding_content'

def test_lookup_merge_dest():
  assert lookupMergeDest('test/blabla',PATH_TO_HANDLE)=='develop'
  assert lookupMergeDest('develop',PATH_TO_HANDLE)=='master'

  # merge lookup failure
  try:
    lookupMergeDest('blablabla',PATH_TO_HANDLE)

  except Exception as e:
    assert e.args == ('exceptions must derive from BaseException',)

def test_git_push():
  try:
    gitPush(PATH_TO_HANDLE)

  except Exception as e:
    assert e.args == ('exceptions must derive from BaseException',)
    pass

def test_git_clone():
  gitClone('git@github.com:louiscklaw/test-git-repo.git','/tmp/test-git-repo-helloworld')

def test_helloworld():
  helloworld()

if __name__ == '__main__':
  test_helloworld()
  test_get_active_branch()
  test_checkout_branch()
  test_merger_test_to_develop()
  test_merger_develop_to_master()
  test_lookup_merge_dest()
  # test_git_push()
  test_git_clone()