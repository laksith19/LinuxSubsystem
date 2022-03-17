#!/usr/bin/env  python3

import LinuxSubsystem
import http.server
import os

# The port where the config is served
PORT = 8000
CONTENT = LinuxSubsystem.generate_config()
class noCloudServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/user-data' and  self.path != '/meta-data':
            self.send_error(404);
            return
        self.send_response(200)
        self.send_header("Content-type", "application/octet-stream");
        self.end_headers()
        self.wfile.write(CONTENT[self.path].encode('utf-8')) 
Handler = noCloudServer
with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    i = 0
    while i < 10:
        httpd.handle_request()
        i += 1
    httpd.server_close()
