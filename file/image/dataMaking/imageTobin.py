
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:17:45 2017

@author: zhangwuyi
"""

import upData_batch as ub
#import threading
import numpy as np
from PIL import Image
import operator
from os import listdir
import sys
import cPickle as pickle
import random
data={}
list1=[]
list2=[]
list3=[]
def img_tra(fi,imglist,num):
    for k in range(0,num):
        currentpath=folder+"/bin"+str(fi)+"/"+imglist[k]
        im=Image.open(currentpath)
        im=im.convert('RGB')
        #width=im.size[0]
        #height=im.size[1]
        x_s=640
        y_s=640
        out = im.resize((x_s,y_s),Image.ANTIALIAS)
        out.save(folder_ad+"/bin"+str(fi)+"/"+str(imglist[k]))
def addWord(theIndex,word,adder):
    theIndex.setdefault(word,[]).append(adder)
def seplabel(fname):
    filestr=fname.split(".")[0]
    label=int(filestr.split("_")[0])
    return label
def mkcf(fi,size):
    imglist=listdir(folder+"/bin"+fi)
    num=len(imglist)
    img_tra(fi,imglist,num)
    label=[]
    for i in range (0,num):
        label.append(seplabel(imglist[i]))
    print(num)
    global data
    global list1
    global list2
    global list3
    for k in range(0,num):
        currentpath=folder_ad+"/bin"+fi+"/"+imglist[k]
        im=Image.open(currentpath)
        #with open(binpath, 'a') as f:
        for i in range (0,640):
            for j in range (0,640):
                cl=im.getpixel((i,j))
                list1.append(cl[0])
        for i in range (0,640):
            for j in range (0,640):
                cl=im.getpixel((i,j))
                #with open(binpath, 'a') as f:
                #mid=str(cl[1])
                #f.write(mid)
                list1.append(cl[1])
        for i in range (0,640):
            for j in range (0,640):
                cl=im.getpixel((i,j))
                list1.append(cl[2])
        list2.append(list1)
        list1=[]
        #f.close()
        print("image"+str(k+1)+"saved.")
        list3.append(imglist[k].encode('utf-8'))
    arr2=np.array(list2,dtype=np.uint8)
    data['batch_label'.encode('utf-8')]='testing batch '+str(fi)+' of '+str(size).encode('utf-8')
    data.setdefault('labels'.encode('utf-8'),label)
    data.setdefault('data'.encode('utf-8'),arr2)
    data.setdefault('filenames'.encode('utf-8'),list3)
    output = open(binpath, 'wb')
    pickle.dump(data, output)
    output.close()
    ub.forDelFile(folder_ad+"/bin"+fi)
    ub.upBatch(binpath+"_"+str(fi))

folder="/data/image"
folder_ad="/data/toimage"
binpath="/data/bin/data_batch"
imgSize=200
shearFileList(folder)
def shearFileList(folder):
    total=listdir(folder)
    imgNum=len(total)/imgSize
    fileList = [imglista[i:i+imgSize] for i in range(0,total,imgSize)]
    for c in range (0,imgNum):
        targetFile=folder+"/bin"+str(fi)
	os.makedirs(targetFile)
        shearFileList(fileList,targetFile)
	

files=listdir(folder)
size=len(files)/imgSize
for fi in range (0,size):
    mkcf(fi,size)
	
