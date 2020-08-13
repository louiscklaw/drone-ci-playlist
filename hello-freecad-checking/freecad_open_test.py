#!/usr/bin/env python3

import sys, os
from pprint import pprint

USER_HOME_DIR = os.getenv('HOME')
print('USER_HOME_DIR', USER_HOME_DIR)

freecad_paths = [
  '{}/.FreeCAD/Mod/ExplodedAssembly'.format(USER_HOME_DIR),
  '{}/.FreeCAD/Mod/Glass'.format(USER_HOME_DIR),
  '{}/.FreeCAD/Mod/Render'.format(USER_HOME_DIR),
  '{}/.FreeCAD/Mod/kicadStepUpMod'.format(USER_HOME_DIR),
  '{}/.FreeCAD/Mod/fasteners'.format(USER_HOME_DIR),
  '{}/.FreeCAD/Mod/Assembly4'.format(USER_HOME_DIR),
  '/usr/share/freecad/Mod/Inspection',
  '/usr/share/freecad/Mod/Fem',
  '/usr/share/freecad/Mod/Test',
  '/usr/share/freecad/Mod/Measure',
  '/usr/share/freecad/Mod/MeshPart',
  '/usr/share/freecad/Mod/Spreadsheet',
  '/usr/share/freecad/Mod/Ship',
  '/usr/share/freecad/Mod/Points',
  '/usr/share/freecad/Mod/Raytracing',
  '/usr/share/freecad/Mod/Path',
  '/usr/share/freecad/Mod/PartDesign',
  '/usr/share/freecad/Mod/Arch',
  '/usr/share/freecad/Mod/Drawing',
  '/usr/share/freecad/Mod/Start',
  '/usr/share/freecad/Mod/TechDraw',
  '/usr/share/freecad/Mod/Complete',
  '/usr/share/freecad/Mod/AddonManager',
  '/usr/share/freecad/Mod/Import',
  '/usr/share/freecad/Mod/Surface',
  '/usr/share/freecad/Mod/Plot',
  '/usr/share/freecad/Mod/Show',
  '/usr/share/freecad/Mod/Draft',
  '/usr/share/freecad/Mod/Image',
  '/usr/share/freecad/Mod/Robot',
  '/usr/share/freecad/Mod/Idf',
  '/usr/share/freecad/Mod/Web',
  '/usr/share/freecad/Mod/Tux',
  '/usr/share/freecad/Mod/Material',
  '/usr/share/freecad/Mod/Mesh',
  '/usr/share/freecad/Mod/OpenSCAD',
  '/usr/share/freecad/Mod/Sketcher',
  '/usr/share/freecad/Mod/ReverseEngineering',
  '/usr/share/freecad/Mod/Part',
  '/usr/share/freecad/Mod',
  '/usr/lib/freecad/lib64',
  '/usr/lib/freecad-python3/lib',
  '/usr/share/freecad/Ext',
  '',
  '/usr/lib/python36.zip',
  '/usr/lib/python3.6',
  '/usr/lib/python3.6/lib-dynload',
  '{}/.local/lib/python3.6/site-packages'.format(USER_HOME_DIR),
  '/usr/local/lib/python3.6/dist-packages',
  '/usr/lib/python3/dist-packages',
  '{}/.FreeCAD/Macro'.format(USER_HOME_DIR),
  '/usr/lib/freecad/Macro'
]

for freecad_path in freecad_paths:
  sys.path.append(freecad_path)

import FreeCAD as App
import Import

freecad_file_to_test = sys.argv[1]
freecad_document_name = os.path.basename(freecad_file_to_test).split('.')[0]
print('testing freecad file {}'.format(freecad_file_to_test))


# filename = '{}/_workspace/freecad-playlist/common_parts.FCStd'.format(USER_HOME_DIR)
App.open(freecad_file_to_test)
App.setActiveDocument(freecad_document_name.replace('-','_'))
App.ActiveDocument.recompute()
App.setActiveDocument("")
App.ActiveDocument=None

print('done')