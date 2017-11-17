# -*-coding:utf-8-*-
import requests
import json
import codecs
import io 
import sys  
import cPickle as pickle
import time


#889976
def getName():
    url = "http://www.iwencai.com/traceback/index/get-query-type-list"
    r = requests.get(url)
    d=r.text
    j=json.loads(d)
    c=j['data']
    list=[]
    for i in c:
        s=i['subNav']
        for k in s:
            name=k['name']
            str=k['value']
            for c in str:
                #list.append(name+u''+c)
				writ(name+u''+c+';\n')
				#print(c)

def getData(query):
    url = "http://www.iwencai.com/regression/back-test-new?query="+query+"&daysForSaleStrategy=2,5,10&startDate=2011-05-26&endDate=2017-11-14&fell=0.001"
    print(url)
    r = requests.get(url)
    d=r.text
    d.encode("utf-8")
    j=json.loads(d)
    #list2 = map(msg.get, list1)  
    #print(list2[0])
    #a=eval(d)
    c=j['data']['result']['result']['rate_data']
    list=[]
    for i in c:
        list.append(float(i['winRate']))
	fitness=int(max(list)*100)
    output=str(fitness)+url
    if fitness>80:
        dump(output)
    print(fitness)
    return fitness
#getData()

def dump(data):
    t = str(time.time())
    output = open("dayu80.bin"+t, 'wb')
    pickle.dump(data, output)

def writ(str):
    with open('douban.txt','a') as f:
        for s in str:
            s = s.encode('utf-8')
            f.write(s)  
def read():
    f=open('douban.txt')
    text=f.readlines()
    if text[0][:3] == codecs.BOM_UTF8: 
        text[0] = text[0][3:] 	
    list=[]		
    for i in text:
        list.append(i.decode("utf-8")[:-1])
    #print(len(list))
    return list
#getName()


def run(individual):
    list=read()
    temp=""
    for i in individual:
        temp+=list[i]
    query=temp+u"非新股;非ST;非*ST;非停牌;不包含ST;非停牌股;不含次新股;非创业板;上市天数>30日;股价5-45元;"
    try:
        fitness=getData(query)
    except BaseException as inis:
        return 0
    return fitness
#list=[0,2,4,5]
#print(run(list))	

	
