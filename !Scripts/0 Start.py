# -*- coding: utf-8 -*-
import Scripts_config
import os

Scripts_config.Main('')

os.system('color')


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


options = {
    '1': '1 Make copy.py',
    '2': '2 Export ID and copy Pixiv ID.py',
    '3': '3 Open list export.py',
    '4': '4 Start download.py',
    '5': '5 Delete db.sqlite.py',
    '6': '6 Delete pixivutil.log.py',
    '7': '7 Convert ugoira.py',
    '8': '8 Delete ugoira zip file.py',
    '9': '9 Delete list export.py',
    'R': 'true',
    'r': 'true'
}

selected = ''
while not (selected == 'Q' or selected == 'q'):

    print(f'''-----------------MENU-----------------

Enter [1] Make copy

Enter [2] Export ID and copy Pixiv ID

Enter [3] Open list export (Optional)

Enter [4] Start download

Enter [5] Delete db.sqlite (Optional)

Enter [6] Delete pixivutil.log (Optional)

Enter [7] Convert ugoira (Optional)

Enter [8] Delete ugoira zip file (Optional)

Enter [9] Delete list export (Optional)

{bcolors.WARNING}Enter [R] Reset Scripts config to default{bcolors.ENDC}

{bcolors.FAIL}Enter [Q] to Quit{bcolors.ENDC}
''')

    selected = input(': ')

    if selected not in options:
        os.system('cls')
        print(f'{bcolors.WARNING}Please select a valid option{bcolors.ENDC}\n')
    elif selected == 'R' or selected == 'r':
        os.system('cls')
        Scripts_config.Main(options[selected])
        print(f'{bcolors.OKGREEN}You selected option {selected}{bcolors.ENDC}\n')
    else:
        os.system('cls')
        try:
            os.startfile(options[selected])
        except FileNotFoundError:
            print(f'{bcolors.FAIL}File not found{bcolors.ENDC}\n')
        print(f'{bcolors.OKGREEN}You selected option {selected}{bcolors.ENDC}\n')
