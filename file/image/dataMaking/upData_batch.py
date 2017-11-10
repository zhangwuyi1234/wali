
from os import listdir
import sys
import shutil
import os as obs
#import threading

sys.path.append("..")
import aliyunTools as ob
ob.init("oss2")

def target():
    upBatch(binpath)
    print('--upData_batch.py  end'+binpath)
   
def delFile(filePath):
    try:
        obs.remove(filePath)
    except BaseException as inis:
        print "--removeFileError---"
def forDelFile(folder_ad):
    shutil.rmtree(folder_ad)
    #imglist=listdir(folder_ad)
    #for i in imglist:
        #delFile(folder_ad+"/"+i)
def upBatch(filePath):
    fileName=filePath.split('/')[-1]
    #aohai_test/cifar-10-batches-py/
    ob.upFile("bin2/"+fileName,filePath)
    delFile(filePath)
        
def upBatchAll(folder):
    global binpath
    imglist=listdir(folder)
    num=len(imglist)
    print num
    for j in range(0,num):
        binpath=folder+"/"+imglist[j]
        #t = threading.Thread(target=target)
        #t.start()
        #ob.upFile("bin/"+imglist[j],currentpath)
        upBatch(binpath)
        
    
if __name__ == "__main__":
    folder="/data/bin"
    upBatchAll(folder) 
