# Writeup 2 - OSINT

Name: Sara Bittner
Section: 101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Sara Bittner

## Assignment Writeup

OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Friday, February 22 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `v0idcache`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `v0idcache` and answer the following questions:

1)	What is v0idcache's real name?  
-	Elizabth Moffet  
2)	Where does v0idcache work? What is the URL to their website?
-	Banking CEO at 13/37th National Bank
-	Company’s website: http://1337bank.money/
3)	List all personal information (including social media accounts, contacts, etc) you can find about v0idcache. For each, briefly detail how you discovered them.
-	Twitter: https://twitter.com/v0idcache  (from search on twitter of user name)
-	Email: v0idcache@protonmail.com (from company website)
-	Maybe github because it was  created around the same time: https://github.com/v0idcache
4)	List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.
     142.93.136.81 (from reverse ip lookup from 1337bank.money on viewdns.info)
    1.	IP Location Results for 142.93.136.81
    ==============
    
    City:         Amsterdam
    Zip Code:     1098
    Region Code:  NH
    Region Name:  North Holland
    Country Code: NL
    Country Name: Netherlands
    Latitude:     52.3529
    Longitude:    4.9415
    There doesn’t seem to be any history beside the bank based on securitytrails.com.  First seen February 6, 2019 and the organization hosting it is Digital Ocean.
    
    2. 162.255.118.61  and 162.255.118.61 (from dnsdumpster.com)
        Says emails are sent there, hosts 33 domains
    
    3. 216.87.155.33 (from dnsdumspter.com)
        Country Code: US
    Country Name: United States
    Latitude:     37.751
    Longitude:    -97.822
        Port 53 open
5)	List any hidden files or directories you found on this website. For full credit, list two distinct flags.
-	CMSC389R-{h1ding_fil3s_in_r0bots_L0L}
6)	What ports are open on the website? What services are running behind these ports? How did you discover this?
-	Port 22: Open ssh Version: 7.6p1 Ubuntu-4ubuntu0.2
-	Port 80: Werkzeug httpdVersion: 0.14.1
-	I discovered this from shodan.
7)	Which operating system is running on the website? How did you discover this?
-	Werkzeug/0.14.1 Python/3.7.2 from BrowserSpy
8)	BONUS: Did you find any other flags on your OSINT mission? (Up to 9 pts!)
-	Good find! CMSC389R-{h1dd3n_1n_plain_5ight} 
-	"CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}"
Random on pastebin: https://pastebin.com/WghDuAr7
Conversation potentially between this v0idcache and fl1nch (most likely true because it was created around the same time frame)  - they discuss a file called AB4300.txt


### Part 2

Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to `v0idcache`'s server via an open port that you should have found in Part 1.

Once you have gained access to `v0idcache`'s account with the correct login credentials, you will have access to a system shell.

Use your knowledge of Linux and OSINT techniques to locate the flag file and submit its contents for points.

Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.

Note: If you choose to write your own program in another language, please include instructions on how to execute your program, including what version of the language you are using. You will **NOT** receive credit if the TAs cannot run your program.

If you are stuck on this part of the assignment, let us know! The facilitator staff is here to help and teach, and we are open to releasing hints as time goes on!


I tried to access both ports with ssh, nc, and telnet, but the prompt for a password never showed.  I feel like it probably should have showed up when I tried to ssh into the server but a prompt never showed and then I couldn't get anything but a protocol mismatch.  I had modified the script to try and have it go through a wordlist (rockyou).  I have the public key so I guess I could somehow add that in but I wasn't sure where it would go.


import socket

host = "142.93.136.81" # IP address here
port = 22 # Port here
wordlist = "/Downloads/rockyou.txt" # Point to wordlist file

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            v0idcache's server.
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = s.recv(1024)     # Receives 1024 bytes from IP/Port
    print(data)             # Prints data

    username = "v0idcache"   # Hint: use OSINT

    fp = open(wordlist, 'r'):
    line = fp.readline()
    while line:
        s.send(data + "\n" + line)
    #password = ""   # Hint: use wordlist




if __name__ == '__main__':
    brute_force()
