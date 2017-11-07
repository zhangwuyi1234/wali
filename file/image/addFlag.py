

from pymongo import *
import getData as gd

client = MongoClient("localhost", 27017)
db = client.share

images=db.image.find({'flag':0})
k=0
for i in images:
#    if k==10:
#        break

    fileName=i['fileName']
    code=fileName[0:6]
    time=fileName[6:]
   
    re=gd.forCode(code,time)
    db.image.update({'fileName':fileName},{'$set':{'output':re,'flag':1}})
    
    print(code+"__"+time+"__"+str(re))
#    k=k+1

#db.image.update({},{$unset:{"output":""}},{multi:true})
