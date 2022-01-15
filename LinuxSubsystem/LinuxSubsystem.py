#!/usr/bin/env python3

import sys, platform, subprocess, socket


if __name__ == '__main__':
    print("Nothing has been implemented")	


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0
