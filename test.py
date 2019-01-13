import os
import pickle
from pprint import pprint

# with open('pickled_deletables', 'rb') as file:
#     deletables = pickle.load(file)
#     pprint(deletables[:10])
#     print(len(deletables))

dir = '/Volumes/G-DRIVE mobile USB/imac/Photos Library2.photoslibrary/Masters'
dir = '/Volumes/G-DRIVE mobile USB/imac/Photos Library 2.photoslibrary/Masters/'
dir ='/Volumes/G-DRIVE mobile USB/imac/imac Photos Library.photoslibrary/Masters/'
for root, subdir, files in os.walk(dir):
    print(root)
    for file in files:
        print(os.path.join(root, file))
