# -*- coding: utf-8 -*-

import os
from pathlib import Path
import sys
sys.path.insert(1, '..\PixivUtil2')
import PixivHelper
import PixivConfig

config=PixivConfig.PixivConfig()

PixivHelper.set_config(config)

config.rootDirectory=input('Enter directory (includes subdirectory):')

for path in Path(config.rootDirectory).rglob('*.ugoira'):
    ugo_name=str(path)
    webm_filename = ugo_name[:-7] + '.' + config.ffmpegExt

    PixivHelper.convert_ugoira(ugo_name,
                               webm_filename,
                               ffmpeg=config.ffmpeg,
                               codec=config.ffmpegCodec,
                               param=config.ffmpegParam,
                               extension=config.ffmpegExt,
                               image=None)

    ts = os.path.getmtime(ugo_name)
    os.utime(webm_filename, (ts, ts))

print('Done! \n')
os.system('pause')
sys.exit()