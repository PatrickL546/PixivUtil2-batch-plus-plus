# About The Project
A simple Powershell and some Python scripts that I personally use for archiving using PixivUtil2

# Notes
 - PixivUtil2 (https://github.com/Nandaka/PixivUtil2)
 - Read requirements of PixivUtil2
 - I have included a copy of PixivUtil2. But if you want to use other versions, just replace it but it might not work properly

# Usage
 - Go to `!Scripts` folder
 - Set up `config.ini`, or you can replace it with your own `config.ini`
 - I recommend using these settings
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
 - Set up `Scripts settings.psm1`
 - To get started. Run `0 Start.ps1` in PowerShell
 - A normal flow will using option `[1]` then `[2]` and then `[4]`

## Menu
```
-----------------MENU-----------------

Press [1] Make copy
 - Copies config.ini into 'PixivUtil2' folder, and make folder copies

Press [2] Export ID and copy Pixiv ID
 - Exports your online bookmark and process it

Press [3] Open list export (Optional)
 - I used this for debugging

Press [4] Start download

Press [5] Delete db.sqlite (Optional)

Press [6] Delete pixivutil.log (Optional)

Press [7] Convert ugoira to webm (Optional)
 - Uses PixivUtil2 and [FFmpeg] settings in config.ini to convert ugoira to webm
 - Old webm settings uses tons of space, pre-https://github.com/Nandaka/PixivUtil2/releases/tag/v20211104
 - This can save 10x from the original size

Press [8] Delete ugoira zip file (Optional)
 - If you didn't have 'deleteZipFile = True' in [Ugoira] settings in config.ini,
 and have the ugoira zip files taking space. You can use this to delete them
```

# Credits/Contributor
 - PatrickL546 (I can't code, what I write will be bad)

# License

Distributed under the BSD 2-Clause "Simplified" License. See `LICENSE` for more information.
