#coding=utf-8
import qiniu

 
accessKey = "SkSVUCDtU5PDISI7X4iJx7OTtxUt39ImIIu_Ihtn"
secretKey = "VXrSU6llkgRujaHVhc86wSLA_e822QNrFpfkSfxh"
 
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
def upload_without_key(bucket,key, filePath):
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








 
def main():
  bucket = "share"
  filePath = "/usr/work/tpot/test/image/0.png"
  upload_without_key(bucket, filePath)



