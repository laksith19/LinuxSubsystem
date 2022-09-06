#!/usr/bin/env  python3

import utils
import http.server
import os

def serveConfig():
    # This is really scuffed but the easiest way to create a persitant update
    FLAG = []
    PORT = 8000
    CONTENT = utils.generate_config()
    LOG_FILE = "http-logs"
    class noCloudServer(http.server.BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            with open(LOG_FILE, "a") as logger:
                logger.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))
        def do_GET(self):
            if self.path != '/user-data' and  self.path != '/meta-data':
                if self.path == '/vendor-data':
                    FLAG.append(1)
                self.send_error(404);
                return
            self.send_response(200)
            self.send_header("Content-type", "application/octet-stream");
            self.end_headers()
            self.wfile.write(CONTENT[self.path].encode('utf-8')) 

    with http.server.HTTPServer(("", PORT), noCloudServer) as httpd:
        print("Serving config files...")
        i = 0
        while True:
            httpd.handle_request()
            if FLAG:
                break
            i += 1
        httpd.server_close()
        print("Completed!")
        print("Configuring the VM. This could take a while.")
