#!/usr/bin/env  python3

import http.server
import os

# The port where the config is served
PORT = 8000

# The data to be served in the form of a python dict
CONTENT = { 
    '/meta-data' : b'{\n"instance-id": "iid-local01"\n}\n', 
    '/user-data' : b'#cloud-config\nusers:\n    - name: laksith\n      shell: /bin/bash\n      passwd: $6$8pLLJrEQ21ZZmaxD$xmNWRDukc/aj3O37ZGWR/1pC1jkJ7bbMIteiXdExGlm8tUdlR/Hel3DOzx7Cto2Fcn3XIWBevZHky6HNafP710 \n      lock_passwd: false\n      sudo: [\'ALL=(ALL) ALL\']\nssh_pwauth: True\nhostname: linuxsubsystem\nruncmd:\n    - echo "blacklist floppy" | tee /etc/modprobe.d/blacklist-floppy.conf\n    - rmmod floppy\n    - update-initramfs -u\n    - touch /etc/cloud/cloud-init.disabled\n    - hostnamectl set-hostname linuxsubsystem\npower_state:\n    mode: poweroff\n    message: Shutting Down\n    timeout: 5\n    condition: True\n'
}

class noCloudServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != '/user-data' and  self.path != '/meta-data':
            FLAG = False
            self.send_error(404);
            return
        self.send_response(200)
        self.send_header("Content-type", "application/octet-stream");
        self.end_headers()
        self.wfile.write(CONTENT[self.path]) 
Handler = noCloudServer
with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    i = 0
    while i < 10:
        httpd.handle_request()
        i += 1
    httpd.server_close()
