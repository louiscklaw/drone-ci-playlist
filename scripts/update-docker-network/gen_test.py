#!/usr/bin/env python3

import os,sys
from pprint import pprint

i = 0
wanted = 256

while i < wanted:
  for j in range(0,16):
    print('docker network create your-network{} &'.format(i))
    i+=1
    if i > wanted:
      break
  print('wait')
