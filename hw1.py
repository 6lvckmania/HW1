import os, sys

path = os.path.join(os.path.expanduser('~'), sys.argv[1])
prefix = sys.argv[2] #folder name
counts = sys.argv[3] #counts of users
mode = sys.argv[4] #permisions mode

for i in range (1, int(counts) + 1):
    usrpath = os.path.join(path, prefix + str(i))
    os.makedirs(usrpath, int(mode))
print('Result: '+ counts +' user(s) with permissions mode ' + mode + ' was(were) created.\nPath: ' + path)
   
