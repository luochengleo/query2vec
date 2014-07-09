import os

files1 = os.listdir('../data/exist/')
files2 = os.listdir('../data/page/')


allid = set()
for l in open('../ref/docs.txt').readlines():
    allid.add(l.strip())
print len(allid)
count = len(allid)

fout = open('../data/log.txt','w')
for l in allid:
    if l.strip()+'.dhtml' in files1:
        open('../data/fromexist/'+l.strip()+'.html','w').write(open('../data/exist/'+l.strip()+'.dhtml').read())
        count -=1
        fout.write('F '+l+'\n')
        continue
    if l.strip()+'.html' in files2:
        open('../data/fromexist/'+l.strip()+'.html','w').write(open('../data/page/'+l.strip()+'.html').read())
        count -=1
        fout.write('F '+l+'\n')
        continue
    fout.write('N '+l+'\n')
print count
