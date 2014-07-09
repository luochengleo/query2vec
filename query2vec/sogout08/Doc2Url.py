#coding=cp936
import os
import sys
import re
docs  = set()
mod = int(sys.argv[1])
for l in open('../ref/docs.txt').readlines():
    docs.add(l.strip())
    print l.strip()

print len(docs),' docs need to find'
files = os.listdir('/home/cluo/publicdata/sogout08/')

fout = open('../data/sogoutdoc2id/'+str(mod)+'.stat','w')

pattern = re.compile(r'<DOCNO>(.*?)</DOCNO>(.*?)<URL>(.*?)</URL>',re.S)
for f in files:
    if '.7z' in f:
        idx = int(f.__hash__())
        if idx%24==mod:
            doccount =0
            datacontent = os.popen('7za e -so /home/cluo/publicdata/sogout08/'+f)
            content = ''
            l  = datacontent.readline()
            while l !='':
                if '<DOC>' in l:
                    content = l
                    content += l.readline()
                    content += l.readline()
                    m = pattern.search(content)
                    if m :
                        fout.write(m.group(1)+'\t'+m.group(3)+'\n')
                    else:
                        fout.write('ERROR\t' + content.replace('\r','').replace('\n',''))
                l = datacontent.readline()