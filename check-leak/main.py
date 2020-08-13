#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint

from subprocess import run
from subprocess import PIPE
import shlex

# https://stackoverflow.com/questions/53209127/subprocess-unexpected-keyword-argument-capture-output/53209196
# command = shlex.split('grep -ri helloworld .')
# result = run(command, stdout=PIPE, stderr=PIPE)
# pprint(result.stdout)
# sys.exit(99)

CWD = os.getcwd()
SCAN_DIR = CWD if len(sys.argv) < 2 else sys.argv[1]

SKIP_LIST=[
  'logickee','1'
]

DIR_SKIP_LIST=[
  '.env'
]

print('SCAN_DIR:"{}"'.format(SCAN_DIR))

def checkLeak(should_not_appear, filepath_to_check):
  command = shlex.split('grep -ri "{}" {}'.format(should_not_appear, filepath_to_check))

  # print(' '.join(command))
  result = run(command, stdout=PIPE, stderr=PIPE)

  terms_found = result.stdout != b''

  if terms_found:
    print('command: ',' '.join(command))
    # print('{}:{}, {}, {}'.format(word, result.returncode, result.stdout, result.args))

    print()
    print( 'error files: {}'.format( result.stdout.decode('utf-8').strip()) )
    print()

    raise 'leakage found'

def readCredentialFile(filepath):
  file_content = open(filepath,'r').readlines()
  file_content = filter(lambda x: x.strip(), file_content)
  file_content = filter(lambda x: x[0] != '#', file_content)

  return set(file_content)

def parseCredentialFile():
  try:
    filepath='/home/logic/.credentials.rc'
    if os.path.exists(filepath):

      content = readCredentialFile(filepath)
      content = map(lambda x: x.strip(), content)
      return map(lambda x: x.replace('export ',''), content)
    else:
      raise 'filepath not found'
  except Exception as e:
    raise e

def clearBashValue(txt_value_in):
  output = txt_value_in

  if output[0]=="'":
    output = output[1:]

  if output[-1]=="'":
    output = output [:-1]

  if output[0]=='"':
    output = output[1:]

  if output[-1]=='"':
    output = output [:-1]

  return output


def credentialValue():
  temp1 = parseCredentialFile()
  temp2 = map(lambda x: x.split('=')[1:][0], temp1)
  temp3 = map(lambda x: clearBashValue(x), temp2)
  return temp3

def printBanner(text, text1):
  print('\n'*1)
  print('V'*76)
  print()
  print(' '* 16, text)
  print(' '* 16, text1)
  print()
  print('^'*76)
  print('\n'*1)


def main():
    printBanner('scanning for sensitive words', SCAN_DIR)
    should_not_appear = list(credentialValue())

    print('num of sensitive word {}'.format(len(should_not_appear)))
    print('scan start')
    for word in should_not_appear:
      if word not in SKIP_LIST:
        try:
          checkLeak(word, SCAN_DIR)
        except Exception as e:
          print('sensitive word found')
          raise e

    print('scan done')

if __name__ == '__main__':
  main()
