#coding=cp936

import os
files = os.listdir('/data2011/d3/uigs/2012/201203')

fout = open('runall.sh','w')
for f in files:
    
    fout.write('nohup python extractquerylog.py '+f+' > ../data/log/'+f+'.log &\n')
fout.close()
