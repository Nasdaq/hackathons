

# server.py
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import time
import thread
import os
import sys
import logging

logging.basicConfig()
logger = logging.getLogger()
handler = logging.FileHandler('server.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def log_event(s, msg):
    #print msg
    if s is not None:
        x_real_ip = s.request.headers.get("X-Real-IP")
        remote_ip = x_real_ip or s.request.remote_ip
    else:
        remote_ip = '0.0.0.0'
    logger.info(remote_ip + '--' + msg)

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        msg = 'new connection'
        log_event(self, msg)

    def on_message(self, message):
        msg = 'message received:  %s' % message
        log_event(self, msg)
        msg = 'sending back message: %s' % message[::-1]
        log_event(self, msg)
        try:
            self.write_message(message[::-1])
        except:
            e = sys.exc_info()[0]
            log_event(self, 'ERROR: %s' % e)

    def on_close(self):
        msg = 'connection closed'
        log_event(self, msg)

    def check_origin(self, origin):
        return True

class StreamHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        msg = 'new connection'
        log_event(self, msg)

    def on_message(self, message):
        meg = 'new connection'
        log_event(self, msg)
        try:
            with open("data.json", 'rb', buffering=20*(1024**2)) as data:
                for line in data:
                    self.write_message(line)
        except:
            e = sys.exc_info()[0]
            log_event(self, 'ERROR: %s' % e)

    def on_close(self):
        msg = 'connection closed'
        log_event(self, msg)

    def check_origin(self, origin):
        return True

application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/stream', StreamHandler),
])

if __name__ == "__main__":
    try:
        http_server = tornado.httpserver.HTTPServer(application)
        http_server.listen(80)
        msg = '*** Websocket Server Started at %s***' % socket.gethostbyname(socket.gethostname())
        log_event(None, msg)
        tornado.ioloop.IOLoop.instance().start()
    except:
        e = sys.exc_info()[0]
        log_event(None, 'ERROR: %s' % e)
