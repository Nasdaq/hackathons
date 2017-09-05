

# server.py
import socket
import time
import thread
import os
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 8080
serversocket.bind((host, port))

def createClientSocket(clientsocket):
    print("Connection from: %s" % str(addr))
    with open("data.json", 'rb', buffering=20*(1024**2)) as data:
        for line in data:
            clientsocket.send(line)
    clientsocket.close()

while True:
    serversocket.listen(99)
    clientsocket,addr = serversocket.accept()
    try:
        thread.start_new_thread( createClientSocket,(clientsocket,))
    except:
        e = sys.exc_info()[0]
        print('ERROR: %s' % e)
        break
