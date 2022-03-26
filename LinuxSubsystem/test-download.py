#!/usr/bin/env python3
import urllib.request
import shutil

url = 'https://cloud-images.ubuntu.com/'\
        'focal/current/focal-server-cloudimg-amd64.img'
file = 'ubuntu-base.img'
request = urllib.request.Request(url)
print("Starting Download of base image")
with urllib.request.urlopen(request) as response:
    with open(file, 'wb') as f:
        shutil.copyfileobj(response, f)

print("Done with the download")

