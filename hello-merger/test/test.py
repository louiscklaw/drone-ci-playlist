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

def test_helloworld():
  helloworld()

if __name__ == '__main__':
    test_helloworld()
    test_get_active_branch()
    test_checkout_branch()
