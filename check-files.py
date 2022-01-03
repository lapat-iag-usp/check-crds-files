import os
import glob

path_base = 'path-of-the-files-base/'
filenames_base = [os.path.basename(filename) for filename in glob.iglob(path_base + '**/*.dat', recursive=True)]
filenames_base.sort()

path = 'path-of-the-files-comparison/'
filenames = [os.path.basename(filename) for filename in glob.iglob(path + '**/*.dat', recursive=True)]
filenames.sort()

if len(filenames_base) == len(filenames):
    if len(list(set(filenames) - set(filenames_base))) == 0:
        print(f'Both lists have the same length and the same file names')
    else:
        print(f'Both lists have the same length but NOT the same file names')
        print(f'Files missing in the base list: {list(set(filenames) - set(filenames_base))}')
        print(f'Files missing in the comparison list: {list(set(filenames_base) - set(filenames))}')
else:
    print(f'The lists do NOT have the same length')
    print(f'Files missing in the base list: {list(set(filenames) - set(filenames_base))}')
    print(f'Files missing in the comparison list: {list(set(filenames_base) - set(filenames))}')
