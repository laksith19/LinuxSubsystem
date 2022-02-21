#!/usr/bin/env  python3

import http.server
import os

PORT = 8000
FLAG = True

class noCloudServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/user-data' and  self.path != '/meta-data':
            FLAG = False
            self.send_error(404);
            return
        self.send_response(200)
        self.send_header("Content-type", "application/octet-stream");
        self.end_headers()
        content = open(os.path.join(os.path.realpath('www'), self.path[1:]), 'rb').read()
        self.wfile.write(content) 
Handler = noCloudServer
with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    while FLAG:
        httpd.handle_request()
    httpd.server_close()

print("test, got here")
