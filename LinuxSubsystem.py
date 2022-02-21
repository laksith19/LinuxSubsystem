#!/usr/bin/env python3

import os
import crypt
import getpass
import socket

# Checks if given port free or not. Used to check for available ports to bind to.
def is_port_free(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) != 0

# Gets a Username from the user to be used with the virtual machine, uses getpass to auto generate a default name
def get_username():
    return getpass.getuser()

# Gets a password form the user and returns encrypted password   
def get_password():
    # Tries to get a valid password match from teh user before qutting with an error 
    for _ in range(3):
        passwd = getpass.getpass(prompt='New Passord:')
        passwd_2 = getpass.getpass(prompt='Confirm Password:')
        if passwd == passwd_2:
            return crypt.crypt(passwd, crypt.mksalt(crypt.METHOD_SHA512))
        print("Passwords don't match! Resetting, re-enter passwords.")
    print("Exiting! Too many failed attempts.")
    os._exit(255)

def generate_config():
    name = get_username()
    password = get_password()
    config = '#cloud-config\nusers:\n    - name: {name}\n      shell: /bin/bash\n      passwd: {password}\n      lock_passwd: false\n      sudo: [\'ALL=(ALL) ALL\']\nssh_pwauth: True\nhostname: linuxsubsystem\nruncmd:\n    - echo "blacklist floppy" | tee /etc/modprobe.d/blacklist-floppy.conf\n    - rmmod floppy\n    - update-initramfs -u\n    - touch /etc/cloud/cloud-init.disabled\n    - hostnamectl set-hostname linuxsubsystem\npower_state:\n    mode: poweroff\n    message: Shutting Down\n    timeout: 5\n    condition: True\n'
    data = bytes(config, 'UTF-8')
    print(data)
    return data
