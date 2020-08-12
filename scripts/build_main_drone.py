#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint
from subprocess import Popen, check_output

drone_pipeline_seperator='''
---
'''

main_drone_yml_list = []

def getGitignoreContent():
  f_gitignore = open('.gitignore','r')
  return f_gitignore.readlines()

def runCommand(command_in):
  return check_output(command_in).decode('utf-8')

def listProjects():
  all_dirs = runCommand(['ls','-1']).split('\n')
  return filter(lambda x: x not in ['scripts','','node_modules','package.json','yarn.lock'], all_dirs)

def checkFileExist(filepath_to_check):
  return os.path.exists(filepath_to_check)


def openProjectDroneYml(filepath):
  return ''.join(open(filepath,'r').readlines())

def writeMainDroneYml(filepath, content):
  f_main_drone = open(filepath,'w')
  f_main_drone.writelines(content)
  f_main_drone.close()

def main():
  project_dirs = listProjects()

  for dirname in project_dirs:
    try:
      drone_file = dirname+'/'+'.drone.yml'


      if not checkFileExist(drone_file):
        raise 'findme'

      drone_yml_content = openProjectDroneYml(drone_file)

      main_drone_yml_list.append(drone_yml_content)

    except Exception as e:
      print('drone file not found: "{}"'.format(drone_file))
      print('error processing project dirs: "{}"'.format(dirname))
      raise e

  writeMainDroneYml('.drone.yml',drone_pipeline_seperator.join(main_drone_yml_list))

def helloworld():
    print('helloworld')


if __name__ == '__main__':
  try:
    main()
    pass
  except Exception as e:
    sys.exit(99)
    pass
