#coding=cp936

import os
files = os.listdir('/data2011/d3/uigs/2012/201204')

fout = open('runall.sh','w')
for f in files:
    fout.write('python Data2Session.py '+f+'\n')
fout.close()
