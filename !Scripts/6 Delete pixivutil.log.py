# -*- coding: utf-8 -*-
from pathlib import Path
import os

print('Warning this will permanently delete the log file(s)\n')

os.system('pause')
print()

for path in Path('..').rglob('pixivutil.log*'):
    try:
        os.remove(path)
        print(f'Deleted {path}')
    except FileNotFoundError:
        print(f'File not found {path}\n')
print('Done!')
os.system('pause')
