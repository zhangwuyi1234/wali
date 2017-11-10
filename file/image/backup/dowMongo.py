import os
import shutil
import sys
sys.path.append("..")
import aliyunTools as ob
ob.init("oss1")

key='share.tar'
ob.dowFile(key,'share.tar')

os.system('tar xvf share.tar')

os.system(' mongorestore -h 127.0.0.1  -d share --drop share ')

shutil.rmtree('share')
os.remove('share.tar')
