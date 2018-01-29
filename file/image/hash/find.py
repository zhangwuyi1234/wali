from pymongo import *

client = MongoClient()
client = MongoClient("localhost", 27017)
db = client.share

#数量和乘几率和=总几率

    

#计算enhash相似度并保存到每条记录上
def computeBykey(key):
    size=db.image.count({"newFlag":{ '$ne' : 1 }})
    k=0
    for i in range(size):
        i=i+1
        image=db.image.find({"newFlag":{ '$ne' : -2 }}).skip(k).limit(i)
        k=i
        enHash=image[0]['enHash']
        key=image[0]['key']
        id=image[0]['id']
        snumber=similarity(enHash)
        db.image.update({'id':id},{'$set':{'snumber':snumber,'skey':key}})
