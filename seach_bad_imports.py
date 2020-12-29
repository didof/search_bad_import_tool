# get folder
# include folders (src, repo, styles)
# for any js and jsx look import, if find 'repo/itsart' replace with 'Repos/' (alert)
# for any scss, if find 'repo/itsart' replace with 'repo/chili' (alert)

from os import listdir
from os.path import isfile, join, isdir

alertcolor = '\u001b[31m'
endcolor = '\u001b[0m'

def getonlyfiles(path, extensions = ['js', 'jsx', 'scss'], include_dotfiles = False, excludedfolders = ['node_modules', 'dist', '__tests__', '__tests_utils__', '__mocks__']):
    print('searching only: ', ' '.join(extensions))
    print('include dotfiles: ', include_dotfiles)
    print('excluding folders: ', ' '.join(excludedfolders))
    
    filesPaths = []

    def hasvalidextension(file_path):
        output = False
        for ext in extensions:
            if file_path.endswith(f'.{ext}'):
                output = True
        return output

    def shouldbeexcluded(file_path):
        output = False
        for folder in excludedfolders:
            if file_path.endswith(folder):
                output = True
        return output


    def operateonfolder(folderpath):
        for file in listdir(folderpath):

            if not include_dotfiles and file.startswith('.'):
                print(f'excluding {join(folderpath, file)}')
                continue

            file_path = join(folderpath, file)

            if shouldbeexcluded(file_path):
                print(f'excluding {file_path}')
                continue

            if isfile(file_path) and hasvalidextension(file_path):
                filesPaths.append(file_path)
            elif isdir(file_path):
                operateonfolder(file_path)

    operateonfolder(path)
    
    return filesPaths

def shunt(file_list, trigger):
    for file in file_list:
        if file.endswith('.js') or file.endswith('.jsx'):
            check(file, trigger)
        elif file.endswith('.scss'):
            check(file, trigger, '@')
    
def check(file_path, trigger, prefix = ''):
    badimports = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for row, line in enumerate(lines):
            if f'{prefix}import' in line and trigger in line:
                badimports.append(str(row + 1))
    
    strbadimports = ' '.join(badimports)
    if len(badimports) >= 1:
        print(f'{alertcolor}bad import in {file_path} at row {strbadimports}{endcolor}')

def search_bad_imports(dirpath, triggerstring):
    print('searching in: ', dirpath)
    filespaths = getonlyfiles(dirpath)
    shunt(filespaths, triggerstring)

target = '/home/fdidonato/chili/chili-website'
trigger = 'repo/itsart'

search_bad_imports(target, trigger)
