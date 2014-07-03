import os
import sys
inpath = '/home/cluo/publicdata/2012010203/hashbyu'

no = sys.argv[1]
print no,1024
urls = dict()
infile = inpath+'/'+no+'.dat'
lines = open(infile).readlines()
for l in lines:
	segs = l.strip().split(' ')
	if len(segs)==3:
		query = segs[0]
		url = segs[1]
		urls[url] = set()

for l in lines:
	segs = l.strip().split(' ')
	if len(segs)==3:
		query = segs[0]
		url = segs[1]
		urls[url].add(query)

fout = open('../data/coclicktext/'+no+'.dat','w')
for k in urls.keys():
	l = list(urls[k])
	if len(l) >1:
		for item in l:
			fout.write(item+' ')
		fout.write('\n')
fout.close()
