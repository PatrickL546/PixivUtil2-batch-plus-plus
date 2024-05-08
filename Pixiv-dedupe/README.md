# About The Project

A python script to deal with Pixiv folder duplicates

## Requirements

- Windows PC
- Python 3.8.0+ (https://www.python.org/)
- Additional library listed in requirements.txt

## Notes

### Assumptions

- Your Pixiv folders looks like this: `PixivUserName (12345)`
- And Fanbox folders looks like this: `FANBOX FanboxUserName (12345)`

The final folders will look like this for Pixiv: `(12345)` and Fanbox: `FANBOX (12345)`

Going forward, it is advised to remove `%artist%` from below to avoid making new folders if the artist changes their name

        [Filename]
        filenameFormat = %artist% (%member_id%)\%urlFilename% - %title%
        filenameMangaFormat = %artist% (%member_id%)\%urlFilename% - %title%
        filenameInfoFormat = %artist% (%member_id%)\%urlFilename% - %title%
        filenameMangaInfoFormat = %artist% (%member_id%)\%urlFilename% - %title%
        filenameSeriesJSON = %artist% (%member_id%)\%manga_series_id% - %manga_series_title%
        filenameFormatSketch = %artist% (%member_id%)\%urlFilename% - %title%
        filenameFormatNovel = %artist% (%member_id%)\%manga_series_id% %manga_series_order% %urlFilename% - %title%

        [FANBOX]
        filenameFormatFanboxCover = FANBOX %artist% (%member_id%)\%urlFilename% - %title%
        filenameFormatFanboxContent = FANBOX %artist% (%member_id%)\%urlFilename% - %title%
        filenameFormatFanboxInfo = FANBOX %artist% (%member_id%)\%urlFilename% - %title%

## Usage

- Run `Pixiv dedupe.py`
- Use option [6] to rename your Pixiv folders
- Then [1] to get hash of all files
- Then [7] to move non-duplicate files to new folders
- Finally [8] so you can delete all the duplicate folders
- All other options are not needed, I probably used them for debugging

### Menu

            Hash Functions                          Folder Functions

    [1] Get hash                             [6] Rename Pixiv folders
    [2] Get hash duplicate and unique        [7] Move files to new folders
    [3] Get hash difference                  [8] Move 'old_' folders to a separate folder
    [4] Sort hash by hash                    [9] Get Pixiv folder list and Pixiv ID
    [5] Sort hash by Pixiv ID

    Press [CTRL + C] to exit functions
    Enter [Q] to Quit

- [1] Get hash
  - uses Blake3 for hashing
- [6] Rename Pixiv folders
  - append 'old_' to Pixiv folders
- [7] Move files to new folders
  - Files that are left behind are files that have the same filename and hash
  - Files that have the same name but different hash are kept with a timestamp appended

## Credits/Contributor

- PatrickL546 (I can't code, what I write will be bad)

## License

Distributed under the BSD 2-Clause "Simplified" License. See `LICENSE` for more information.
