#!/usr/bin/env python
import os
import sys
import logging
import traceback
from pprint import pprint

from subprocess import check_output

GITHUB_TOKEN=os.environ['GITHUB_TOKEN']
DRONE_BRANCH=os.environ['DRONE_BRANCH']

merge_dest = {
  'test': 'develop',
  'develop': 'master'
}

def listBranch(path_to_check='.'):
  return check_output(['git','branch'], cwd=path_to_check).decode('utf-8').split('\n')

def getActiveBranch(path_to_check='.'):
  list_branch_result = listBranch(path_to_check)
  return list(filter(lambda x: x.find('* ') ==0, list_branch_result))[0].replace('* ','')

def git_merge(git_branch_to_merge, git_filepath='.'):
  try:
    result = check_output(['git', 'merge', '--ff-only',git_branch_to_merge], cwd=git_filepath)

  except Exception as e:
    print('error occur during git merge')
    raise e

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

def tryMerge(src_branch,dest_branch,git_filepath='.'):
  # test/xxxxx -> develop
  # src_branch = test/xxxxxx
  # dest_branch = test/xxxxxx

  try:
    checkoutBranch(dest_branch, git_filepath)
    git_merge(src_branch,git_filepath)

  except Exception as e:
    print('error occur during merge branch {} -> {}'.format(src_branch, dest_branch))

def lookupMergeDest(branch_name, path_to_check='.'):
  try:
    front_name = branch_name.split('/')[0]

    if front_name in merge_dest.keys():
      return merge_dest[front_name]
    else:
      raise 'error during lookup merge name'

  except Exception as e:
    print('error during lookup merge name "{}"'.format(front_name))
    raise e

def gitPush(path_to_push="."):
  result = check_output(['git','push'],cwd=path_to_push).decode('utf-8')
  return result

def gitClone(git_src_url, path_to_store='.'):
  result = check_output(['git','clone',git_src_url, path_to_store]).decode('utf-8')
  return result

def helloworld():
  print('helloworld')

def main():
  try:
    git_working_dir = sys.argv[1]
    print('working on {}'.format(git_working_dir))

    active_branch = getActiveBranch(git_working_dir)
    dest_branch = lookupMergeDest(active_branch, git_working_dir)
    tryMerge(active_branch, dest_branch, git_working_dir)
    gitPush(git_working_dir)

  except Exception as e:
    print('error during handling merger')
    sys.exit(99)

if __name__ == '__main__':
  main()
