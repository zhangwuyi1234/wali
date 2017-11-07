# -*- coding: utf-8 -*-

import os
import shutil
import oss2
import config as cf



endpoint = os.getenv('OSS_TEST_ENDPOINT', 'oss-cn-shanghai.aliyuncs.com')

def init(flag):
    global access_key_id
    global access_key_secret
    global bucket_name
    global bucket
    a=cf.loadConfig(flag)
    access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID',a[0])
    access_key_secret = os.getenv('6OSS_TEST_ACCESS_KEY_SECRET',a[1])
    bucket_name = os.getenv('OSS_TEST_BUCKET', a[2])
    for param in (access_key_id, access_key_secret, bucket_name, endpoint):
        assert '<' not in param, 'setPram' + param
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)


def upFile(fileName,path):
    oss2.resumable_upload(bucket, fileName, path)
    
def upImage(key,fileName):
    bucket.put_object_from_file(key, fileName)
def dowImage(key,fileName):
    bucket.get_object_to_file(key, fileName)
def dowFile(key,fileName):
    bucket.get_object_to_file(key,fileName)
#test
#upImage("12344.png","test.png")
#dowImage("share.tar","share.tar")

if __name__ == "__main__":
    
    from pymongo import *
    client = MongoClient("localhost", 27017)
    db = client.share
    collection = db.code

    f=open("images.lst","w+")
    try: 
        count=db.image.count({"flag":1,"output":{ '$ne' : -2 }})
        print(count)
        #count=29
        k=0
        for i in range(count):
            i=i+1
            image=db.image.find({"flag":1,"output":{ '$ne' : -2 }}).skip(k).limit(i)
            k=i
            output=str(image[0]['output'])
            fileName=str(image[0]['fileName'])
            print(output+'_'+fileName+".png")
            db.image.update({'flag':1,'fileName':fileName},{'$set':{'flag':2}})
            dowImage(fileName,'/data/'+fileName+'.png')
            f.writelines(fileName+' '+output)
    except BaseException as inst:
        f.close()
        print("___error__openImage____")
