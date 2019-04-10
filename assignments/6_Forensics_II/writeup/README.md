# Writeup 6 - Forensics

Name: Sara Bittner
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sara Bittner

## Assignment Writeup

### Part 1 (45 Pts)

1. Warmup: what IP address has been attacked?
The initial get request is to 185.199.110.153 but I think the IP address that is getting hacked is 159.203.113.181

2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

There are many TCP requests to lots of different ports, so they are most likely doing an nmap attack.

3. What are the hackers' IP addresses, and where are they connecting from?
The hacker IP is 142.93.136.81 from port 55914 since they seem to use this IP for all of the connections they make.

4. What port are they using to steal files on the server?
The port that finally gives them a 220 response is port 21.

5. Which file did they steal? What kind of file is it? Provide all metadata on the file. Specifically,
The file that they stole was fine_me.jpeg

    a) What kind of file is it? jpeg

    b) Where was this photo taken? Provide a country and city in your answer.

    c) When was this photo taken? Provide a timestamp in your answer. 2018:12:23 17:16:24

    d) What kind of camera took this photo? Apple Iphone 8 back camera 3.9mm

    e) How high up was this photo taken? Provide an answer in meters.

6. Which file did the attackers leave on the server?
They left a file called greetz.fpff

7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.
You should make sure that ports that don't need to be open are not open.  You should also use firewalls, as well as perhaps configuring firewalls so that they sense when someone is scanning ports and cuts them off. 

### Part 2 (55 Pts)

*Replace this text with your repsonse to our prompt for part 2!*
