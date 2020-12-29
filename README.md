# SEARCH BAD IMPORT TOOL

## WHAT IT DOES
This simple script reads recursively all the files/folders in the folder specified as `target`, filters out the files not interested. Then runs a check in the imports of the files looking for a trigger string. It just makes an alert in the console.

## HOW TO USE
1. clone file in local
2. update `target` with the path to your folder
3. run `python3 search_bad_imports.py` and read console

*optional*: update the main function second argument to a different trigger string (default to 'repo/itsart')
