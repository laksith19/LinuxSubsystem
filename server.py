#server.py, test python http server

import http.server
import socketserver
import os

PORT = 8000

class noCloudServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/user-data' or self.path == '/meta-data':
            self.send_response(200)
            dataFile = open(os.path.join(os.path.realpath('www'), self.path[1:]), 'r')
            print(dataFile)
            self.wfile.write(bytes(dataFile.read(), "utf8"))
        else: 
            self.send_response(404)
        return

Handler = noCloudServer
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    httpd.serve_forever()
