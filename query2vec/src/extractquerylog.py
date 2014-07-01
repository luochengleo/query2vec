import os
import re
import sys


import urllib
from datetime import datetime
import threading

dirname = sys.argv[1]

hit = 0
inpath = '/data2011/d3/uigs/2012/201203/' + dirname
outfile = '../data/querylog/' + dirname + '.dat'
files = os.listdir(inpath)
fout = open(outfile, 'w')
fcount = 0
for file in files:
    fcount +=1
    print dirname,hit,str(fcount)+'/'+str(len(files))
    if file.endswith("7z"):
        f = inpath + "/" + file
        datacontent = os.popen("7z e -so " + f)
        line = datacontent.readline()
        while line != '':
            uid = re.compile(r'(?<=uigs_cookie=SUID%)(\S{34})')
            uuid = uid.search(line)
            if uuid:
                uuid = uuid.groups()[0]
                qr = re.compile(r'(?<=query=)(.*?)(?=&rn)')
                tm = re.compile(r'\[(.*?)\]')
                querys = qr.search(line)
                if querys:
                    query = urllib.unquote(urllib.unquote(querys.groups()[0])).replace('+', '')
                    times = tm.search(line)
                    if times :
                        times = times.groups()[0]
                        if query !=''  and uuid !='':
                            try:
                                tm = times.split(' ')[1].split(':')[1]
                                fout.write(query  +'\t'+uuid+'\t'+tm+ '\n')
                            except:
                                pass
            line = datacontent.readline()
fout.close()
