# -*- coding: utf-8 -*-
import Scripts_config
import shutil
import os

config = Scripts_config.Load()

FanboxCopy = int(config['Settings']['FanboxCopy'])
PixivCopy = int(config['Settings']['PixivCopy'])

ProblematicID = config['Settings']['ProblematicID']
ProblematicID = ProblematicID.split(',')
ProblematicID = [_.strip() for _ in ProblematicID]
ProblematicID = list(filter(None, ProblematicID))

os.makedirs(r'../PixivUtil2', exist_ok=True)
shutil.copy(r'./config.ini', r'../PixivUtil2')

print('Copied config.ini to /PixivUtil2\n')

if len(ProblematicID) > 0:
    shutil.copytree(r'../PixivUtil2',
                    r'../PixivUtil2 - Problematic', dirs_exist_ok=True)

print('Copied /PixivUtil2 to /PixivUtil2 - Problematic\n')
print('Making copies of /PixivUtil2 - Fanbox\n')

for i in range(FanboxCopy):
    if i == 0:
        shutil.copytree(r'../PixivUtil2',
                        r'../PixivUtil2 - Fanbox', dirs_exist_ok=True)
    elif i == 1:
        shutil.copytree(r'../PixivUtil2',
                        r'../PixivUtil2 - Fanbox - Copy', dirs_exist_ok=True)
    else:
        shutil.copytree(r'../PixivUtil2',
                        fr'../PixivUtil2 - Fanbox - Copy ({i})', dirs_exist_ok=True)

print('Making copies of /PixivUtil2 - Copy\n')

for i in range(1, (PixivCopy + 1)):
    if i == 1:
        shutil.copytree(r'../PixivUtil2',
                        r'../PixivUtil2 - Copy', dirs_exist_ok=True)
    else:
        shutil.copytree(r'../PixivUtil2',
                        fr'../PixivUtil2 - Copy ({i})', dirs_exist_ok=True)
