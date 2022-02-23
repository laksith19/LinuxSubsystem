#!/usr/bin/env python3

import threading
import subprocess
import time
import sys

t = threading.Thread(target = subprocess.run, args =(["curl", "https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64.img", "-o", "ubuntu-focal-base.img"], ), kwargs = {"capture_output" : True})
t.start()
print("Download Started")
print(threading.active_count())
while t.is_alive():
    print(".", end =' ', flush=True)
    time.sleep(2)
print(threading.active_count())
