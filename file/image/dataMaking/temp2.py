import os
import shutil
from os import listdir


def mkdir(path):
    path=path.strip()
    isExists=os.path.exists(path)
    if isExists:
        shutil.rmtree(dirName)
    os.makedirs(path)


def shearFileList(folderPath):
    fileList=listdir(folderPath)
    total=len(fileList) 
    folder = [fileList[i:i+imgSize] for i in range(0,total,imgSize)]
    for c in range(0,len(folder)):
        fPath=folder_ad_Path+"/bin"+str(c)
        mkdir(fPath)

if __name__ == "__main__":
    folderPath="/data/image"
    folder_ad_Path="/data/toimage"
    imgSize=200
    shearFileList(folderPath)
  
