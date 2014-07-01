infile = '/home/cluo/publicdata/2012010203/folded/folded.dat'

outpath = '/home/cluo/publicdata/2012010203/hashbyu/'

fin = open(infile)
line = fin.readline()

data= dict()
count = dict()
for i in range(0,1024,1):
    data[i]=list()
    count[i] = 0

while line !='':
    segs = line.strip().split(' ')
    if len(segs) == 3:
        query =segs[0]
        url = segs[1]
        times = segs[2]
        mod =  url.__hash__()%1024
        data[mod].append(line)
        count[mod]+=1
        
        if count[mod]>=10000:
            count[mod]=0
            fout = open(outpath+str(mod)+'.dat','a')
            for item in data[mod]:
                fout.write(item)
            data[mod] = list()
    line = fin.readline()
                
                
