import os

count = 0
with open('deletables.txt', 'r') as deletables_file:
    for deletable in deletables_file.readlines():
        deletable = deletable.split('\n')[0]
        count += 1
        print(count, deletable)
        if os.path.exists(deletable):
            os.remove(deletable)
