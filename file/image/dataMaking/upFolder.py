# -*- coding:utf-8 -*-
import os
import shutil
from os import listdir
from PIL import Image


def checkPath(path):
    if os.path.exists(path):
	#os.path.isfile(path):
        if os.path.isdir(path):
            return True
    return False

def mkdir(path):
    path=path.strip()
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False
def remove(path):
    isExists=os.path.exists(path)
    if isExists:
        os.remove(path)
        return True
    else:
        return False
def imgShear(srcPath,tagetPath):
    try:
        im=Image.open(srcPath)
        img_size = im.size
        #print("图片宽度和高度分别是{}".format(img_size))
        w = img_size[0]/2.0
        h = img_size[1]/2.0
        x = 0
        y = 0
        region = im.crop((x, y, x+w, y+h))
        bg = Image.new("RGB", region.size, (255,255,255))
        bg.paste(region,region)
        bg.save(tagetPath)
    except BaseException as inst:
	remove(srcPath)

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
        if checkPath(tempPath):
            continue			  
        #shutil.copy(tempPath, folderPath+"/bin"+dirNum) 
        imgShear(tempPath,folderPath+"/bin"+dirNum+"/"+fileName)
        remove(tempPath)
        #os.system(' rm -rf '+tempPath)  
        
def upShearFileList(folderPath):
    dnList=listdir(folderPath)
    for dn in dnList:
        dirName=folderPath+"/"+dn
        fnlist=listdir(dirName)
        for fn in fnlist:
            isExists=os.path.exists(folderPath+"/"+fn)
            if not isExists:
                shutil.copy(dirName+"/"+fn, "/data/image/"+fn) 
        shutil.rmtree(dirName)
	


def checkImageOpen(imagePath):
    try:
        im=Image.open(imagePath)
        im=im.convert('RGB')
    except BaseException as inst:
	remove(imagePath)
def checkDirImage(folderPath):
    imgList=listdir(folderPath)
    for i in imgList:
        checkImageOpen(folderPath+"/"+i);
        
if __name__ == "__main__":
    folderPath="/data/image"
    folder_ad_Path="/data/toimage"
    imgSize=4000
    stratNum=0
    
    #checkDirImage(folderPath)
    shearFileList(folderPath)
    #upShearFileList(folderPath)
