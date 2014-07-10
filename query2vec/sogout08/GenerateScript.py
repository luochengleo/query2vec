import os

count = 0

for f in os.listdir('../data/sogout08ready/'):
    fout = open('../data/start'+str(count %16)+'.bat','a')
    count +=1
    #
    if '.html' in f:
#          
        fout.write('wkhtmltoimage --width 800 --height 2000 --username thuir --password beibeiAllTheWay --quiet --load-error-handling ignore --quality 70 ./sogout08ready/'+f+' '+'./sogoutlimited/'+f+'.png'+' \n')
    fout.close()

fout= open('../data/start.bat','w')
for i in range(0,16,1):
    fout.write('start start'+str(i)+'.bat \n')
fout.close()

