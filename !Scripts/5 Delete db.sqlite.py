# -*- coding: utf-8 -*-
from pathlib import Path
import os

print('Warning this will permanently delete the db file(s)\n')

os.system('pause')
print()

for path in Path('..').rglob('db.sqlite'):
    try:
        os.remove(path)
        print(f'Deleted {path}')
    except FileNotFoundError:
        print(f'File not found {path}\n')
print('Done!')
os.system('pause')
