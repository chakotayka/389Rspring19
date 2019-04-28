#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    #hashes = # open and read hashes.txt
    #passwords = # open and read passwords.txt

    with open('passwords.txt') as my_file:
        passwords = my_file.readlines()
        
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58' #'put_your_ip_here'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)
    # parse data
    # crack 3 times

    for i in range(3):
        print data
        data_parsed = data.split('\n')

        server_hash = data_parsed[2]

        for c in characters:
            #print c
            for p in passwords:
                hash = c + "" + p.strip('\n')
                h = hashlib.sha256(hash).hexdigest()
                #print h
                if h == server_hash:
                    s.send(c + p)
                    

        data = s.recv(1024)
        print data

    
    

if __name__ == "__main__":
    server_crack()
