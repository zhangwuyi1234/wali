# -*- coding:utf-8 -*-
import os
import shutil
from os import listdir

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
    for c in range(0,len(folder)):
        dirNum=str(c+stratNum)
        targetFile=folderPath+"/bin"+dirNum
        fPath=folder_ad_Path+"/bin"+dirNum
        mkdir(targetFile)
        mkdir(fPath)
        shearFolder(folder[c],folderPath,dirNum)

def shearFolder(folder,folderPath,dirNum):
    for fileName in folder:
        tempPath=folderPath+"/"+fileName
        shutil.copy(tempPath, folderPath+"/bin"+dirNum) 
        os.remove(tempPath)
        #os.system(' rm -rf '+tempPath)  
        
def upShearFileList(folderPath):
    dnList=listdir(folderPath)
    for dn in dnList:
        dirName=folderPath+"/"+dn
        fnlist=listdir(dirName)
        for fn in fnlist:
            isExists=os.path.exists(folderPath+"/"+fn)
            if not isExists:
                shutil.copy(dirName+"/"+fn, folderPath+"/"+fn) 
        shutil.rmtree(dirName)

def checkImageOpen(imagePath):
    try:
        im=Image.open(imagePath)
        im=im.convert('RGB')
    except BaseException as inst:
	os.remove(imagePath)
def checkDirImage(folderPath):
    imgList=listdir(folderPath)
    for i in imgList:
        checkImageOpen(folderPath+"/"+i);
        
if __name__ == "__main__":
    folderPath="/data/image"
    folder_ad_Path="/data/toimage"
    imgSize=1000
    stratNum=0
    
    checkDirImage(folderPath)
    #shearFileList(folderPath)
    #upShearFileList(folderPath)
