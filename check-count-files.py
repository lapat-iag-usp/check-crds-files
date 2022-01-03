import pandas as pd

file_base = 'name-of-the-file-base.txt'
df_base = pd.read_csv(file_base, sep=' ', header=None, names=['count', 'name'])
counts_base = list(df_base['count'])
names_base = list(df_base['name'])

file = 'name-of-the-file-comparison.txt'
df = pd.read_csv(file, sep=' ', header=None, names=['count', 'name'])
counts = list(df['count'])
names = list(df['name'])

if len(names) == len(names_base):
    if len(list(set(names) - set(names_base))) == 0:
        print(f'Both lists have the same length and the same file names')
        for i in range(len(counts_base)):
            if counts_base[i] != counts[i]:
                print(f'{names_base[i]} from base list has {counts_base[i]} and '
                      f'{names[i]} from comparison list has {counts[i]}')
    else:
        print(f'Both lists have the same length but NOT the same file names')
        print(f'Files missing in the base list: {list(set(names) - set(names_base))}')
        print(f'Files missing in the comparison list: {list(set(names_base) - set(names))}')
else:
    print(f'The lists do NOT have the same length')
    print(f'Files missing in the base list: {list(set(names) - set(names_base))}')
    print(f'Files missing in the comparison list: {list(set(names_base) - set(names))}')
