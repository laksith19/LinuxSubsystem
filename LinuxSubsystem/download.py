#!/usr/bin/env python3
import urllib.request
import shutil

url = 'https://cloud-images.ubuntu.com/'\
        'jammy/current/jammy-server-cloudimg-amd64.img'
file = 'ubuntu-base.img'
request = urllib.request.Request(url)
print("Starting Download of base image")
with urllib.request.urlopen(request) as response:
    total_size = int(response.info()['Content-Length'])
    completion = 0
    with open(file, 'wb') as f:
        while True:
            buffer = response.read(shutil.COPY_BUFSIZE)
            if not buffer:
                break
            f.write(buffer)
            completion += len(buffer) / total_size
            print("Completion Percentage: ", completion * 100, "%")


print("Done with the download")

