import warc
import sys
import os


folderidx =sys.argv[1]

foldername = '/home/cluo/publicdata/DiskB/ClueWeb12_'+folderidx
pages = set()
for l in open('../ref/enpages.txt').readlines():
    pages.add(l.strip())


for folder in os.listdir(foldername):
    subfoldername = foldername+'/'+folder
    for filename in os.listdir(subfoldername):
        print subfoldername,filename
        os.system('7z e '+subfoldername+'/'+filename)
        warcfilename = filename.replace('.7z','')
        f = warc.open(warcfilename)
    
        for record in f:
            id = record.header.get('WARC-TREC-ID')
            if id in pages:
                fout = open('../data/parse/'+str(record.header.get('WARC-TREC-ID')+'.html'),'w')
                content = record.payload.read()
                write = False
                for l in content.split('\n'):
                    if '<!DOCTYPE' in l:
                        write=True
                    if write == True:
                        fout.write(l+'\n')
                fout.write(content)
                fout.close()
        os.system('rm '+warcfilename)
