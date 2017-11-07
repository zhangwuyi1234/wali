#coding=utf-8
import qiniu
import requests
from qiniu.services.cdn.manager import create_timestamp_anti_leech_url
import time
import config as cf

a=cf.loadConfig("qiniu")
accessKey = a[0].strip()
secretKey = a[1].strip()
bucket = "share0"

#解析结果
def parseRet(retData, respInfo):
  if retData != None:
    print("Upload file success!")
    print("Hash: " + retData["hash"])
    print("Key: " + retData["key"])
    #检查扩展参数
    for k, v in retData.items():
      if k[:2] == "x:":
        print(k + ":" + v)
    #检查其他参数
    for k, v in retData.items():
      if k[:2] == "x:" or k == "hash" or k == "key":
        continue
    else:
        print(k + ":" + str(v))
    return retData["key"]
  else:
    print("Upload file failed!")
    print("Error: " + respInfo.text_body)
 
#无key上传，http请求中不指定key参数
def upload_without_key(key, filePath):
  #生成上传凭证
  auth = qiniu.Auth(accessKey, secretKey)
  upToken = auth.upload_token(bucket, key)
  #上传文件
  retData, respInfo = qiniu.put_file(upToken, key, filePath)
  #解析结果
  return parseRet(retData, respInfo)
 

def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return G
        else:
            return M
    else:
        return kb
# 获取文件大小
def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return formatSize(size)
    except Exception as err:
        print(err)

        
    

def dowImage(key,path):
    #http://owcxc992o.bkt.clouddn.com/00000120170916
    host = 'owcxc992o.bkt.clouddn.com'
    # 配置时间戳时指定的key
    encrypt_key = key
    # 资源路径
    #file_name = path
    # 查询字符串,不需要加?
    query_string = key
    # 截止日期的时间戳,秒为单位，3600为当前时间一小时之后过期
    deadline = int(time.time())+3600
    timestamp_url = create_timestamp_anti_leech_url(host, path, query_string, encrypt_key, deadline)
    print(timestamp_url)
        
 
if __name__ == "__main__":
    #filePath = "/usr/work/github/file/image/test.txt"
    #upload_without_key("testtxt", filePath)
    key='00000120170916'
    path = '/tmp/'+key+'.png'
    dowImage(key,path)



