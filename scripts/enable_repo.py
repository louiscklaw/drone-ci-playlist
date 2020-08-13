#!/usr/bin/env python3

import os,sys
from pprint import pprint

from subprocess import check_output
import shlex

# curl -X POST "$DRONE_SERVER/api/repos/louiscklaw/3d-library" -H "Authorization: Bearer $DRONE_TOKEN"

DRONE_SERVER=os.environ['DRONE_SERVER']
DRONE_TOKEN=os.environ['DRONE_TOKEN']

def run(repo):
  command = 'curl -X POST "{}/api/repos/louiscklaw/{}" -H "Authorization: Bearer {}"'.format(DRONE_SERVER,repo, DRONE_TOKEN)

  check_output(shlex.split(command))


f_repo_list=open('scripts/repos_list.txt')
repo_list = map(lambda x: x.strip(), f_repo_list.readlines())

for repo in repo_list:
  run(repo)
