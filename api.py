#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from py_irsend import irsend
import os, sys
from socketserver import ThreadingMixIn
import threading

rooms = ['vmc']
cmds = ['off', 'powerfull', 'up', 'down', 'cooling', 'light']

class S(BaseHTTPRequestHandler):
    server_version='server-0.0.1'
    sys_version=''
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def exec_cmd(self, room, ircommand):
        try:
          cmd = irsend.send_once(room, [ircommand])
        except:
          return 0

    def do_GET(self):
        self._set_headers()
        document_root = self.path
        check_get = document_root[1:].split('&')
        room = check_get[0].split('=')
        commands = check_get[1].split('=')
        for i in rooms:
            if room[0] == "room" and room[1] == i:
               for j in cmds:
                   if commands[0] == 'cmd' and commands[1] == j:
                      self.exec_cmd(i,j)
        self.send_response(200)  
  
    def do_HEAD(self):
        self._set_headers()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass 
    
def run(port=80):
    httpd = ThreadedHTTPServer(('0.0.0.0', port), S)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        run(port=int(sys.argv[1]))
    else:
        run()
