# -*- coding: utf-8 -*-
from pathlib import Path
import os
import sys
sys.path.append('../PixivUtil2')
import PixivHelper
import PixivConfig

config = PixivConfig.PixivConfig()
PixivHelper.set_config(config)

print('''THIS HAS BEEN IMPLEMENTED IN PIXIVUTIL2
You can use this or use the built in one
''')

config.rootDirectory = input('Enter Pixiv directory: ')

for path in Path(config.rootDirectory).rglob('*.ugoira'):
    ugo_name = str(path)
    webm_filename = f'{ugo_name[:-7]}.{config.ffmpegExt}'

    PixivHelper.convert_ugoira(ugo_name,
                               webm_filename,
                               ffmpeg=config.ffmpeg,
                               codec=config.ffmpegCodec,
                               param=config.ffmpegParam,
                               extension=config.ffmpegExt,
                               image=None)

    ts = os.path.getmtime(ugo_name)
    os.utime(webm_filename, (ts, ts))
print('Done!')
os.system('pause')
