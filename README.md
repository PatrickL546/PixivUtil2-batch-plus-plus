# About The Project

Simple Python scripts that I personally use for archiving using PixivUtil2

## Requirements

- PixivUtil2 (<https://github.com/Nandaka/PixivUtil2>)
- Read requirements of PixivUtil2
- I have included a copy of PixivUtil2. But if you want to use other versions, just replace it but it might not work properly
- Windows PC

## Usage

- Go to `!Scripts` folder
- Set up `config.ini`, or you can replace it with your own `config.ini`
- Use these settings, it might not work properly otherwises

> useList = True

- See (<https://github.com/Nandaka/PixivUtil2/blob/master/readme.md>) FAQ A.Q3

>username =  
>password =  
>cookie =  
>cookieFanbox =  

- Run `Scripts_config.py` or `0 Start.py` to make the config file
- Set up `Scripts config.ini`
- To get started. Run `0 Start.py` (Note that you can run the scripts on their own without using this)
- Normal steps will using option `[1]` then `[2]` and then `[4]` to download

### Menu

> -----------------MENU-----------------
>
> Enter [1] Make copy
>
> - Copies config.ini into 'PixivUtil2' folder, and make folder copies
>
> Enter [2] Export ID and copy Pixiv ID
>
> - Exports your online bookmark and process it
>
> Enter [3] Open list export (Optional)
>
> - I use this for checking which ID is in which instances
>
> Enter [4] Start download
>
> Enter [5] Delete db.sqlite (Optional)
>
> Enter [6] Delete pixivutil.log (Optional)
>
> Enter [7] Convert ugoira (Optional)
>
> - Uses PixivUtil2 and [FFmpeg] settings in config.ini to convert ugoira to webm or any extention you choose
>
> - Old webm settings uses tons of space, pre-<https://github.com/Nandaka/PixivUtil2/releases/tag/v20211104>
>
> - This can save ~10x from the original size
>
> Enter [8] Delete ugoira zip file (Optional)
>
> - If you didn't have 'deleteZipFile = True' in [Ugoira] settings in config.ini, and have the ugoira zip files taking space. You can use this to delete them
>
> Enter [9] Delete list export (Optional)
>
> Enter [R] Reset Scripts config to default
>
> Enter [Q] to Quit

## Credits/Contributor

- PatrickL546 (I can't code, what I write will be bad)

## License

Distributed under the BSD 2-Clause "Simplified" License. See `LICENSE` for more information.
