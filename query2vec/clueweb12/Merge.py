import os
import shutil

fromnet = os.listdir('../data/clueweb12/imagefromnet')
fromlocal = os.listdir('../data/clueweb12/imagefromlocal')
all = set()
for item in fromnet:
    all.add(item)
for item in fromlocal:
    all.add(item)
    
for item in all:
    sizenet = 0
    sizelocal = 0
    if item in fromnet:
        sizenet = os.path.getsize('../data/clueweb12/imagefromnet/'+item)
    if item in fromlocal:
        sizelocal = os.path.getsize('../data/clueweb12/imagefromlocal/'+item)
    if sizenet > sizelocal:
        shutil.copy("../data/clueweb12/imagefromnet/"+item,'../data/clueweb12/merge/'+item)
#         imgout = open(' ../data/clueweb12/merge/'+item,'wb')
#         imgin = open("copy ../data/clueweb12/imagefromnet/"+item,'rb')
#         imgout.write(imgin.read())
#         imgout.close()
#         imgin.close()
        print 'NET',item
    if sizenet < sizelocal:
        shutil.copy("../data/clueweb12/imagefromlocal/"+item,'../data/clueweb12/merge/'+item)
#         imgout = open(' ../data/clueweb12/merge/'+item,'wb')
#         imgin = open("copy ../data/clueweb12/imagefromlocal/"+item,'rb')
#         imgout.write(imgin.read())
#         imgout.close()
#         imgin.close()
        print 'LOCAL',item