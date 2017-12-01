# -*- coding: utf-8 -*-

import os
import shutil
import oss2
import time
import sys
sys.path.append("..")
import aliyunTools as q
q.init("oss2")

def upShare():
    #os.system(' cd /tmp ')
    os.system('mongodump -h 127.0.0.1 -d share -o share')
    os.system('tar -cvf share.tar share ')
    timeStr=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    key="share_"+timeStr+".tar"
    q.upFile( key, 'share.tar')
    #q.upload_without_key("share0",'share1.tar','share.tar')
    shutil.rmtree('share')
    os.remove('share.tar')

   
if __name__ == "__main__":
    upShare()
