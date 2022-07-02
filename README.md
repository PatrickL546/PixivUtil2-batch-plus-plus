# About The Project

Simple Python scripts that I personally use for archiving with PixivUtil2

## Requirements

- PixivUtil2 (<https://github.com/Nandaka/PixivUtil2>)
- Read requirements of PixivUtil2
- I have included a copy of PixivUtil2. But if you want to use other versions, just replace it, but it might not work properly
- Windows PC

## Usage

- Set up `config.ini`, or you can replace it with your own `config.ini`
- Use these settings

> useList = True

- See (<https://github.com/Nandaka/PixivUtil2/blob/master/readme.md>) FAQ A.Q3

>[Authentication]  
>username =  
>password =  
>cookie =  
>cookieFanbox =  

- Run `PixivUtil2 Batch Downloader.py` and set up `Scripts config.ini`
- You can continue without restarting the script after you set it up
- Use option [1] to make instances
- Then [2] to export followed artists' ID
- Then [4] to start download
- All other options are not needed

### Menu

    Check https://github.com/PatrickL546/PixivUtil2-batch-downloader for new versions

            Functions

    [1] Make instances
    [2] Export followed artist and process ID
    [3] Open ID list
    [4] Start download
    [5] Delete db.sqlite
    [6] Delete list
    [7] Delete pixivutil.log
    [8] Delete .ugoira zip
    [9] Re-encode webm

    [R] Reset script settings

    Press [CTRL + C] to exit functions
    Enter [Q] to Quit

#### This uses the command line arguments of PixivUtil2

- [1] Make instances
  - Copies `config.ini` to `/Instance/PixivUtil2` and create instance copies
- [2] Export followed artist and process ID
  - Can be modified with any export args in `config.ini`
- [4] Start download
  - Can be modified with any args in `config.ini`
- [6] Delete list
  - Deletes the `list.txt` and `listfanbox.txt`
- [9] Re-encode webm
  - This will override old webm
  - Can be modified using `[FFmpeg]` option in `config.ini` in `/Instance/PixivUtil2`
  - This can save lots of space if your webm are encoded in old settings, pre https://github.com/Nandaka/PixivUtil2/releases/tag/v20211104

## Credits/Contributor

- PatrickL546 (I can't code, what I write will be bad)

## License

Distributed under the BSD 2-Clause "Simplified" License. See `LICENSE` for more information.
