#!/usr/bin/env python3

import os,sys
from pprint import pprint
from subprocess import run, check_output
from subprocess import PIPE
import shlex

SKIP_LIST=[
  '.',
  '.cache',
  '.git',
  '.local',
  '.ssh',
  '',
  'drone-python-helloworld',
  'hello-merger',
  'hello-ubuntu',
  'node_modules',
  'scripts',
  'x86-runner-setup',
  'check-leak',
  '.config',
  '.npm'
  ]


directory_with_valid_drone_yml=check_output(shlex.split('find . -maxdepth 2')).decode('utf-8').split('\n')
directory_with_valid_drone_yml=list(filter(lambda x: x.find('.drone.yml') != -1, directory_with_valid_drone_yml))
directory_with_valid_drone_yml=list(filter(lambda x: x.find('disable') == -1, directory_with_valid_drone_yml))
directory_with_valid_drone_yml=list(filter(lambda x: x.find('./.drone.yml') == -1, directory_with_valid_drone_yml))
directory_with_valid_drone_yml=list(map(lambda x: x.replace('/.drone.yml',''), directory_with_valid_drone_yml))
directory_with_valid_drone_yml = sorted(directory_with_valid_drone_yml)
# pprint(directory_with_valid_drone_yml)