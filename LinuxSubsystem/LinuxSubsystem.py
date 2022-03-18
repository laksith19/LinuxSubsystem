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
        passwd = getpass.getpass(prompt='Password:')
        passwd_2 = getpass.getpass(prompt='Confirm Password:')
        if passwd == passwd_2:
            return crypt.crypt(passwd, crypt.mksalt(crypt.METHOD_SHA512))
        print("Passwords don't match! Resetting, re-enter passwords.")
    print("Exiting! Too many failed attempts.")
    os._exit(255)

def generate_config():
    USER = get_username()
    PASSWD  = get_password()
    config = { 
            '/meta-data' : '{\n"instance-id": "iid-local01"\n}\n',
            '/user-data' : f'#cloud-config\nusers:\n    - name: {USER}\n'
                           f'      shell: /bin/bash\n      passwd: {PASSWD}\n      lock_passwd: false\n'
                            '      sudo:\n        - \'ALL=(ALL) ALL\'\n        - \'ALL=(ALL) NOPASSWD:/usr/sbin/shutdown\'\n'
                            'ssh_pwauth: True\nhostname: linuxsubsystem\n'
                            'runcmd:\n    - echo "blacklist floppy" | tee /etc/modprobe.d/blacklist-floppy.conf\n'
                            '    - rmmod floppy\n    - update-initramfs -u\n    - touch /etc/cloud/cloud-init.disabled\n'
                            '    - hostnamectl set-hostname linuxsubsystem\npower_state:\n    mode: poweroff\n'
                            '    message: Shutting Down\n    timeout: 5\n    condition: True\n'
            }
    return config
