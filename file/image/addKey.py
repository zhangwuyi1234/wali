

from pymongo import *

client = MongoClient("localhost", 27017)
db = client.share

images=db.code.find({'flag':0})
k=0
for i in images:
#    if k==10:
#        break

    code=i['code']
    #code1=code+"20171106"
    #db.image.insert({'fileName':code1,'flag':0})
