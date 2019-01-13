import os
from pprint import pprint

dirs = [
    '/Volumes/G-DRIVE mobile USB/photos_only/iPhoto Library/Masters',
    '/Volumes/G-DRIVE mobile USB/photos_only/iPhoto Library 1/Masters',
    '/Volumes/G-DRIVE mobile USB/photos_only/imac/imac Photos Library/Masters',
    '/Volumes/G-DRIVE mobile USB/photos_only/imac/Photos Library 2/Masters',
]
output_dir = '/Volumes/G-DRIVE mobile USB/photos'

for dir in dirs:
    if dir[-1] != os.sep:
        dir = dir + os.sep
    for root, subdir, files in os.walk(dir):
        for file in files:
            if file[0] != '.':
                frompath = os.path.join(root, file)
                relpath = frompath.replace(dir, '')
                topath = os.path.join(output_dir, relpath)
                todir = os.path.split(topath)[0]
                if not os.path.exists(todir):
                    os.makedirs(todir)
                os.rename(frompath, topath)
