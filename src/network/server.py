#!/usr/bin

# Time server program
from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)

while True:
    client = s.accept()
    print("I got a connection from %s" % str(client))
    timestr = time.ctime(time.time()) + "\r\n"
    client.send(timestr.encode('ascii'))
    client.close()



