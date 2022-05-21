# -*- coding: utf-8 -*-
from configparser import ConfigParser
import os


def Main(overwrite):
    if not os.path.exists('./Scripts config.ini') or overwrite == 'true':

        config = ConfigParser(allow_no_value=True, interpolation=None)
        config.optionxform = str

        config.add_section('Settings')
        config.set('Settings', 'FanboxCopy', '1')
        config.set('Settings', 'PixivCopy', '1')
        config.set('Settings', '  #Arguments should look like this: arg1, arg2, arg3', None)
        config.set('Settings', 'FanboxArg', '-s, f5, -x')
        config.set('Settings', 'PixivArg', '-s, 4, -f, list.txt, --is, -x')
        config.set('Settings', 'PixivExportArg', '-s, e, -p, y, -x, --ef, 2 Pixiv ID.txt')
        config.set('Settings', '  #This removes the ###Export date: ### and ###END-OF-FILE###', None)
        config.set('Settings', 'Scrub', 'true')
        config.set('Settings', '  #Archive date format', None)
        config.set('Settings', 'DateFormat', '%m-%d-%Y_%H-%M-%S')
        config.set('Settings', '  #Add ID to remove. Separate ID with comma: 1234,5678 or 1234, 5678', None)
        config.set('Settings', 'BlacklistID', '')
        config.set('Settings', '  #If there are some ID that uses OAuth to continue, this groups them', None)
        config.set('Settings', 'ProblematicID', '')

        with open(r'./Scripts config.ini', 'w') as f:
            config.write(f)


def Load():
    if not os.path.exists('./Scripts config.ini'):
        Main('')
    config = ConfigParser(allow_no_value=True, interpolation=None)
    config.read(r'./Scripts config.ini')

    return config


if __name__ == '__main__':
    overwrite = ''
    Main('')

    # FanboxCopy = int(config['Settings']['FanboxCopy'])
    # PixivCopy = int(config['Settings']['PixivCopy'])

    # FanboxArg = config['Settings']['FanboxArg']
    # FanboxArg = FanboxArg.split(', ')

    # PixivArg = config['Settings']['PixivArg']
    # PixivArg = PixivArg.split(', ')

    # PixivExportArg = config['Settings']['PixivExportArg']
    # PixivExportArg = PixivExportArg.split(', ')

    # Scrub = config.getboolean('Settings', 'Scrub')
    # DateFormat = config['Settings']['DateFormat']

    # BlacklistID = config['Settings']['BlacklistID']
    # BlacklistID = BlacklistID.split(',')
    # BlacklistID = [_.strip() for _ in BlacklistID]
    # BlacklistID = list(filter(None, BlacklistID))

    # ProblematicID = config['Settings']['ProblematicID']
    # ProblematicID = ProblematicID.split(',')
    # ProblematicID = [_.strip() for _ in ProblematicID]
    # ProblematicID = list(filter(None, ProblematicID))
