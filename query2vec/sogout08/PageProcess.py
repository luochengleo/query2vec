from bs4 import BeautifulSoup

import os
import re
# os.mkdir('../data/localpage2')

all = 0
has = 0

def translate(lt, url):
    if 'http' in url:
        return url
    topurl = lt[0]+'//'+lt[2]
    if url[0:2] == '//':
        return topurl+url[1:]
    if url[0] == '/':
        return topurl +url  
    if url[0].isalpha():
        return topurl + '/'+url
    if url[0].isaphpa == '':
        return ''
    
    return url
        
for f in os.listdir('../data/fromexist'):
    all += 1
    print all
    content = open('../data/fromexist/'+f).readlines()
    html = content[3:len(content)-1]
    docid = content[1][7:40]
    url = content[2][5:len(content[2])-7]
    
    segs = url.split('/')
    topurl = segs[0]+'//'+segs[2]
    newcontent = ''
    for l in html:
        newcontent = newcontent +'\n'+l
    
    scriptpat = re.compile(r'<script.*?</script>',re.S)
    new = re.sub(scriptpat,'',newcontent)
    fout = open('../data/sogout08ready/'+f,'w')
    try:
        soup = BeautifulSoup(new)
        try:
            for img in soup.find_all('img'):
                if 'src' in img.attrs:
                    img['src'] = translate(segs,img['src'])
        except:
            print all,f,'REPLACE Except'
        
        
        
        write = False
        fout.write(soup.prettify())
    except:
        print all,f,'SOUP Except'
        fout.write(new)
    fout.close()
