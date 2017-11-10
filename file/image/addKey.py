

from pymongo import *

client = MongoClient("localhost", 27017)
db = client.share

images=db.code.find({'flag':0})
k=0
for i in images:
#    if k==10:
#        break

    code=i['code']
    code1=code+"20171106"
    code2=code+"20171107"
    code3=code+"20171108"
    code4=code+"20171109"
    code5=code+"20171110"
    db.image.insert({'fileName':code1,'flag':0})
    db.image.insert({'fileName':code2,'flag':0})
    db.image.insert({'fileName':code3,'flag':0})
    db.image.insert({'fileName':code4,'flag':0})
    db.image.insert({'fileName':code5,'flag':0})
