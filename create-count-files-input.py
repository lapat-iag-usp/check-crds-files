import os
import glob

path = input("Enter files path: ")
output_file = input("Enter output file name: ")

with open(output_file, 'w') as out:
    filenames = [filename for filename in glob.iglob(path + '**/*.dat', recursive=True)]
    filenames.sort()
    for filename in filenames:
        with open(filename, 'r') as f:
            count = sum(1 for line in f)
            out.write('{c} {f}\n'.format(c=count, f=os.path.basename(filename)))
