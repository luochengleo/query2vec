
doc2url = dict()
# 20dab857d4b6462b-fc09de91451034f0
errorout = open('../data/mergedoc2url.error','w')
for i in range(0,24,1):
    print i
    fin = open('../data/sogoutdoc2id/'+str(i)+'.stat')
    for l in fin.readlines():
        segs = l.strip().split('\t')
        if len(segs) ==2:
            if len(segs[0]) == len('20dab857d4b6462b-fc09de91451034f0'):
                doc2url[segs[0]] = segs[1]
            else:
                errorout.write(l)
        else:
            errorout.write(l)
            
result = open('../data/sogoutdoc2id/merge.txt','w')
for item in doc2url:
    result.write(item+'\t'+doc2url[item]+'\t')

matchout = open('../data/doc2id.match','w')
count = 0
for l in open('log.txt').readlines():
    count +=1
    print 'match',count
    segs = l.strip().split('\t')
    flag = segs[0]
    id = segs[1]
    matchout.write(flag+'\t'+id+'\t')
    if id in doc2url.keys():
        matchout.write(doc2url[id]+'\n')
    else:
        matchout.write('NOTFOUND\n')
matchout.close()
    