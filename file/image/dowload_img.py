# -*- coding: utf-8 -*-

import os
from pymongo import *
import qiniuTools as qb

client = MongoClient("localhost", 27017)
db = client.share
collection = db.code

if __name__ == "__main__":
    count=db.image.count({"flag":1,"output":{ '$ne' : -2 }})
    print(count)
    count=2500
    k=0
    for i in range(count):
        i=i+1
        image=db.image.find({"flag":1,"output":{ '$ne' : -2 }}).skip(k).limit(i)
        k=i
        output=str(image[0]['output'])
        fileName=str(image[0]['fileName'])
        path="/data/image/"+output+'_'+fileName+".jpg"
        db.image.update({'flag':1,'fileName':fileName},{'$set':{'flag':2}})
        qb.dowImage(fileName,path)
            
