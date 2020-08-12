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
  # all_dirs = runCommand(['ls','-1']).split('\n')
  all_dirs = runCommand(['find','.','-type','d','-maxdepth','1']).split('\n')
  all_dirs = map(lambda x: x.replace('./',''), all_dirs)
  all_dirs = filter(lambda x: x not in ['.','.git','.cache','scripts','','node_modules','package.json','yarn.lock','hello-ubuntu','.local'], all_dirs)
  return all_dirs

def checkFileExist(filepath_to_check):
  return os.path.exists(filepath_to_check)


def openProjectDroneYml(filepath):
  return ''.join(open(filepath,'r').readlines())

def writeMainDroneYml(filepath, content):
  f_main_drone = open(filepath,'r+')
  f_main_drone.truncate(0)
  f_main_drone.writelines(content)
  f_main_drone.close()

def main():
  project_dirs = listProjects()

  for dirname in project_dirs:
    try:
      drone_file = dirname+'/'+'.drone.yml'

      if checkFileExist(drone_file):

        drone_yml_content = '\n'.join([
          '# inserted by test {} start'.format(drone_file),
          openProjectDroneYml(drone_file),
          '# inserted by test {} end'.format(drone_file)
        ])

        main_drone_yml_list.append(drone_yml_content)

      # else:
      #   raise 'wanted drone file not exist'

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
