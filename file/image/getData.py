from pymongo import *
import requests
import time
import getTime as gt



client = MongoClient()
client = MongoClient("localhost", 27017)
db = client.share
collection = db.initData



def getFlag(data):
    rouws=[]
    #print("getFlag===time==="+str(data[3]))
    for j in range(3):
        print(data[j])
        temp=float(data[j][4].split("%")[0])
        rouws.append(temp)
    return rouws
            
         
def getData(code,start,end):
    print (code+str(start)+'++++++++++++++'+str(end))
    url = "http://q.stock.sohu.com/hisHq?code="+code+"&start="+str(start)+"&end="+str(end)+"&stat=1&order=D&period=d&callback=historySearchHandler&rt=json&r=0.8374035742227424&0.6025517862823159"
    
    r = requests.get(url)
    try:
        r.json()[0]['hq']
    except BaseException as inst:
        print("r===nul======")
        return -2

    data= r.json()[0]['hq']
    print("datalength==="+str(len(data)))    
    if len(data)<8:
        return -2
    data2=getFlag(data)
    print(data2)
    temp=sum(data2)
    if temp>2:
        return 1
    else:
        return -1
    #collection.insert_many(data2)
 

#codes=db.code.find({"code":"600979"})

def forCode(scode,start):
    code="cn_"+scode
    end=gt.getTimeForEnd(3,start)
    start=gt.getTimeForFrst(5,start)
    temp = db.code.find_one({"code":code})
    #end=time.strftime("%Y%m%d",time.localtime())
    #end=int(end)+1
    re=getData(code,start,end)
    return re

      #  try:   
       #     except BaseException:
        #        print("error====="+code)
        
#===test
#re=forCode("600979","20170718")
#print(re)











       
