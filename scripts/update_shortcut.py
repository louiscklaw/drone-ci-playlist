import os,sys
import subprocess
import shlex
import re
from pprint import pprint

ENV_FILE_TO_UPDATE=sys.argv[1]

new_command_template='''
new_from_##PROJ_NAME##(){
  new_from ##PROJ_DIR_NAME##
  pipenv run python3 main.py
  ./run.sh
}
'''

def simple_replace(x):
  output = re.sub( '##PROJ_NAME##', x.replace('-','_'), new_command_template,
    flags=re.MULTILINE)

  output = re.sub( '##PROJ_DIR_NAME##', x, output,
    flags=re.MULTILINE)

  return output

dirs = subprocess.check_output(shlex.split('ls -1')).decode('utf-8').split('\n')
tryout_dirs = list(filter(lambda x: x.find('-tryout') > 0, dirs))

new_commands_content = map( lambda x: simple_replace(x), tryout_dirs)

start_string = '''
# update_by_dir_start
# source script: {}
'''.format(os.path.abspath(__file__)).strip()

end_string = '# update_by_dir_end'

new_commands_content=list(new_commands_content)+[
  '''testing_shortcut(){
  echo testing_shortcut
}
'''
]

new_commands_string='\n'.join(
  [start_string]+list(new_commands_content)+[end_string]
  )


temp = ''
with open(ENV_FILE_TO_UPDATE,'r') as fi:
  temp = ''.join(fi.readlines())
  temp = re.sub(r'# update_by_dir_start.+?# update_by_dir_end',
    new_commands_string,
    temp, count=1,flags=re.MULTILINE|re.DOTALL)

with open(ENV_FILE_TO_UPDATE,'w') as fo:
  fo.writelines(temp)
