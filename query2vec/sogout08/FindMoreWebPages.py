#coding=cp936
import os
import sys

docs  = set()

mod = int(sys.argv[1])


for l in open('../ref/docs.txt').readlines():
    docs.add(l.strip())
    print l.strip()

print len(docs),' docs need to find'
    
files = os.listdir('/work/caoyj/SogouT')
for f in files:
    if '.7z' in f:
        idx = int(f.split('.')[1])
        if idx%12==mod:
            doccount =0
            datacontent = os.popen('7za e -so /work/caoyj/SogouT/'+f)
            l  = datacontent.readline()
            
            write = False
            fout = open('../data/temp.txt','w')
            while l !='':
                if write==True:
                    fout.write(l)
                if '</DOC>' in l:
                        write=False
                if '<DOCNO>' in l :
                    doccount +=1
                    docno = l.strip().replace('<DOCNO>','').replace('</DOCNO>','')
                    if docno in docs:
                        print f,doccount,docno
                        fout = open('../data/page/'+docno+'.html','w')
                        fout.write('<DOC>\n')
                        fout.write(l)
                        write = True
                
                l = datacontent.readline()

            
                
            