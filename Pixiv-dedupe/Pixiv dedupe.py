# -*- coding: utf-8 -*-
from collections import Counter
from blake3 import blake3
from pathlib import Path
import requests
import shutil
import time
import sys
import os
import re


# Start of Hash Functions
def get_hash():
    while True:
        try:
            os.system(f'title Pixiv dedupe {version} - Get hash')
            os.system('cls')
            result_path = './Hash.txt'

            while True:
                print('This uses Blake3 for fast hashing\n')
                print(r'Example: C:\Pixiv')
                path_to_hash = input('Enter directory to hash: ')
                print()

                if not os.path.exists(path_to_hash) or not os.path.isdir(path_to_hash):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a directory\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Hashing...\n')
            path_and_hash = []
            for path in Path(path_to_hash).rglob('*'):
                blake = blake3()
                if not Path.is_dir(path):
                    with open(path, 'rb') as f:
                        blake.update(f.read())
                    path_and_hash.append(f'{str(path)}//{str(blake.hexdigest())}\n')
                    print(f'Files hashed: {len(path_and_hash)}', end='\r')
                else:
                    pass

            with open(result_path, 'w', encoding='utf-8') as f:
                for line in path_and_hash:
                    f.write(line)

            print('\nDone!')
            os.system('pause')
            print('Going to menu...')
            time.sleep(2)
            break

        except KeyboardInterrupt:
            os.system('cls')
            print('Going to menu...')
            time.sleep(1)
            break


def get_hash_dupe_and_unique():
    while True:
        try:
            os.system(f'title Pixiv dedupe {version} - Get hash duplicate and unique')
            os.system('cls')
            result_unique_path = './HashUnique.txt'
            result_dupe_path = './HashDupe.txt'

            while True:
                print('Duplicates are counted when same file name and hash, everything else is unique\n')
                print(r'Example: C:\Users\User\Downloads\Hash.txt or Hash.txt')
                hash_path = input('Enter Hash path: ')
                print()

                if not os.path.exists(hash_path) or not os.path.isfile(hash_path):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a file\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Thinking...\n')
            with open(hash_path, encoding='utf-8') as f:
                hash_list = f.readlines()

            file_name_and_hash = []
            unique_hash = []
            dupe_hash = []
            # Make list of only filename//hash
            for line in hash_list:
                line_tuple = line.partition('//')
                file_name = os.path.basename(line_tuple[0])
                hash = line_tuple[2]
                file_name_and_hash.append(f'{file_name}//{hash}')

            # Count filename//hash
            file_name_and_hash_count_dict = Counter(file_name_and_hash)

            # Find unique and dupe by count
            for index, line in enumerate(hash_list):
                file_name_and_hash_count = file_name_and_hash_count_dict.get(file_name_and_hash[index])

                if file_name_and_hash_count == 1:
                    unique_hash.append(line)
                else:
                    dupe_hash.append(line)

            with open(result_unique_path, 'w', encoding='utf-8') as f:
                for line in unique_hash:
                    f.write(line)

            with open(result_dupe_path, 'w', encoding='utf-8') as f:
                for line in dupe_hash:
                    f.write(line)

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


def get_hash_difference():
    while True:
        try:
            os.system(f'title Pixiv dedupe {version} - Get hash difference')
            os.system('cls')
            result_path = './HashDifference.txt'

            def check():
                while True:
                    print(r'Example: C:\Users\User\Downloads\Hash.txt or Hash.txt')
                    hash_path = input('Enter Hash path: ')
                    print()

                    if not os.path.exists(hash_path) or not os.path.isfile(hash_path):
                        os.system('cls')
                        print(f'{bcolors.FAIL}Error: Path does not exist or not a file\n{bcolors.ENDC}')
                    else:
                        return hash_path

            print(f'{bcolors.WARNING}This will lose order{bcolors.ENDC}\n')
            print('First Hash\n')
            file_1 = check()
            print('Second Hash\n')
            file_2 = check()

            os.system('cls')
            print('Thinking...\n')
            with open(file_1, encoding='utf-8') as f:
                hash_file_1 = f.readlines()

            with open(file_2, encoding='utf-8') as f:
                hash_file_2 = f.readlines()

            # Find difference between 2 list, get item in list 1 not exist in list 2 and vice versa
            difference = set(hash_file_1) ^ set(hash_file_2)

            with open(result_path, 'w', encoding='utf-8') as f:
                for line in difference:
                    f.write(line)

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


def sort_hash(title, result_path, regex_pattern):
    while True:
        try:
            os.system(title)
            os.system('cls')
            result_path = result_path

            while True:
                print(r'Example: C:\Users\User\Downloads\Hash.txt or Hash.txt')
                hash_path = input('Enter Hash path: ')
                print()

                if not os.path.exists(hash_path) or not os.path.isfile(hash_path):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a file\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Thinking...\n')
            with open(hash_path, encoding='utf-8') as f:
                hash_list = f.readlines()

            def key_sort(hash_list):
                pattern = re.compile(regex_pattern)
                return list(map(str, pattern.findall(hash_list)))

            hash_list.sort(key=key_sort)

            with open(result_path, 'w', encoding='utf-8') as f:
                for line in hash_list:
                    f.write(line)

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
# End of Hash Functions


# Start of Folder Functions
def rename_pixiv_folders():
    while True:
        try:
            os.system(f'title Pixiv dedupe {version} - Rename Pixiv folders')
            os.system('cls')

            while True:
                print("This will append 'old_' to the folders, it will not keep appending it if it startswith 'old_'\n")
                print(r'Example: C:\Pixiv')
                pixiv_path = input('Enter directory to rename: ')
                print()

                if not os.path.exists(pixiv_path) or not os.path.isdir(pixiv_path):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a directory\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Thinking...\n')
            for path in Path(pixiv_path).glob('*'):
                if Path.is_dir(path) and not path.name.startswith('old_'):
                    path.rename(os.path.join(pixiv_path, f'old_{path.name}'))

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


def move_files():
    while True:
        try:
            os.system(f'title Pixiv dedupe {version} - Move files to new folders')
            os.system('cls')

            while True:
                print(r'Example: C:\Users\User\Downloads\Hash.txt or Hash.txt')
                hash_path = input('Enter Hash path: ')
                print()

                if not os.path.exists(hash_path) or not os.path.isfile(hash_path):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a file\n{bcolors.ENDC}')
                else:
                    break

            with open(hash_path, encoding='utf-8') as f:
                hash_list = f.readlines()

            os.system('cls')
            print('Thinking...\n')

            # Make new list of dupes and only keep one of same filename and hash. Only keep items with Pixiv ID
            # Get PixivID
            move_hash_list = []
            pixiv_id_list = []
            visited = set()
            # Get PixivID, matches '(1234)\', captures 1234
            pixiv_id_pattern = re.compile(r'\((\d+)\)\\')
            for line in hash_list:
                line_tuple = line.partition('//')
                file_name = os.path.basename(line_tuple[0])
                hash = line_tuple[2]
                file_name_and_hash = f'{file_name}//{hash}'

                if file_name_and_hash not in visited and pixiv_id_pattern.findall(line):
                    visited.add(file_name_and_hash)
                    move_hash_list.append(line)
                    pixiv_id_list.append(pixiv_id_pattern.findall(line))

            # Get Pixiv folder path
            line_tuple = move_hash_list[0].partition('//')
            pixiv_folder = Path(line_tuple[0]).parents[1]

            # Move files to folder
            def move_files(file_path, folder_path):
                os.makedirs(folder_path, exist_ok=True)
                full_file_path = os.path.join(folder_path, os.path.basename(file_path))

                # Retry amount
                for i in range(3):
                    try:
                        if os.path.exists(file_path):
                            shutil.move(file_path, folder_path)
                            break
                        else:
                            print(f'File not found: {file_path}')
                            break
                    except shutil.Error:
                        file_time = os.path.getctime(full_file_path)
                        file_time = time.strftime('%Y%m%d_%H%M%S', time.gmtime(file_time))
                        os.rename(full_file_path, f'{full_file_path}.{file_time}')

            fanbox_pattern = re.compile(r'\\old_FANBOX')
            for index, line in enumerate(move_hash_list):
                line_tuple = line.partition('//')
                file_path = line_tuple[0]

                if fanbox_pattern.findall(line):
                    fanbox_folder_path = os.path.join(pixiv_folder, f'FANBOX ({pixiv_id_list[index][0]})')
                    move_files(file_path, fanbox_folder_path)
                else:
                    pixiv_folder_path = os.path.join(pixiv_folder, f'({pixiv_id_list[index][0]})')
                    move_files(file_path, pixiv_folder_path)

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


def move_old_folders():
    while True:
        try:
            os.system("title Move 'old_' folders to a separate folder")
            os.system('cls')

            while True:
                print("Moves folders that startswith 'old_' to '!old_Pixiv'")
                print('You can then delete this folder as it only contains duplicates\n')
                print(r'Example: C:\Pixiv')
                pixiv_path = input('Enter Pixiv directory: ')
                print()

                if not os.path.exists(pixiv_path) or not os.path.isdir(pixiv_path):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a directory\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Thinking...\n')
            old_folder = '!old_Pixiv'

            os.makedirs(os.path.join(pixiv_path, old_folder), exist_ok=True)

            for path in Path(pixiv_path).glob('old_*'):
                if Path.is_dir(path):
                    shutil.move(path, os.path.join(pixiv_path, old_folder))

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


def get_pixiv_folder_list_and_pixiv_id():
    while True:
        try:
            os.system(f'title Pixiv dedupe {version} - Get Pixiv folder list and Pixiv ID')
            os.system('cls')
            result_directory_path = './PixivFolderDirectory.txt'
            result_id_path = './PixivFolderPixivID.txt'

            while True:
                print('The result does not include folders without a Pixiv ID, keeps folders like ex. test (1234)')
                print(r'Example: C:\Pixiv')
                pixiv_path = input('Enter Pixiv directory: ')
                print()

                if not os.path.exists(pixiv_path) or not os.path.isdir(pixiv_path):
                    os.system('cls')
                    print(f'{bcolors.FAIL}Error: Path does not exist or not a directory\n{bcolors.ENDC}')
                else:
                    break

            os.system('cls')
            print('Thinking...\n')
            directory_list = []
            pixiv_id_list = []
            # Get PixivID, matches '(1234)', captures 1234
            pixiv_id_pattern = re.compile(r'\((\d+)\)')
            for path in Path(pixiv_path).glob('*'):
                if Path.is_dir(path) and pixiv_id_pattern.findall(str(path)):
                    directory_list.append(str(path))
                    pixiv_id_list.append(pixiv_id_pattern.findall(str(path)))

            with open(result_directory_path, 'w', encoding='utf-8') as f:
                for line in directory_list:
                    f.write(f'{line}\n')

            with open(result_id_path, 'w', encoding='utf-8') as f:
                for line in pixiv_id_list:
                    f.write(f'{line[0]}\n')

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


def main(version):
    while True:
        try:
            r = requests.get('https://api.github.com/repos/PatrickL546/Pixiv-dedupe/releases/latest')
            online_version = r.json()['name']
            new_version_link = r.json()['html_url']
            if online_version > version:
                print(f'{bcolors.OKBLUE}New version(s) is available: {online_version}{bcolors.ENDC}')
                print(f'{bcolors.OKBLUE}{new_version_link}{bcolors.ENDC}')
        except Exception:
            print('Failed to check for new version')

        valid_options = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        os.system(f'title Pixiv dedupe {version} - Menu')
        print(f'''
                        {bcolors.BOLD}Hash Functions{bcolors.ENDC}                          {bcolors.BOLD}Folder Functions{bcolors.ENDC}
                {bcolors.OKGREEN}
                [1] Get hash                             [6] Rename Pixiv folders
                [2] Get hash duplicate and unique        [7] Move files to new folders
                [3] Get hash difference                  [8] Move 'old_' folders to a separate folder
                [4] Sort hash by hash                    [9] Get Pixiv folder list and Pixiv ID
                [5] Sort hash by Pixiv ID

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
            get_hash()
            os.system('cls')
        elif selected == '2':
            get_hash_dupe_and_unique()
            os.system('cls')
        elif selected == '3':
            get_hash_difference()
            os.system('cls')
        elif selected == '4':
            title = f'title Pixiv dedupe {version} - Sort hash by hash'
            result_path = './HashSortedByHash.txt'
            # Get hash, positive lookbehind, gets everything after '//'
            regex_pattern = r'(?<=\/\/).+'

            sort_hash(title, result_path, regex_pattern)
            os.system('cls')
        elif selected == '5':
            title = f'title Pixiv dedupe {version} - Sort hash by Pixiv ID'
            result_path = './HashSortedByPixivID.txt'
            # Get PixivID, matches '(1234)\', captures 1234
            regex_pattern = r'\((\d+)\)\\'

            sort_hash(title, result_path, regex_pattern)
            os.system('cls')
        elif selected == '6':
            rename_pixiv_folders()
            os.system('cls')
        elif selected == '7':
            move_files()
            os.system('cls')
        elif selected == '8':
            move_old_folders()
            os.system('cls')
        elif selected == '9':
            get_pixiv_folder_list_and_pixiv_id()
            os.system('cls')


if __name__ == '__main__':
    version='v20221203'
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

    main(version)
