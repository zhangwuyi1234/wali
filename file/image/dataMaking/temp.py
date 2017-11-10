
from os import listdir
import sys

import random
data={}


folder="/data/image"
folder_ad="/data/toimage"
imglist=listdir(folder)
for i in imglist:
    path=folder+"/"+i
    filelist=listdir(path)
    num=len(filelist)
    print(num)
