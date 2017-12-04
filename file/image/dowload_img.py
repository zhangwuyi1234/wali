# -*- coding: utf-8 -*-

import os
from pymongo import *
import qiniuTools as qb
import backup.upMongo as upMongo

client = MongoClient("localhost", 27017)
db = client.share
collection = db.code

if __name__ == "__main__":
    import hash.hashTools as ht
    
    count=db.image.count({"flag":1,"output":{ '$ne' : -2 }})
    print(count)
    #count=4000
    k=0
    for i in range(count):
        i=i+1
        image=db.image.find({"flag":1,"output":{ '$ne' : -2 }}).skip(k).limit(i)
        k=i
        output=str(image[0]['output'])
        fileName=str(image[0]['fileName'])
        path="/data/image/"+output+'_'+fileName+".png"
        isExists=os.path.exists(path)
        flag=1
        if not isExists:
            try:
                qb.dowImage(fileName,path)
                flag=2
                #db.image.update({'flag':1,'fileName':fileName},{'$set':{'flag':2}})
            except BaseException as inst:
                print("dowImageError")
                flag=-1
                #db.image.update({'flag':1,'fileName':fileName},{'$set':{'flag':-1}})
        if os.path.exists(path):
            strenHash=ht.enHash(path)
            print(strenHash)
            db.image.update({'flag':1,'fileName':fileName},{'$set':{'flag':flag,'enHash':strenHash}})
    upMongo.upShare()
