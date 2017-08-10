# Realtime Streaming Stock Market Data

Client SDK

```python
import socket
import os
import sys

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host connection
host = '0.0.0.0'
port = 80

# connect to host
s.connect((host, port))

while True:
    try:
        # get 1024 bytes
        data = s.recv(1024)
        
        # check for empty byte (end of stream)
        if str(data)== 'b\'\'':
            s.close()
            break
            
        # do something with the stream data    
        print(data)
    except:
        e = sys.exc_info()[0]
        print('ERROR: %s' % e)
```
