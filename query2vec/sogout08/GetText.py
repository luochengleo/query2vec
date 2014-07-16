from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os

count =1
for f in os.listdir('../data/sogout08ready'):
    
    count +=1
    fout = open('../data/sogouttext/'+f.replace('.html','.txt'),'w')

    try:
        soup = BeautifulSoup(open('../data/sogout08ready/'+f).read())
        text = soup.get_text()
        for l in text.split('\n'):
            if l.strip() != '':
                fout.write(l+'\n')
        fout.write(text)
    except:
        print count,f
        print "EXCEPT"
        fout.write(open('../data/sogout08ready/'+f).read())
    fout.close()