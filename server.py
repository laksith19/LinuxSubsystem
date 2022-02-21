#!/usr/bin/env  python3

import http.server
import socketserver
import os

PORT = 8000

class noCloudServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/user-data' and  self.path != '/meta-data':
            self.send_responsde(404);
            return
        self.path = 'www' + self.path
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = noCloudServer
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    httpd.serve_forever()
