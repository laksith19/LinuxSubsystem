#!/usr/bin/env python3
import urllib.request
import shutil

URL = 'https://cloud-images.ubuntu.com/'\
        'jammy/current/jammy-server-cloudimg-amd64.img'
FILE = 'base.img'
REQUEST= urllib.request.Request(URL)


print("Starting Download of base image")
with urllib.request.urlopen(REQUEST) as RESPONSE:
    total_size = int(RESPONSE.info()['Content-Length'])
    completion = 0
    with open(FILE, 'wb') as f:
        while True:
            buffer = RESPONSE.read(shutil.COPY_BUFSIZE)
            if not buffer:
                break
            f.write(buffer)
            completion += len(buffer) / total_size
            print("Downloading: ", f'{completion * 100:.2f}', "%", end='\r')

print("\nDownload Completed!")

