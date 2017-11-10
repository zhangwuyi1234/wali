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
    for c in folder:
        targetFile=folderPath+"/"+c
        folder_adPath=folder_ad_Path+"/"+c
        mkdir(targetFile)
        mkdir(folder_adPath)
        shearFolder(c,folderPath)

def shearFolder(folder,folderPath):
    for fileName in folder:
        tempPath=folderPath+"/"+fileName
        shutil.copy(tempPath, folderPath+"/"+folder) 
        os.remove(tempPath)
        #os.system(' rm -rf '+tempPath) 

def upShearFileList(folderPath):
    dnList=listdir(folderPath)
    for dn in dnList:
        dirName=folderPath+"/"+dn
        fnlist=listdir(dirName)
        for fn in fnlist:
            shutil.copy(dirName+"/"+fn, folderPath+"/"+fn) 
        shutil.rmtree(dirName)

if __name__ == "__main__":
    folderPath="/data/image"
    folder_ad_Path="/data/toimage"
    imgSize=100
    #shearFileList(folderPath)
    
    upShearFileList(folderPath)
