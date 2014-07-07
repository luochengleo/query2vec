fout = open('run.sh','w')

for i in range(0,32,1):
    if i <10:
        num = '0'+str(i)
    else:
        num = str(i)
    fout.write('nohup python FindMoreWebPages.py '+num+' > '+num+'.log & \n')