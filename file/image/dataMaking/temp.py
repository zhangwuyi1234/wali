
from os import listdir
import sys

import random
data={}

folder="/data/image"
folder_ad="/data/toimage"
imglist=listdir(folder)
print(len(imglist))
imglist_ad=listdir(folder_ad)
for i in imglist:
    path=folder+"/"+i
    filelist=listdir(path)
    num=len(filelist)
    print(i+"=="+str(num))
    
for j in imglist_ad:
    print(j)
