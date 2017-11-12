

from pymongo import *
import requests
import time
import sys
import os
import importlib
import urllib.request
import numpy as np
import qiniuTools as q
import getData as gd
from PIL import Image
import aliyunTools as ob
import backup.upMongo as upMongo

ob.init("oss1")
importlib.reload(sys)

client = MongoClient()
client = MongoClient("localhost", 27017)
db = client.share
collection = db.code


def getfilePath(fileName):
    filePath='/usr/work/github/file/image/data/'+ fileName +'.png'
    return filePath

def getImage(code,te,formula,typem):
     
    url="http://pifm3.eastmoney.com/EM_Finance2014PictureInterface/Index.aspx?ID="+code+te+"&UnitWidth=-6&imageType=KXL&EF=&Formula="+formula+"&&AT=&type="+typem+"&token=44c9d251add88e27b65ed86506f6e5da&0.2942712066803206"
    #print(url)

    end=time.strftime("%Y%m%d",time.localtime())    
    fileName=code+"_"+end+"_"+formula
    if "RSI"==formula or typem=="":
        formulaPath=getfilePath(fileName)
        urllib.request.urlretrieve(url,formulaPath)
        return formulaPath
    
    formulaPath=getfilePath(formula)
    urllib.request.urlretrieve(url,formulaPath)   
    img=""
    try:
        img=Image.open(formulaPath)  
        os.remove(formulaPath)
    except BaseException as inst:
        print("open.formulaPath_error=========")
        print(inst)
        return -1
    img= img.transpose(Image.FLIP_TOP_BOTTOM)    
    box=(0,0,520,80)
    img=img.crop(box)
    img= img.transpose(Image.FLIP_TOP_BOTTOM)
    filePath=getfilePath(fileName)
    img.save(filePath,"png")
    
    return filePath
    #return formulaPath 




def sumImage(files,code,end):

    img= Image.open(files[1])
    mw=img.size[0] #*img.sie[1]
    mwy=img.size[1]
        
    ms = 2
    msize = mw * ms
    msy =5
    mysize= mwy*msy
    toImage = Image.new('RGBA', (msize,mysize))

    ix=1
    for y in range(1, msy+1): 
        for x in range(1, ms+1):
            fname =files[ix]
            fromImage = Image.open(fname)
            #fromImage =fromImage.resize((mw, mw), Image.ANTIALIAS)  
            toImage.paste(fromImage, ((x-1) * mw, (y-1) * mwy))
            os.remove(fname)
            ix=ix+1
    
    filePath=getfilePath(code+end)
    toImage.save(filePath)
    img1 = Image.open(files[0])
    img2 = Image.open(filePath)
    img3 = Image.open(files[-1])
    size1=img1.size
    size2=img2.size
    ms=img1.size[1]+img2.size[1]  
    toImage = Image.new('RGBA', (size2[0], ms)) 
    toImage.paste(img1,( 0, 0)) 
    toImage.paste(img3,( size1[0], 0))
    toImage.paste(img2,( 0, size1[1]))
    toImage.save(filePath)

    key=q.upload_without_key(code+end,filePath)
    ob.upImage(code+end,filePath)
    db.image.insert({'fileName':key,'flag':0})
    os.remove(files[0])
    os.remove(filePath)
    os.remove(files[-1])



end=time.strftime("%Y%2m%d",time.localtime())
end=str(int(end))
#2end="20170615"

count=db.code.count({"flag":0})
#print(codes[0]['c8ode'])
#code=codes[0]['code']

#count=10

for i in range(count):
    print(i)
    temp=db.code.find({"i":i})
    code=temp[0]['code']    
    te=""
    if code[0]=='6':
        te='1'
    elif code[0]=='0':
        te='2'

    fileName=code+end
    print(fileName)
    image=db.image.find({"fileName":fileName})
    if image.count() > 0:
        print("==========image  >  0   =========="+str(image[0]))
        #db.error.insert({"code":scode})
        continue

    formulas=["RSI","KDJ","MACD","WR","DMI","BIAS","OBV","CCI","ROC","CR","BOLL","typem"]
    files=[]
    
    for i in formulas:
        typem="M30"
        if "typem"==i:
            typem="" 
        repath=getImage(code,te,i,typem)
        if repath == -1:
            break
        files.append(repath)
    #print(files)
    else:
        sumImage(files,code,end)
        db.code.update({'flag':0,'code':code},{'$set':{'flag':1,'end':end}})

print("-----up----end-------")
upMongo.upShare()


