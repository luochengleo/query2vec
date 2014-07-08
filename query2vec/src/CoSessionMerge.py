#coding=cp936
import os
count =0
files = os.listdir('../data/sessiontext')
fout = open('../data/cosession.dat','w')
def clearQuery(query):
	for symbol in [',','.','，','。','?','？','+',' ']:
		query = query.replace(symbol,'')
	return query
for f in files:
	
	print f,count
	count +=1
	for l in open('../data/sessiontext/'+f).readlines():
		segs = l.strip().split(' ')
		if len(segs) >20:
			continue
		qset = set()
		for s in segs:
			if s != '':
				qset.add(clearQuery(s))
		if len(qset)>1:
			fout.write(l.strip()+'\n')
fout.close()
