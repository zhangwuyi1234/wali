
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:17:45 2017

@author: ielij
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
def img_tra():
    for k in range(0,num):
        currentpath=folder+"/"+imglist[k]
        im=Image.open(currentpath)
        im=im.convert('RGB')
        #width=im.size[0]
        #height=im.size[1]
        x_s=64
        y_s=64
        out = im.resize((x_s,y_s),Image.ANTIALIAS)
        out.save(folder_ad+"/"+str(imglist[k]))
def addWord(theIndex,word,adder):
    theIndex.setdefault(word,[]).append(adder)
def seplabel(fname):
    filestr=fname.split(".")[0]
    label=int(filestr.split("_")[0])
    return label
def mkcf():
    global data
    global list1
    global list2
    global list3
    for k in range(0,num):
        currentpath=folder_ad+"/"+imglist[k]
        im=Image.open(currentpath)
        #with open(binpath, 'a') as f:
        for i in range (0,64):
            for j in range (0,64):
                cl=im.getpixel((i,j))
                list1.append(cl[0])
        for i in range (0,64):
            for j in range (0,64):
                cl=im.getpixel((i,j))
                #with open(binpath, 'a') as f:
                #mid=str(cl[1])
                #f.write(mid)
                list1.append(cl[1])
        for i in range (0,64):
            for j in range (0,64):
                cl=im.getpixel((i,j))
                list1.append(cl[2])
        list2.append(list1)
        list1=[]
        #f.close()
        print("image"+str(k+1)+"saved.")
        list3.append(imglist[k].encode('utf-8'))
    arr2=np.array(list2,dtype=np.uint8)
    data['batch_label'.encode('utf-8')]='testing batch 1 of 1'.encode('utf-8')
    data.setdefault('labels'.encode('utf-8'),label)
    data.setdefault('data'.encode('utf-8'),arr2)
    data.setdefault('filenames'.encode('utf-8'),list3)
    output = open(binpath, 'wb')
    pickle.dump(data, output)
    output.close()

folder="/data/image"
folder_ad="/data/toimage"
imglist=listdir(folder_ad)
num=len(imglist)
img_tra()
label=[]
for i in range (0,num):
    label.append(seplabel(imglist[i]))
binpath="/data/bin/test_batch"
print(binpath)
mkcf()
	
