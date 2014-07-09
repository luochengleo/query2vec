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
            type = ''
            if 'GET /pv.gif' in line:
                type = 'P'
            if 'GET /cl.gif' in line:
                type = 'C'
            
            uid = re.compile(r'(?<=uigs_cookie=SUID%)(\S{34})')
            uuids = uid.search(line)
            uuid = ''
            if uuids:
                uuid = uuid.groups()[0]

            qr = re.compile(r'(?<=query=)(.*?)(?=&rn)')
            querys = qr.search(line)
            query = ''
            if querys:
                query = urllib.unquote(urllib.unquote(querys.groups()[0])).replace('+', '')
            
            tm = re.compile(r'\[(.*?)\]')    
            times = tm.search(line)
            time = ''
            if times :
                time = times.groups()[0]
            
            u = re.compile('(?<=href%3D)(.*?)(?=&txt)')
            urls = u.search(line)
            url = ''
            if urls:
                url = url.groups()[0]
            
            
            line = datacontent.readline()
fout.close()
