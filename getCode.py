
from pymongo import *
import requests
import time
import sys
import importlib
importlib.reload(sys)

client = MongoClient()
client = MongoClient("localhost", 27017)
db = client.share
collection = db.code

            
def getCode():
    url="http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C._A&sty=FCOIATA&sortType=C&sortRule=-1&page=2&pageSize=5000&python=var%20quote_123%3d{rank:[(x)],pages:(pc)}&token=7bc05d0d4c3c22ef9fca8c2a912d779c&jsName=quote_123&_g=0.578745418953210"
    
    r = requests.Session().get(url)
  
    s=r.content
    text= s.decode()
    print(type(text))
    strs=str(s[5:]).split('","')
    codes=[]
    k=0
    ki=100
    for i in range(len(strs)):
        d=strs[i]
        code=d[2:8]
        count=collection.count({"code":code})
        if count>0:
            continue
        elif code[0] =='3':
            #print(code)
            continue
        print(code)
        codes.append({'code':code,'flag':0,"i":k,'start':20050101})
        k=k+1
    collection.insert_many(codes)
getCode();
