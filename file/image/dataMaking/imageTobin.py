# -*- coding: utf-8 -*-
"""
@author: zhangwuyi
"""

import numpy as np
from PIL import Image
import operator
from os import listdir
import os as obs
import sys
import cPickle as pickle
import random
import upData_batch as ub
#import threading

data={}
list1=[]
list2=[]
list3=[]


def target():
    ub.upBatch(binpath)
    print('--upData_batch.py  end'+binpath)	
def forDelFile(imglisttemp):
    for img in imglisttemp:
        ub.delFile(folder_ad+"/"+img)	
def img_tra():
    for k in range(0,num):
        currentpath=folder+"/"+imglist[k]
        im=Image.open(currentpath)
        im = im.convert('RGB')
        #width=im.size[0]
        #height=im.size[1]
        x_s=35
        y_s=50
        out = im.resize((x_s,y_s),Image.ANTIALIAS)
        out.save(folder_ad+"/"+str(imglist[k]))
	#ub.delFile(currentpath)
def addWord(theIndex,word,adder):
    theIndex.setdefault(word,[]).append(adder)
def seplabel(fname):
    filestr=fname.split(".")[0]
    label=int(filestr.split("_")[0])
    if label==-1:
        label=0;
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
        for i in range (0,35):
            for j in range (0,50):
                cl=im.getpixel((i,j))
                list1.append(cl[0])
        for i in range (0,35):
            for j in range (0,50):
                cl=im.getpixel((i,j))
                list1.append(cl[1])
        for i in range (0,35):
            for j in range (0,50):
                cl=im.getpixel((i,j))
                list1.append(cl[2])
        list2.append(list1)
        list1=[]
        #f.close()
        print("image"+str(k+1)+"saved.")
        list3.append(imglist[k].encode('utf-8'))
    arr2=np.array(list2,dtype=np.uint8)
    list2=[]
    data['batch_label'.encode('utf-8')]="training batch {} of {}".format(1, 1).encode('utf-8')
    data.setdefault('labels'.encode('utf-8'),label)
    data.setdefault('data'.encode('utf-8'),arr2)
    arr2=[]
    data.setdefault('filenames'.encode('utf-8'),list3)
    list3=[]
    output = open(binpath, 'wb')
    pickle.dump(data, output)
    output.close
    forDelFile(imglist)
    #t = threading.Thread(target=target)
    #t.start()
    #t.join()	
    target()
    print(' pickle.dump Data_batch  end --'+binpath)


folder="/data/image"
folder_ad="/data/toimage"
imglist=listdir(folder)
num=len(imglist)
img_tra()
num=len(listdir(folder_ad))
label=[]
for i in range (0,num):
    label.append(seplabel(imglist[i]))
binpath="/data/bin/data_batch_"+str(j)
print(binpath)
mkcf()

   

