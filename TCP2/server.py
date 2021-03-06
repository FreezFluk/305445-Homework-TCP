#!/usr/bin/env python

import socket
import os

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    newpath = r'file-upload/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    data = conn.recv(BUFFER_SIZE)
    FileUpload = open(newpath+data,"wb")
    
    if not data: break
    while data:
        FileUpload.write(data)
        data = conn.recv(BUFFER_SIZE)
    print "Upload Finish:"
    conn.send(str(data))  # echo
conn.close()
