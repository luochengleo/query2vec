import re
pattern = re.compile(r'<DOCNO>(.*?)</DOCNO>(.*?)<URL>(.*?)</URL>',re.S)



datacontent = open('../data/SogouT.mini.txt')
l  = datacontent.readline()
while l !='':
    if '<DOC>' in l:
        content = l
        content += datacontent.readline()
        content += datacontent.readline()
        m = pattern.search(content)
        if m :
            print m.group(1)
            print m.group(3)
        else:
            print 'error'
            print content
    l = datacontent.readline()