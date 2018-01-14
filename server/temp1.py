#encoding=utf-8
 
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()
host = '127.0.0.1' #'106.15.176.141'
port = 80 #26195
s.bind((host, port)) #
s.listen(10) 
while True:
    c, addr = s.accept() #
    c.send('This is a simple server') #
    print c.recv(1024) #
    c.close()
