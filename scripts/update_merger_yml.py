#!/usr/bin/env python
import os,sys
from pprint import pprint
from subprocess import Popen, check_output

from config import *

SCRIPTS_DIR=os.path.abspath(os.path.dirname(__file__))
PROJ_HOME = os.path.abspath(SCRIPTS_DIR+'/..')

def runCommand(command_in):
  return check_output(command_in).decode('utf-8')

def listDroneYmlDirs():
  # output = runCommand(['find','.','-maxdepth','1','-type','d']).split('\n')
  # output = directory_with_valid_drone_yml
  return directory_with_valid_drone_yml

def helloworld_merger_yml():
  print('helloworld_merger_yml')

def listAllProjects():
  proj_dirs = listDroneYmlDirs()
  proj_dirs = map(lambda x: x.replace('./',''), proj_dirs)
  proj_dirs = filter(lambda x: x not in SKIP_LIST, proj_dirs)
  return proj_dirs

def updateDependsOn(in_yml):
  in_yml = in_yml.replace('<depends_on>','\n'.join(map(lambda x: '  - {}'.format(x), listAllProjects())))
  return in_yml
