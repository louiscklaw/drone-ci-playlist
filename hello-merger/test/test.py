#!/usr/bin/env python

import os
import sys
import logging
import traceback
from pprint import pprint



TEST_DIR = os.path.dirname(__file__)
PROJ_HOME = os.path.join(TEST_DIR,'..')
SRC_DIR = os.path.join(PROJ_HOME,'src')

sys.path.append(SRC_DIR)

from main import *

def test_get_active_branch():
  print(getActiveBranch('.'))

def test_checkout_branch():
  checkoutMaster()

def test_helloworld():
  helloworld()

if __name__ == '__main__':
    test_helloworld()
    test_get_active_branch()
    test_checkout_branch()