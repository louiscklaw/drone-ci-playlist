#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint
from subprocess import Popen, check_output

from config import *
from update_merger_yml import *

drone_pipeline_seperator='''

---

'''

main_drone_yml_list = []

def getGitignoreContent():
  f_gitignore = open('.gitignore','r')
  return f_gitignore.readlines()

def runCommand(command_in):
  return check_output(command_in).decode('utf-8')

def listDirs():
  return runCommand(['find','.','-maxdepth','1','-type','d']).split('\n')

def listProjects():
  # all_dirs = runCommand(['ls','-1']).split('\n')
  all_dirs = listDirs()
  all_dirs = map(lambda x: x.replace('./',''), all_dirs)
  all_dirs = filter(lambda x: x not in ['.','.git','.cache','scripts','','node_modules','package.json','yarn.lock','hello-ubuntu','.local'], all_dirs)
  return all_dirs

def checkFileExist(filepath_to_check):
  return os.path.exists(filepath_to_check)


def openProjectDroneYml(filepath):
  return ''.join(open(filepath,'r').readlines())

def replacePipelineName(content_in, pipeline_name):
  # pprint(content_in)
  import re


  # content_in = content_in.split('\n')
  # print(list(map(lambda x: re.sub('name: hello-merger','name: 123',x), content_in)))
  # after_process = list(map(lambda x: re.sub('^name: [\w|\d|-]+$','name: '+pipeline_name,x), content_in))

  text_to_search = 'kind: pipeline\nname: [\d|\w|-]+\n'
  text_to_replace = 'kind: pipeline\nname: {}\n'.format(pipeline_name)

  m = re.search(text_to_search, content_in)

  if m is None:
    print('cannot find text to replace')
    raise 'cannot find text to replace'

  content_in = re.sub(text_to_search, text_to_replace, content_in)
  # print(content_in)
  # sys.exit()

  # pprint(output)
  # sys.exit()
  return content_in

def writeMainDroneYml(filepath, content):
  f_main_drone = open(filepath,'r+')
  f_main_drone.truncate(0)
  f_main_drone.writelines(content)
  f_main_drone.close()

def main():
  project_dirs = sorted(listProjects())
  project_dirs = list(filter(lambda x: x != 'hello-merger', project_dirs))+['hello-merger']

  for dirname in project_dirs:
    try:
      drone_file = dirname+'/'+'.drone.yml'
      pipeline_name = os.path.dirname(drone_file)

      drone_file_arm = dirname+'/'+'.drone.yml.arm'

      if checkFileExist(drone_file_arm):
        temp = ''

        if dirname == 'hello-merger':
          temp = updateDependsOn(
            replacePipelineName(openProjectDroneYml(drone_file), pipeline_name)
          )

        else:
          temp = replacePipelineName(openProjectDroneYml(drone_file), pipeline_name)

        drone_yml_content = '\n'.join([
          '# inserted by test {} start'.format(drone_file),
          temp,
          '# inserted by test {} end'.format(drone_file),
        ])

        main_drone_yml_list.append(drone_yml_content)

      if checkFileExist(drone_file):
        temp = ''

        if dirname == 'hello-merger':
          temp = updateDependsOn(
            replacePipelineName(openProjectDroneYml(drone_file), pipeline_name)
          )

        else:
          temp = replacePipelineName(openProjectDroneYml(drone_file), pipeline_name)

        drone_yml_content = '\n'.join([
          '# inserted by test {} start'.format(drone_file),
          temp,
          '# inserted by test {} end'.format(drone_file),
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
    raise e
    sys.exit(99)
    pass
