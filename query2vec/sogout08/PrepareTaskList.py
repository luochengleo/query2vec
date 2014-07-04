
fout = open('../ref/imine11.cn','w')
for l in open('../ref/docs.txt').readlines():
    fout.write('0201 0 '+l.strip()+' 20 0.634130796362478 0\n')
fout.close()