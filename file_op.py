import os, shutil
import re

#trainFile = open('train.txt', 'w')
testFile = open('testall.txt', 'w')
path = 'allsketch'
files = os.listdir(path)

for f in files:
    name = f.split('.')[0]
    newname = name.zfill(5)
    newf = newname + '.png'
    os.rename(os.path.join(path, f), os.path.join(path, newf))

print('complete renaming\n')
files = os.listdir(path)
files.sort()

for i, f in enumerate(files):
    #label = re.findall("\d+", f)[0]
    label = f.split('.')[0]
    label = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", label)
    testFile.write(f + ' ' + str(i) + '\n')
    if i % 100 == 0:
        print('complete %d sketches.\n' % i)

testFile.close()
