#!/usr/bin/env python3

import sys, platform, subprocess, socket, crypt, getpass


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def get_username():
   pass 

def get_password():
    print("User " + getpass.getuser() + " will be created")
    while True:
        p = getpass.getpass(prompt='New Passord:')
        p2 = getpass.getpass(prompt='Confirm Password:')
        if p == p2:
            break
        print("Passwords don't match! Resetting, re-enter passwords.")
    return crypt.crypt(p, crypt.mksalt(crypt.METHOD_SHA512))
