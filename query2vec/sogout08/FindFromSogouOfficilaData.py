doc2url = dict()
for l in open('log.txt').readlines():
    segs = l.strip().split(' ')
    flag = segs[0]
    id = segs[1]
    doc2url[id] = 'UNFOUND'

result = open('/home/cluo/publicdata/try/id2url.link')

for l in result.readlines():
    segs = l.strip().split('\t')
    doc2url[segs[0]] = segs[1]

matchout = open('../data/doc2id.match.official','w')
count = 0
for l in open('log.txt').readlines():
    count +=1
    print 'match',count
    segs = l.strip().split(' ')
    flag = segs[0]
    id = segs[1]
    matchout.write(flag+'\t'+id+'\t')
    matchout.write(doc2url[id]+'\n')
matchout.close()