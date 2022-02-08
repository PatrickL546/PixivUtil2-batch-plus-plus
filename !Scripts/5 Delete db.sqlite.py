import os
from pathlib import Path
import sys

print('Warning this will permanently delete the file(s)\n')

input('Press Enter to continue\n')

for path in Path('..').rglob('db.sqlite'):
    os.remove(path)
    print(f'Deleted {path}')

print('Done! \n')
os.system('pause')
sys.exit()