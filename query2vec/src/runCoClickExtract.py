for i in range(0,1024,1):
	fout = open('runCoclick2Text'+str(i%20)+'.sh','a')
	fout.write('python CoClickExtract.py '+str(i)+' \n')
	fout.close()

fout = open('runall.sh','w')
for i in range(0,20,1):
	fout.write('nohup sh runCoclick2Text'+str(i)+'.sh > ../data/log/'+str(i)+'.log &\n')
fout.close()
