# jdFileSystemPythonScript
A python script that makes the skeleton of a Johnny Decimal file system!

Here is the reference: https://johnnydecimal.com/ It's not a bad idea in my opinion. 

If you feel my intepretation of this material is not correct or other suggestions - let me know!

Thanks, hopefully this saves you some time.

## How does it work?
1. Input the directory (empty directory) where you will want to create your JD filesystem into `dire`
2. Creates the 10 area folders
3. Creates 10 category folders within each area folder (sequentially ordered 00-99)
4. Creates 10 ID folders within each category folder occupying .00 - .09 of each ID establishing the management IDs of (index, inbox, wip, todo, bookmarks, templates, blank, blank, someday, archive)
5. Creates a text based tree map of the entire system and stores it in /00-09/00/00.00_index/index.txt
