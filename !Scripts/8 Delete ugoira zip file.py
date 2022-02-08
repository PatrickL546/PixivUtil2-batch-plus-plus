# -*- coding: utf-8 -*-

import os
from pathlib import Path
import sys

print('Warning this will permanently delete the file(s)\n')

rootDirectory=input('Enter directory (includes subdirectory):')

for path in Path(rootDirectory).rglob('*.ugoira'):
    ugo_name=str(path)
    zipfile_name = ugo_name[:-7] + '.zip'
    os.remove(zipfile_name)
    print(f'Deleted {zipfile_name}')

print('Done! \n')
os.system('pause')
sys.exit()