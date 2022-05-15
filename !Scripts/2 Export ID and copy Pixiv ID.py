# -*- coding: utf-8 -*-
from datetime import datetime
from functools import cache
import Scripts_config
import subprocess
import shutil
import math
import sys
import os

config = Scripts_config.Load()

FanboxCopy = int(config['Settings']['FanboxCopy'])
PixivCopy = int(config['Settings']['PixivCopy'])

PixivExportArg = config['Settings']['PixivExportArg']
PixivExportArg = PixivExportArg.split(", ")

Scrub = config.getboolean('Settings', 'Scrub')
DateFormat = config['Settings']['DateFormat']

BlacklistID = config['Settings']['BlacklistID']
BlacklistID = BlacklistID.split(',')
BlacklistID = [_.strip() for _ in BlacklistID]
BlacklistID = list(filter(None, BlacklistID))

ProblematicID = config['Settings']['ProblematicID']
ProblematicID = ProblematicID.split(',')
ProblematicID = [_.strip() for _ in ProblematicID]
ProblematicID = list(filter(None, ProblematicID))

os.system('color')


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


selected = ''
while not (selected == 'Q' or selected == 'q'):

    print(f'''-----------------MENU-----------------

{bcolors.WARNING}Enter [C] To continue{bcolors.ENDC}

Enter [1] Export online followed artist

Enter [2] Remove blacklisted ID

Press [3] Archive Pixiv ID

{bcolors.FAIL}Enter [Q] to Quit{bcolors.ENDC}
''')

    selected = input(': ')

    if (selected == 'C' or selected == 'c'):
        os.system('cls')
        print(f'{bcolors.OKGREEN}You selected option {selected}{bcolors.ENDC}\n')
        break
    elif selected == '1':
        os.system('cls')
        print(f'{bcolors.OKGREEN}You selected option {selected}{bcolors.ENDC}\n')

        args = ['python.exe', r'../PixivUtil2/PixivUtil2.py']
        args.extend(PixivExportArg)

        subprocess.run(args, creationflags=subprocess.CREATE_NEW_CONSOLE)
        if Scrub:
            with open(r'./2 Pixiv ID.txt') as f:
                pixivIDContent = f.read().splitlines()
                pixivIDContent = [_ for _ in pixivIDContent if '#' not in _]

            with open(r'./2 Pixiv ID.txt', 'w') as f:
                for id in pixivIDContent:
                    f.write(f'{id}\n')

    elif selected == '2':
        os.system('cls')
        print(f'{bcolors.OKGREEN}You selected option {selected}{bcolors.ENDC}\n')

        with open(r'./2 Pixiv ID.txt') as f:
            pixivIDContent = f.read().splitlines()
            pixivIDContent = [_ for _ in pixivIDContent if _ not in BlacklistID]

        with open(r'./2 Pixiv ID.txt', 'w') as f:
            for id in pixivIDContent:
                f.write(f'{id}\n')

    elif selected == '3':
        os.system('cls')
        print(f'{bcolors.OKGREEN}You selected option {selected}{bcolors.ENDC}\n')

        os.makedirs(r'./Export Archive', exist_ok=True)

        time = datetime.today()
        time = time.strftime(DateFormat)

        try:
            shutil.copy(r'./2 Pixiv ID.txt', fr'./Export Archive/PixivIDArchive_{time}.txt')
        except Exception:
            print('Failed to archive\n')

    elif (selected == 'Q' or selected == 'q'):
        sys.exit()
    else:
        os.system('cls')
        print(f'{bcolors.WARNING}Please select a valid option{bcolors.ENDC}\n')

    config = Scripts_config.Load()


# Remove Problematic ID from '2 Pixiv ID.txt'
if len(ProblematicID) > 0:
    with open(r'./2 Pixiv ID.txt') as f:
        pixivIDContent = f.read().splitlines()
        pixivIDContent = [_ for _ in pixivIDContent if _ not in ProblematicID]

    with open(r'./2 Pixiv ID.txt', 'w') as f:
        for id in pixivIDContent:
            f.write(f'{id}\n')

    # Copies Problematic ID to '/PixivUtil2 - Problematic'
    with open(r'../PixivUtil2 - Problematic/list.txt', 'w') as f:
        for id in ProblematicID:
            f.write(f'{id}\n')

    with open(r'../PixivUtil2 - Problematic/listfanbox.txt', 'w') as f:
        for id in ProblematicID:
            f.write(f'{id}\n')


@cache
def GetPixivIDSplitLines():
    with open(r'./2 Pixiv ID.txt') as f:
        idList = f.read().splitlines()
    return idList


def WriteCopyPixivID(path, index, indexEnd):
    if not os.path.exists(os.path.dirname(path)):
        os.mkdir(os.path.dirname(path))
    with open(path, 'w') as f:
        idList = GetPixivIDSplitLines()[index:indexEnd]
        for id in idList:
            f.write(f'{id}\n')


lineCountPixivID = sum(1 for line in open(r'./2 Pixiv ID.txt'))

# Divides Pixiv ID list to diffeerent instance(s)
# Fanbox Instances
if FanboxCopy > 0:
    fanboxIncrement = math.ceil(lineCountPixivID / FanboxCopy)

    for i in range(FanboxCopy):
        if i == 0:
            index = 0
            indexEnd = fanboxIncrement
            WriteCopyPixivID(r'../PixivUtil2 - Fanbox/listfanbox.txt', index, indexEnd)
        elif i == 1:
            index = fanboxIncrement
            indexEnd = (fanboxIncrement * 2)
            WriteCopyPixivID(r'../PixivUtil2 - Fanbox - Copy/listfanbox.txt', index, indexEnd)
        else:
            index = (fanboxIncrement * i)
            indexEnd = (fanboxIncrement * (i + 1))
            WriteCopyPixivID(fr'../PixivUtil2 - Fanbox - Copy ({i})/listfanbox.txt', index, indexEnd)

# Pixiv Instances
if PixivCopy > 0:
    pixivIncrement = math.ceil(lineCountPixivID / PixivCopy)

    for i in range(PixivCopy):
        if i == 0:
            index = 0
            indexEnd = pixivIncrement
            WriteCopyPixivID(r'../PixivUtil2 - Copy/list.txt', index, indexEnd)
        elif i == 1:
            index = pixivIncrement
            indexEnd = (pixivIncrement * 2)
            WriteCopyPixivID(fr'../PixivUtil2 - Copy ({(i+1)})/list.txt', index, indexEnd)
        else:
            index = (pixivIncrement * i)
            indexEnd = (pixivIncrement * (i + 1))
            WriteCopyPixivID(fr'../PixivUtil2 - Copy ({(i+1)})/list.txt', index, indexEnd)
print('Done!')
os.system('pause')
