# About The Project
A simple batch downloader for PixivUtil2 that I personally use for archiving

# Prerequisites
 - PixivUtil2 (Included) (https://github.com/Nandaka/PixivUtil2)

# Installation
I have included a copy of PixivUtil2. But if you want to use other versions, just replace it but it might not work properly

# Usage
 - Set up 'config.ini' in '!Scripts' folder, or you can copy your own config.ini into '!Scripts' folder
 - Use these settings
```
useList = True
```
 - See (https://github.com/Nandaka/PixivUtil2/blob/master/readme.md) FAQ A.Q3
```
username =
password =
cookie =
cookieFanbox =
```
 - Set up 'Scripts settings.psm1' in '!Scripts' folder

## Menu
```
-----------------MENU-----------------

Press [1] Make copy
 - Copies config.ini into 'PixivUtil2' folder and make folder copies

Press [2] Export ID and copy Pixiv ID
 - Exports your online bookmark and process it

Press [3] Open list export (Optional)
 - I used this for debugging

Press [4] Start download

Press [5] Delete db.sqlite (Optional)

Press [6] Delete pixivutil.log (Optional)

Press [7] Convert ugoira to webm (Optional)
 - Uses PixivUtil2 and [FFmpeg] settings in config.ini to convert ugoira to webm

Press [8] Delete ugoira zip file (Optional)
 - If you didn't have 'deleteZipFile = True' in [Ugoira] settings in config.ini,
 and have the ugoira zip files taking space. You can use this to delete them
```

# Credits/Contributor
 - PatrickL546

# License

Distributed under the BSD 2-Clause "Simplified" License. See `LICENSE` for more information.