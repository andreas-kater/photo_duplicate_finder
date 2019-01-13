import os
import pickle
from pprint import pprint

directories = [
    '/Volumes/G-DRIVE mobile USB/iPhoto Library/Masters',
    '/Volumes/G-DRIVE mobile USB/iPhoto Library 1/Masters',
    '/Volumes/G-DRIVE mobile USB/imac/Photos Library 2.photoslibrary/Masters',
    '/Volumes/G-DRIVE mobile USB/imac/imac Photos Library.photoslibrary/Masters'
]


def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    # return total_size/1073741824
    return total_size/1000000000


grand_total = 0
for dir in directories:
    size = get_size(dir)
    print(size)
    grand_total += size
print(grand_total)

