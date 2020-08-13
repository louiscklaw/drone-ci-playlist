#!/usr/bin/env python3

import os, sys
from pprint import pprint

import unittest

from main import *

class TestStringMethods(unittest.TestCase):

  def test_leak_not_found(self):
    checkLeak('bbb',os.path.abspath(os.getcwd())+'/leak_doc.txt')

  def test_leak_found(self):
    with self.assertRaises(TypeError):
      checkLeak('aaa',os.path.abspath(os.getcwd())+'/leak_doc.txt')



if __name__ == '__main__':
  unittest.main()
