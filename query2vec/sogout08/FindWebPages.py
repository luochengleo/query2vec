#coding=cp936
import os
docs  = set()

for l in open('../ref/docs.txt').readlines():
    docs.add(l.strip())
    print l.strip()

print len(docs),' docs need to find'
    
files = os.listdir('/work/caoyj/SogouT')
for f in files:
    if '.7z' in f:
        doccount =0
        datacontent = os.popen('7z e -so /work/caoyj/SogouT/'+f)
        l  = datacontent.readline()
        
        write = False
        fout = open('../data/temp.txt','w')
        while l !='':
            if write==True:
                fout.write(l)
                if '</DOC>' in l:
                    write=False
            else:
                if '<DOCNO>' in l :
                    doccount +=1
                    docno = l.strip().replace('<DOCNO>','').replace('</DOCNO>','')
                    print docno
                    if docno in docs:
                        print f,doccount,docno
                        fout = open('../data/page/'+docno+'.html','w')
                        fout.write('<DOC>\n')
                        fout.write(l)
                        write = True
                
            l = datacontent.readline()
            
                
            