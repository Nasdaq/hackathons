

# client.py
import socket
import os
import sys

for x in range(0, 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 8080
    s.connect((host, port))

    while True:
        try:
            data = s.recv(1024)
            if str(data)== 'b\'\'':
                s.close()
                break
            print(data)
        except:
            e = sys.exc_info()[0]
            print('ERROR: %s' % e)
