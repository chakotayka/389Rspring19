#!/usr/bin/env python3

import hashlib
import string

def crack():
    #hashes = open("hashes.txt", "r") # open and read hashes.txt
    #passwords = open("passwords.txt", "r") # open and read passwords.txt
    with open('passwords.txt') as my_file:
        passwords = my_file.readlines()
    with open('hashes.txt') as my_file:
        hashes = my_file.readlines()

    hashes = [i.replace('\n','') for i in hashes]

    characters = string.ascii_lowercase

    # for c in characters:
    #    for p in passwords:
            #print p + '\n'
            
            # crack hashes
            #hash = c + "" + p.strip('\n')
            #print hash + "\n"
            #h = hashlib.sha256(hash).hexdigest()
            #print h
            #if h in hashes:
               #print password + ":" + h
            
            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

    for c in characters:
        #print c
        for p in passwords:
            hash = c + "" + p.strip('\n')
            h = hashlib.sha256(hash).hexdigest()
            #print h
            if h in hashes:
                print p.strip('\n') + ":" + h
    
if __name__ == "__main__":
    crack()
