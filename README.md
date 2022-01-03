# Check CRDS files

This repository contains scripts to check if the lists of files in different locations are the same. It was initially created to check files from Cavity Ring-Down Spectrometers (CRDS), but it can be applied to any set of files.

## Main scripts

The script [`create-count-files.py`](create-count-files.py) outputs a file with a list of the number of lines and the name of each file in a given location.

The script [`check-count-files.py`](check-count-files.py) reads two files created with [`create-count-files.py`](create-count-files.py) and checks if they are the same. In other words, if both locations have the same list of files with the same size (number of lines).

The scripts:
- check the length of both lists.
- check if both lists with the same length have the same file names.
- check if both lists with the same length and the same file names also have the same number of lines for each file.

Be aware all scripts consider a structure of subfolders and files with extension .dat

```python
glob.iglob(path + '**/*.dat', recursive=True)
```

## Alternative scripts

[`check-files.py`](check-files.py) is an alternative script that checks only if the lists of files in different locations are the same, but does not check the size (number of lines).

[`create-count-files-input.py.py`](create-count-files-input.py) is an alternative script that outputs a file with a list of the number of lines and the name of each file in a given location using the input of the user to define the path of the files and the name of the output file.
