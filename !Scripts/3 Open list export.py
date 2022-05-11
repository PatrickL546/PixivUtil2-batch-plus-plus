# -*- coding: utf-8 -*-
from pathlib import Path
import os

for list in Path('..').rglob('list*'):
    os.startfile(list)
