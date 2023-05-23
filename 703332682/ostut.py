import os
start='.' # here . refers to the current directory
excluded_dirs = ['hell']
f=0
for current, dir, filenames in os.walk(start):
    #print('Path:',path)
    print(current)
    print(dir)
    print(filenames)
    print(f)
    f+=1
    #print('Files:', filenameṇs)
