import sys


fin = open('../data/querylog/'+sys.argv[1]+'.dat')
line = fin.readline()
count = 0
currtime = 0
dataOfSession = dict()
while line != '':
    count +=1
    if count %10000000==0:
        print count
    try:
        segs = line.strip().split('\t')
        if len(segs) ==3:
            query = segs[0]
            sessionid= segs[1]
            dataOfSession[sessionid] = list()
    except:
        print line
    
    line = fin.readline()
fin.close()


def session2text(lt):
    text = ''
    count = 0
    for (q,s,t) in lt:
        if 'C@' in q:
            pass
        if 'P@' in q:
            text = text+' '+q
            count +=1
    if count >0:
        return text+'\n'
    else:
        return ''


fin = open('../data/querylog/'+sys.argv[1]+'.dat')
fout = open('../data/sessiontextwithouturl/'+sys.argv[1]+'.txt','w')
line = fin.readline()
count = 0
currtime = 0
while line != '':
    count +=1
    if count %1000000==0:
        print float(count)/160000000.0,' clear'
        for k in dataOfSession.keys():
            existData = dataOfSession[k]
            if len(existData)>0:
                existTime = existData[-1][2]
                if currtime - existTime > 1800.0:
                    fout.write(session2text(existData))
                    dataOfSession[k] = list()
    segs = line.strip().split('\t')
    if len(segs) ==3:
        query = segs[0]
        sessionid= segs[1]
        time = float(segs[2])
        currtime = time
        existData = dataOfSession[sessionid]
        if len(existData)>0:
            existTime = existData[-1][2]
            if currtime - existTime > 1800.0:
                fout.write(session2text(existData))
                dataOfSession[sessionid] = list()
                dataOfSession[sessionid].append((query,sessionid,time))
            else:
                dataOfSession[sessionid].append((query,sessionid,time))
        if len(existData) == 0:
            dataOfSession[sessionid].append((query,sessionid,time))
    
    line = fin.readline()
fin.close()

for k in dataOfSession.keys():
    existData = dataOfSession[k]
    if len(existData)>0:
        fout.write(session2text(existData))
        dataOfSession[k] = list()
fout.close()