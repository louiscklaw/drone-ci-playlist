#!/usr/bin/env python
import os
import sys
import logging
import traceback
from pprint import pprint

from subprocess import check_output

def listBranch(path_to_check='.'):
  return check_output(['git','branch'], cwd=path_to_check).decode('utf-8').split('\n')

def getActiveBranch(path_to_check='.'):
  list_branch_result = listBranch(path_to_check)
  return list(filter(lambda x: x.find('* ') ==0, list_branch_result))[0].replace('* ','')

def checkoutBranch(branch_name_to_checkout, path_to_checkout="."):
  try:
    command_result = check_output(['git','checkout',branch_name_to_checkout], cwd=path_to_checkout)
    return command_result
  except Exception as e:
    pprint(command_result)
    raise e

def checkoutDevelop(path_to_checkout="."):
  try:
    command_result= checkoutBranch('develop',path_to_checkout)

  except Exception as e:
    pprint(command_result)
    raise e


def checkoutMaster(path_to_checkout="."):
  try:
    command_result= checkoutBranch('master',path_to_checkout)

  except Exception as e:
    pprint(command_result)
    raise e


def helloworld():
    print('helloworld')

if __name__ == '__main__':
    helloworld()