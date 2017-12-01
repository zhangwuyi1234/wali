# import the necessary packages
from PIL import Image
import imagehash
from numpy import *

def enHash(imagePath):
    highfreq_factor = 1
    hash_size = 16
    img_size = hash_size * highfreq_factor
    hash1 = imagehash.phash(Image.open(imagePath),hash_size=hash_size,highfreq_factor=highfreq_factor)
    #hash2 = imagehash.phash(Image.open(imagePath2),hash_size=hash_size,highfreq_factor=highfreq_factor)
    return str(hash1)

def encode(s):
    lists= ''.join([bin(ord(c)).replace('0b', '').zfill(8) for c in s])
    temp = []
    for i in lists:
        temp.append(int(i))
    return temp

def similarity(hash1,hash2):
    vector1 = mat(encode(hash1))
    vector2 = mat(encode(hash2))
    vector3 = vector1-vector2
    #print("vector3 = vector1-vector2",vector3)
    smstr = nonzero(vector1-vector2);
    #print (smstr)
    sim=(shape(smstr[1])[0])
    print (sim)
    return sim


if __name__ == "__main__":
    from pymongo import *
    import backup.upMongo as upMongo
    #imagePath1="/home/wuyi/data/toimage/28bird_bullocks_oriole.jpg"
    #imagePath2="/home/wuyi/data/toimage/30bird_bullocks_oriole.jpg"
    #hash1=enHash(imagePath1)
    #hash2=enHash(imagePath2)
    #similarity(hash1,hash2)
    client = MongoClient("localhost", 27017)
    db = client.share
    collection = db.code
    
    count=db.image.count({'flag':2,'enHash':{'$exists':False}})
    print(count)
    k=0
    for i in range(count):
        i=i+1
        image=db.image.find({"flag":2,'enHash':{'$exists':False}}).skip(k).limit(i)
        k=i
        output=str(image[0]['output'])
        fileName=str(image[0]['fileName'])
        path="/data/image/"+output+'_'+fileName+".png"
        isExists=os.path.exists(path)
        if not isExists:
            try:
                db.image.update({'fileName':fileName},{'$set':{'flag':1}})
            except BaseException as inst:
                print("updateImageError")
                db.image.update({'flag':1,'fileName':fileName},{'$set':{'flag':-1}})
        else:
            enHash=enHash(path)
            print(enHash)
            db.image.update({'fileName':fileName},{'$set':{'enHash':enHash}})
    upMongo.upShare()
