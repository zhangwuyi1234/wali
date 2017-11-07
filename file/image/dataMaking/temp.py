import numpy as np
from PIL import Image
import operator
from os import listdir
import sys

import random
data={}
def img_tra():
    for k in range(0,num):
        currentpath=folder+"/"+imglist[k]
        im=Image.open(currentpath)
        im = im.convert('RGB')
        #width=im.size[0]
        #height=im.size[1]
        x_s=32
        y_s=32
        out = im.resize((x_s,y_s),Image.ANTIALIAS) 
        out.save(folder_ad+"/"+str(imglist[k]))

folder="/data/image"
folder_ad="/data/toimage"
imglist=listdir(folder)
num=len(imglist)
print(num)
#img_tra()
