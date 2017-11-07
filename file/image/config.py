def load():
    file = open("sample.txt")
    a=[]
    while 1:
        line = file.readline()
        if not line:
            break
        a.append(line)
    return a
def loadConfig(flag):
    a=load()
    for i in range(0,len(a)):
        a[i]=a[i].strip()
    b=[]
    if flag=="qiniu":
        b=[a[0],a[1]]
    elif flag=="oss1":
        b=[a[2],a[3],a[4]]
    elif flag=="oss2":
        b=[a[5],a[6],a[7]]
    return b

