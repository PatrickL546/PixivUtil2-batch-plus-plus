# -*- coding: utf-8 -*-
from pathlib import Path
import os

print('Warning this will permanently delete the zip file(s)\n')

pixivDirectory = input('Enter Pixiv directory: ')
print()

for path in Path(pixivDirectory).rglob('*.ugoira'):
    ugo_name = str(path)
    zipfile_name = f'{ugo_name[:-7]}.zip'
    try:
        os.remove(zipfile_name)
        print(f'Deleted {zipfile_name}')
    except FileNotFoundError:
        print(f'File not found {zipfile_name}\n')
print('Done!')
os.system('pause')
