#coding=cp936
import os
import sys

docs  = set()

mod = int(sys.argv[1])


for l in open('../ref/docs.txt').readlines():
    docs.add(l.strip())
    print l.strip()

print len(docs),' docs need to find'

files = os.listdir('/home/cluo/publicdata/sogout08/')

for f in files:
    if '.7z' in f:
        idx = int(f.split('.')[1])
        if idx%32==mod:
            doccount =0
            datacontent = os.popen('7za e -so /home/cluo/publicdata/sogout08/'+f)
            l  = datacontent.readline()
            
            write = False
            fout = open('../data/temp.txt','w')
            count = 0
            while l !='':
                count +=1
                if '-' in l:
                    for item  in docs:
                        if item in l:
                            fout = open('../data/count/'+str(mod)+'.count','a')
                            fout.write('Find '+ item +' in the '+str(count)+ ' file '+f+'\n')
                            fout.close()
                l = datacontent.readline()

            
                
            