# About The Project

Simple Python scripts that I personally use for archiving with PixivUtil2

Hopefully merge dedupe if I have time

> [!NOTE]  
> Not in active development, could use a rewrite

## Warning

- Pixiv recently limited the ammount of connections, keep the PixivUtil2 download instance to 1

## Requirements

- PixivUtil2 (<https://github.com/Nandaka/PixivUtil2>)
- Read requirements of PixivUtil2
- Additional library listed in requirements.txt
- I have included a copy of PixivUtil2. But if you want to use other versions, just replace it, but it might not work properly
- Windows PC

## Usage

### To update your instances, replace `PixivUtil2-master` with the newer version and use option [1]

- Set up `config.ini`, or you can replace it with your own `config.ini`
- Use these settings

> useList = True

- See (<https://github.com/Nandaka/PixivUtil2/blob/master/readme.md>) FAQ A.Q3

>[Authentication]  
>username =  
>password =  
>cookie =  
>cookieFanbox =  

- Run `PixivUtil2_batch_downloader.py` and set up `script_config.ini`
- You can continue without restarting the script after you set it up
- Use option [1] to make instances
- Then [2] to export followed artists' ID
- Then [4] to start download
- All other options are not needed

### Menu

            Functions

    [1] Make instances
    [2] Export followed artist and process ID
    [3] Open ID list
    [4] Start download
    [5] Delete db.sqlite
    [6] Delete list
    [7] Delete pixivutil.log
    [8] Delete .ugoira zip

            Extras

    [9] Re-encode webm
    [A] Follow Pixiv users
    [B] Bookmark artworks

    [R] Reset Script config

    Press [CTRL + C] to exit functions
    Enter [Q] to Quit

#### This uses the command line arguments of PixivUtil2

- [1] Make instances
  - Copies `config.ini` to `/Instance/PixivUtil2` and create instance copies
- [2] Export followed artist and process ID
  - Can be modified with any export args in `script_config.ini`
- [4] Start download
  - Can be modified with any args in `script_config.ini`
- [6] Delete list
  - Deletes the `list.txt` and `listfanbox.txt`
- [9] Re-encode webm
  - This will override old webm
  - Can be modified using `[FFmpeg]` option in `config.ini` in `/Instance/PixivUtil2`
  - This can save lots of space if your webm are encoded in old settings, pre [v20211104](https://github.com/Nandaka/PixivUtil2/releases/tag/v20211104)
- [A] Follow Pixiv users
  - Follows/Unfollows Pixiv users using PixivUtil2's exported member list. Or any ID list formatted the same way. Add IDs to `follow_pixiv_users_list.txt`
- [B] Bookmark artworks
  - Add/Delete artworks to bookmarks using artworks ID list in the same format as PixivUtil2's exported member list Add IDs to `bookmark_artworks_list.txt`
