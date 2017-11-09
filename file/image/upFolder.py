# -*- coding:utf-8 -*-
import os
import shutil
from os import listdir

folderPath="/data/image"
imgSize=200

def mkdir(path):
    path=path.strip()
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

def shearFileList(folderPath):
    fileList=listdir(folderPath)
    total=len(fileList) 
    folder = [fileList[i:i+imgSize] for i in range(0,total,imgSize)]
    for c in range(0,total/imgSize):
        targetFile=folderPath+"/bin"+str(c)
	mkdir(targetFile)
        shearFolder(folder[c],folderPath,c)

def shearFolder(folder,folderPath,c):
    for fileName in folder:
        tempPath=folderPath+"/"+fileName
        shutil.copy(tempPath, folderPath+"/bin"+str(c)) 
        os.remove(filename)
        #os.system(' rm -rf '+tempPath)  

shearFileList(folderPath)


