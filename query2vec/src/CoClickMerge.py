import os
count =0
files = os.listdir('../data/coclicktext')
fout = open('../data/coclickmerge.dat','w')
for f in files:
	print f,count
	count +=1
	for l in open('../data/coclicktext/'+f).readlines():
		fout.write(l)
fout.close()
