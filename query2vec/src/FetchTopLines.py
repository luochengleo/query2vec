import sys
num = int(sys.argv[1])
infile = sys.argv[2]
outfile = sys.argv[3]

fin = open(infile)
fout = open(outfile,'w')
for i in range(0,num,1):
    fout.write(fin.readline())
