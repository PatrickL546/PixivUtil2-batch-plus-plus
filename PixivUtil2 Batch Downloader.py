# -*- coding: utf-8 -*-
from configparser import ConfigParser
from datetime import datetime
from pathlib import Path
import subprocess
import shutil
import math
import time
import sys
import os


def start_config(overwrite=None):
    while True:
        try:
            os.system('title PixivUtil2 Batch Downloader - Config')
            os.system('cls')

            if not os.path.exists('./Script config.ini') or overwrite:

                config = ConfigParser(allow_no_value=True, interpolation=None)
                config.optionxform = str

                config.add_section('Settings')
                config.set('Settings', 'ConfigFile', 'config.ini')
                config.set('Settings', 'FanboxCopy', '1')
                config.set('Settings', 'PixivCopy', '1')
                config.set('Settings', '  #Arguments should look like this: arg1, arg2, arg3', None)
                config.set('Settings', 'FanboxArg', '-s, f5, -x')
                config.set('Settings', 'PixivArg', '-s, 4, -f, list.txt, --is, -x')
                config.set('Settings', 'PixivExportArg', '-s, e, -p, y, -x, --ef, PixivUtil2 export.txt')
                config.set('Settings', '  #This removes the ###Export date: ### and ###END-OF-FILE###', None)
                config.set('Settings', 'Scrub', 'true')
                config.set('Settings', '  #Archive date format', None)
                config.set('Settings', 'DateFormat', '%m-%d-%Y_%H-%M-%S')
                config.set('Settings', '  #Add ID to remove. Separate ID with comma: 1234,5678 or 1234, 5678', None)
                config.set('Settings', 'BlacklistID', '')
                config.set('Settings', '  #If there are some ID that uses OAuth to continue, this groups them', None)
                config.set('Settings', 'ProblematicID', '')

                with open('./Script config.ini', 'w') as f:
                    config.write(f)

            break

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            break


def load_config():
    while True:
        try:
            os.system('title PixivUtil2 Batch Downloader - Load config')
            os.system('cls')

            if not os.path.exists('./Script config.ini'):
                start_config()

            config = ConfigParser(allow_no_value=True, interpolation=None)
            config.read('./Script config.ini')
            return config

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            break


def make_instances():
    while True:
        try:
            os.system('title PixivUtil2 Batch Downloader - Make instances')
            os.system('cls')

            config = load_config()

            config_file = config['Settings']['ConfigFile']

            fanbox_copy = int(config['Settings']['FanboxCopy'])
            pixiv_copy = int(config['Settings']['PixivCopy'])

            problematic_id = config['Settings']['ProblematicID']
            problematic_id = problematic_id.split(',')
            problematic_id = [_.strip() for _ in problematic_id]
            problematic_id = list(filter(None, problematic_id))

            shutil.copy(config_file, './Instance/PixivUtil2-master')

            print('Copied config.ini to ./Instance/PixivUtil2-master\n')

            try:
                shutil.copytree('./Instance/PixivUtil2-master',
                                './Instance/PixivUtil2', dirs_exist_ok=True)
            except Exception:
                print('Failed to copy PixivUtil2-master')
                os.system('pause')
                print('Going to menu...')
                time.sleep(2)
                break

            print('Copied ./Instance/PixivUtil2-master to ./Instance/PixivUtil2\n')

            if problematic_id:
                shutil.copytree('./Instance/PixivUtil2-master',
                                './Instance/PixivUtil2 - Problematic', dirs_exist_ok=True)

                print('Copied ./Instance/PixivUtil2-master to ./Instance/PixivUtil2 - Problematic\n')

            print('Making copies of ./Instance/PixivUtil2 - Fanbox\n')

            for i in range(fanbox_copy):
                if i == 0:
                    shutil.copytree('./Instance/PixivUtil2-master',
                                    './Instance/PixivUtil2 - Fanbox', dirs_exist_ok=True)
                elif i == 1:
                    shutil.copytree('./Instance/PixivUtil2-master',
                                    './Instance/PixivUtil2 - Fanbox - Copy', dirs_exist_ok=True)
                else:
                    shutil.copytree('./Instance/PixivUtil2-master',
                                    f'./Instance/PixivUtil2 - Fanbox - Copy ({i})', dirs_exist_ok=True)

            print('Making copies of ./Instance/PixivUtil2 - Copy\n')

            # Starts counting from 1 to sync up numbers in 'copy ()'
            for i in range(1, (pixiv_copy + 1)):
                if i == 1:
                    shutil.copytree('./Instance/PixivUtil2-master',
                                    './Instance/PixivUtil2 - Copy', dirs_exist_ok=True)
                else:
                    shutil.copytree('./Instance/PixivUtil2-master',
                                    f'./Instance/PixivUtil2 - Copy ({i})', dirs_exist_ok=True)

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            break

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            break


def export_followed_artist_and_process_id():
    while True:
        try:
            os.system('title PixivUtil2 Batch Downloader - Export followed artist and process ID')
            os.system('cls')

            config = load_config()

            fanbox_copy = int(config['Settings']['FanboxCopy'])
            pixiv_copy = int(config['Settings']['PixivCopy'])

            pixiv_export_arg = config['Settings']['PixivExportArg']
            pixiv_export_arg = pixiv_export_arg.split(', ')

            scrub = config.getboolean('Settings', 'Scrub')
            date_format = config['Settings']['DateFormat']

            blacklist_id = config['Settings']['BlacklistID']
            blacklist_id = blacklist_id.split(',')
            blacklist_id = [_.strip() for _ in blacklist_id]
            blacklist_id = list(filter(None, blacklist_id))

            problematic_id = config['Settings']['ProblematicID']
            problematic_id = problematic_id.split(',')
            problematic_id = [_.strip() for _ in problematic_id]
            problematic_id = list(filter(None, problematic_id))

            while True:
                try:
                    config = load_config()
                    valid_options = {'1', '2', '3', 'c', 'C'}

                    print(f'''
        {bcolors.BOLD}Menu{bcolors.ENDC}
{bcolors.OKGREEN}
[1] Export followed artist
[2] Remove blacklisted ID from list
[3] Archive ID list

[C] Continue

{bcolors.FAIL}Enter [Q] to Quit{bcolors.ENDC}
''')

                    selected = input('Input: ')

                    if (selected == 'c' or selected == 'C'):
                        os.system('cls')
                        break
                    elif (selected == 'q' or selected == 'Q'):
                        sys.exit()
                    elif selected not in valid_options:
                        os.system('cls')
                        print(f'{bcolors.FAIL}Please select a valid option{bcolors.ENDC}')
                    elif selected == '1':
                        args = ['python.exe', './Instance/PixivUtil2/PixivUtil2.py']
                        args.extend(pixiv_export_arg)

                        subprocess.run(args, creationflags=subprocess.CREATE_NEW_CONSOLE)

                        if scrub:
                            with open('./PixivUtil2 export.txt', 'r') as f:
                                content = f.read().splitlines()
                                content = [_ for _ in content if '#' not in _]

                            with open('./PixivUtil2 export.txt', 'w') as f:
                                for line in content:
                                    f.write(f'{line}\n')

                        os.system('cls')
                    elif selected == '2':
                        with open('./PixivUtil2 export.txt', 'r') as f:
                            content = f.read().splitlines()
                            content = [_ for _ in content if _ not in blacklist_id]

                        with open('./PixivUtil2 export.txt', 'w') as f:
                            for line in content:
                                f.write(f'{line}\n')

                        os.system('cls')
                    elif selected == '3':
                        os.makedirs('./Export archive', exist_ok=True)

                        time_now = datetime.today()
                        time_now = time_now.strftime(date_format)

                        try:
                            shutil.copy('./PixivUtil2 export.txt', f'./Export archive/PixivUtil2 export {time_now}.txt')
                        except Exception:
                            print(f'{bcolors.FAIL}Failed to archive{bcolors.ENDC}\n')

                        os.system('cls')

                except KeyboardInterrupt:
                    os.system('cls')
                    print('Going to menu...')
                    time.sleep(1)
                    break

            if problematic_id:
                # Copies problematic_id to './Instance/PixivUtil2 - Problematic'
                with open('./PixivUtil2 export.txt', 'r') as f:
                    content = f.read().splitlines()
                    problematic_id_in_export_list = [_ for _ in content if _ in problematic_id]

                with open('./Instance/PixivUtil2 - Problematic/list.txt', 'w') as f:
                    for line in problematic_id_in_export_list:
                        f.write(f'{line}\n')

                with open('./Instance/PixivUtil2 - Problematic/listfanbox.txt', 'w') as f:
                    for line in problematic_id_in_export_list:
                        f.write(f'{line}\n')

                # Remove problematic_id from PixivUtil2 export.txt
                with open('./PixivUtil2 export.txt', 'r') as f:
                    content = f.read().splitlines()
                    content = [_ for _ in content if _ not in problematic_id]

                    with open('./PixivUtil2 export.txt', 'w') as f:
                        for line in content:
                            f.write(f'{line}\n')

            # Read './PixivUtil2 export.txt'
            with open('./PixivUtil2 export.txt', 'r') as f:
                pixivUtil2_export_content = f.read().splitlines()

            def write_id(path, index_start, index_end):
                os.makedirs(os.path.dirname(path), exist_ok=True)

                with open(path, 'w') as f:
                    id_list = pixivUtil2_export_content[index_start:index_end]
                    for line in id_list:
                        f.write(f'{line}\n')

            line_count = sum(1 for _ in open('./PixivUtil2 export.txt', 'r'))

            # Divides ID onto different instances
            # Fanbox instances
            if fanbox_copy > 0:
                fanbox_increment = math.ceil(line_count / fanbox_copy)

                for i in range(fanbox_copy):
                    if i == 0:
                        index_start = 0
                        index_end = fanbox_increment
                        write_id('./Instance/PixivUtil2 - Fanbox/listfanbox.txt', index_start, index_end)
                    elif i == 1:
                        index_start = fanbox_increment
                        index_end = (fanbox_increment * 2)
                        write_id('./Instance/PixivUtil2 - Fanbox - Copy/listfanbox.txt', index_start, index_end)
                    else:
                        index_start = (fanbox_increment * i)
                        index_end = (fanbox_increment * (i + 1))
                        write_id(f'./Instance/PixivUtil2 - Fanbox - Copy ({i})/listfanbox.txt', index_start, index_end)

            # Pixiv instances
            if pixiv_copy > 0:
                pixiv_increment = math.ceil(line_count / pixiv_copy)

                for i in range(pixiv_copy):
                    if i == 0:
                        index_start = 0
                        index_end = pixiv_increment
                        write_id('./Instance/PixivUtil2 - Copy/list.txt', index_start, index_end)
                    elif i == 1:
                        index_start = pixiv_increment
                        index_end = (pixiv_increment * 2)
                        write_id(f'./Instance/PixivUtil2 - Copy ({(i+1)})/list.txt', index_start, index_end)
                    else:
                        index_start = (pixiv_increment * i)
                        index_end = (pixiv_increment * (i + 1))
                        write_id(f'./Instance/PixivUtil2 - Copy ({(i+1)})/list.txt', index_start, index_end)

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            break

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            break


def open_id_list():
    while True:
        try:
            os.system('title PixivUtil2 Batch Downloader - Open ID list')
            os.system('cls')

            for path in Path('./Instance').rglob('list*'):
                os.startfile(path)

            break

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            break


def start_download():
    while True:
        try:
            os.system('title PixivUtil2 Batch Downloader - Start download')
            os.system('cls')

            config = load_config()

            fanbox_arg = config['Settings']['FanboxArg']
            fanbox_arg = fanbox_arg.split(', ')

            pixiv_arg = config['Settings']['PixivArg']
            pixiv_arg = pixiv_arg.split(', ')

            problematic_id = config['Settings']['ProblematicID']
            problematic_id = problematic_id.split(',')
            problematic_id = [_.strip() for _ in problematic_id]
            problematic_id = list(filter(None, problematic_id))

            print(f'''{bcolors.FAIL}##### DO NOT CLOSE #####{bcolors.ENDC}''')

            if problematic_id:
                dl_args_fanbox = ['python.exe', './PixivUtil2.py']
                dl_args_pixiv = ['python.exe', './PixivUtil2.py']

                dl_args_fanbox.extend(fanbox_arg)
                dl_args_pixiv.extend(pixiv_arg)

                subprocess.run(dl_args_fanbox, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd='./Instance/PixivUtil2 - Problematic')
                subprocess.run(dl_args_pixiv, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd='./Instance/PixivUtil2 - Problematic')

            fanbox_path = Path('./Instance').glob('PixivUtil2 - Fanbox*')
            pixiv_path = Path('./Instance').glob('PixivUtil2 - Copy*')

            for path in fanbox_path:
                dl_args_fanbox = ['python.exe', './PixivUtil2.py']

                dl_args_fanbox.extend(fanbox_arg)

                subprocess.Popen(dl_args_fanbox, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=f'{path}')

            for path in pixiv_path:
                dl_args_pixiv = ['python.exe', './PixivUtil2.py']

                dl_args_pixiv.extend(pixiv_arg)

                subprocess.Popen(dl_args_pixiv, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=f'{path}')

            break

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            break


def delete_files(title, file_warning, file_delete):
    while True:
        try:
            os.system(title)
            os.system('cls')

            print(f'{bcolors.WARNING}Warning! this will permanently delete {file_warning} file(s)\n{bcolors.ENDC}')
            os.system('pause')
            print()

            for path in Path('./Instance').rglob(file_delete):
                try:
                    os.remove(path)
                    print(f'Deleted {path}')
                except FileNotFoundError:
                    print(f'File not found {path}\n')
                except Exception:
                    print('File is open or unhandled exception\n')

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            break

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            break


def delete_ugoira_zip():
    while True:
        try:
            os.system('title PixivUtil2 Batch Downloader - Delete .ugoira zip')
            os.system('cls')

            print(f'{bcolors.WARNING}Warning! this will permanently delete .ugoira zip file(s)\n{bcolors.ENDC}')
            pixiv_directory = input('Enter Pixiv directory: ')
            print()

            for path in Path(pixiv_directory).rglob('*.ugoira'):
                ugo_name = str(path)
                zip_name = f'{ugo_name[:-7]}.zip'
                try:
                    os.remove(zip_name)
                    print(f'Deleted {zip_name}')
                except FileNotFoundError:
                    print(f'File not found {zip_name}\n')
                except Exception:
                    print('File is open or unhandled exception\n')

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            break

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            break


def re_encode_webm():
    while True:
        try:
            os.system('title PixivUtil2 Batch Downloader - Re-encode webm')
            os.system('cls')

            config = load_config()

            config_file = config['Settings']['ConfigFile']

            sys.path.append('./Instance/PixivUtil2')
            try:
                import PixivConfig
                import PixivHelper
            except ModuleNotFoundError:
                print('Cannot import PixivConfig and PixivHelper. Exiting!')
                time.sleep(5)
                sys.exit()

            pixiv_config = PixivConfig.PixivConfig()
            pixiv_config.loadConfig(config_file)

            PixivHelper.set_config(pixiv_config)

            os.system('cls')

            print(f'{bcolors.WARNING}Re-encoding had been implemented in PixivUtil2\n{bcolors.ENDC}')

            pixiv_config.rootDirectory = input('Enter Pixiv directory: ')

            for path in Path(pixiv_config.rootDirectory).rglob('*.ugoira'):
                ugo_name = str(path)
                webm_filename = f'{ugo_name[:-7]}.{pixiv_config.ffmpegExt}'
                PixivHelper.ugoira2webm(ugo_name, webm_filename)

                ts = os.path.getmtime(ugo_name)
                os.utime(webm_filename, (ts, ts))

            print('Done!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            break

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            break


def main():
    while True:
        valid_options = {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'r', 'R'}
        print(f'{bcolors.OKBLUE}Check https://github.com/PatrickL546/PixivUtil2-batch-downloader for new versions{bcolors.ENDC}')
        os.system('title PixivUtil2 Batch Downloader - Menu')
        print(f'''
        {bcolors.BOLD}Functions{bcolors.ENDC}
{bcolors.OKGREEN}
[1] Make instances
[2] Export followed artist and process ID
[3] Open ID list
[4] Start download
[5] Delete db.sqlite
[6] Delete list
[7] Delete pixivutil.log
[8] Delete .ugoira zip
[9] Re-encode webm

{bcolors.WARNING}[R] Reset script settings{bcolors.ENDC}

{bcolors.WARNING}Press [CTRL + C] to exit functions{bcolors.ENDC}
{bcolors.FAIL}Enter [Q] to Quit{bcolors.ENDC}
''')

        selected = input('Input: ')

        if (selected == 'q' or selected == 'Q'):
            sys.exit()
        elif selected not in valid_options:
            os.system('cls')
            print(f'{bcolors.FAIL}Please select a valid option{bcolors.ENDC}')
        elif selected == '1':
            make_instances()
            os.system('cls')
        elif selected == '2':
            export_followed_artist_and_process_id()
            os.system('cls')
        elif selected == '3':
            open_id_list()
            os.system('cls')
        elif selected == '4':
            start_download()
            os.system('cls')
        elif selected == '5':
            title = 'title PixivUtil2 Batch Downloader - Delete db.sqlite'
            file_warning = 'db.sqlite'
            file_delete = 'db.sqlite'
            delete_files(title, file_warning, file_delete)
            os.system('cls')
        elif selected == '6':
            title = 'title PixivUtil2 Batch Downloader - Delete list'
            file_warning = 'list'
            file_delete = 'list*'
            delete_files(title, file_warning, file_delete)
            os.system('cls')
        elif selected == '7':
            title = 'title PixivUtil2 Batch Downloader - Delete pixivutil.log'
            file_warning = 'pixivutil.log'
            file_delete = 'pixivutil.log*'
            delete_files(title, file_warning, file_delete)
            os.system('cls')
        elif selected == '8':
            delete_ugoira_zip()
            os.system('cls')
        elif selected == '9':
            re_encode_webm()
            os.system('cls')
        elif (selected == 'r' or selected == 'R'):
            start_config(overwrite=True)
            os.system('cls')
            print(f'{bcolors.OKGREEN}Script config reset{bcolors.ENDC}')


if __name__ == '__main__':
    os.system('color')

    class bcolors:
        HEADER    = '\033[95m'
        OKBLUE    = '\033[94m'
        OKGREEN   = '\033[92m'
        WARNING   = '\033[93m'
        FAIL      = '\033[91m'
        BOLD      = '\033[1m'
        UNDERLINE = '\033[4m'
        ENDC      = '\033[0m'

    start_config()
    main()

    # Get value from config

    # config_file = config['Settings']['ConfigFile']

    # fanbox_copy = int(config['Settings']['FanboxCopy'])
    # pixiv_copy = int(config['Settings']['PixivCopy'])

    # fanbox_arg = config['Settings']['FanboxArg']
    # fanbox_arg = fanbox_arg.split(', ')

    # pixiv_arg = config['Settings']['PixivArg']
    # pixiv_arg = pixiv_arg.split(', ')

    # pixiv_export_arg = config['Settings']['PixivExportArg']
    # pixiv_export_arg = pixiv_export_arg.split(', ')

    # scrub = config.getboolean('Settings', 'Scrub')
    # date_format = config['Settings']['DateFormat']

    # blacklist_id = config['Settings']['BlacklistID']
    # blacklist_id = blacklist_id.split(',')
    # blacklist_id = [_.strip() for _ in blacklist_id]
    # blacklist_id = list(filter(None, blacklist_id))

    # problematic_id = config['Settings']['ProblematicID']
    # problematic_id = problematic_id.split(',')
    # problematic_id = [_.strip() for _ in problematic_id]
    # problematic_id = list(filter(None, problematic_id))
