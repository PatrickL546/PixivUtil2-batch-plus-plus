# -*- coding: utf-8 -*-
from pathlib import Path
import Scripts_config
import subprocess
import os

config = Scripts_config.Load()

os.system('color')


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


FanboxArg = config['Settings']['FanboxArg']
FanboxArg = FanboxArg.split(", ")

PixivArg = config['Settings']['PixivArg']
PixivArg = PixivArg.split(", ")

ProblematicID = config['Settings']['ProblematicID']
ProblematicID = ProblematicID.split(',')
ProblematicID = [_.strip() for _ in ProblematicID]
ProblematicID = list(filter(None, ProblematicID))

print(f'''{bcolors.FAIL}#####DO NOT CLOSE#####{bcolors.ENDC}

This will close automatically when all instances has been launched
''')

if len(ProblematicID) > 0:
    argsFanbox = ['python.exe', r'../PixivUtil2 - Problematic/PixivUtil2.py']
    argsPixiv = ['python.exe', r'../PixivUtil2 - Problematic/PixivUtil2.py']

    argsFanbox.extend(FanboxArg)
    argsPixiv.extend(PixivArg)

    subprocess.run(argsFanbox, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=r'../PixivUtil2 - Problematic')
    subprocess.run(argsPixiv, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=r'../PixivUtil2 - Problematic')

fanboxPath = Path('..').glob('PixivUtil2 - Fanbox*')
pixivPath = Path('..').glob('PixivUtil2 - Copy*')

for path in fanboxPath:
    argsFanbox = ['python.exe', fr'{path}/PixivUtil2.py']
    argsFanbox.extend(FanboxArg)
    subprocess.Popen(argsFanbox, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=fr'{path}')

for path in pixivPath:
    argsPixiv = ['python.exe', fr'{path}/PixivUtil2.py']
    argsPixiv.extend(PixivArg)
    subprocess.Popen(argsPixiv, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=fr'{path}')
