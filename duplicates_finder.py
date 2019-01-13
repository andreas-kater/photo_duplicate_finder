import itertools
import os
import pickle
from pprint import pprint


def compare(filepath1, filepath2):
    return open(filepath1, "rb").read() == open(filepath2, "rb").read()


directories = [
    '/Volumes/G-DRIVE mobile USB/iPhoto Library/Masters',
    '/Volumes/G-DRIVE mobile USB/iPhoto Library 1/Masters',
    '/Volumes/G-DRIVE mobile USB/imac/Photos Library 2.photoslibrary/Masters/',
    '/Volumes/G-DRIVE mobile USB/imac/imac Photos Library.photoslibrary/Masters/'
]
filelist = []
filedir = {}
duplicates = []
deletables = []
count = 0

for dir in directories:
    for root, subdir, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            filelist.append({
                'path': path,
                'size': size,
            })
            if size not in filedir.keys():
                filedir[size] = []
            filedir[size].append(path)
            count += 1
    print(count)
count = 0
print('Finished generating filedir dict')
filedir_length = len(filedir)
print('filelist length:', len(filelist))
print('filedir dict keys length:', len(filedir))
for size in filedir.keys():
    count += 1
    print(count, '/', filedir_length)
    if len(filedir[size]) > 1:
        repeats = []
        for combination in itertools.combinations(filedir[size], 2):
            if compare(*combination):
                if combination[0] not in repeats:
                    repeats.append(combination[0])
                if combination[1] not in repeats:
                    repeats.append(combination[1])
        if repeats:
            duplicates.append(repeats)
print('Finished generating duplicates list')
for duplicate_group in duplicates:
    if len(duplicate_group) > 1:
        for duplicate in duplicate_group[1:]:
            deletables.append(duplicate)
print('Finished generating deletables list')
with open('pickled_deletables', 'wb') as pickled_deletables_file:
    pickle.dump(deletables, pickled_deletables_file)
with open('deletables.txt', 'w') as deletables_file:
    for deletable in deletables:
        try:
            deletables_file.write(deletable + '\n')
        except:
            pass
