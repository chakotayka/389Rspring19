# Crypto II Writeup

Name: Sara Bittner
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Sara Bittner

## Assignment Writeup

### Part 1 (40 Pts)

I first tried 1337bank.money:5000/item='SELECT password from users where user = 'admin' and got ERROR: ATTEMPTED SQL INJECTION
Then tried to add a comment -- at the end of that same URL but got the same error.
I then tried to do 1337bank.money:5000/item=1 and 'SELECT password from users where user = 'admin'
In the place of that 'and' I then tried a 'or' and a ';'.
I next began playing with id = 10000 etc.  It didn't give an error so I tried negative numbers and then large numbers like 999999999999999999999999999999999999.  It still didn't give an error, just a mostly blank screen.  This was the same if I gave it a '--' or letters.
Doing something as simple as "http://1337bank.money:5000/item?id=1%20or%201=1" gave ERROR: ATTEMPTED SQL INJECTION
Doing "http://1337bank.money:5000/item?id=1';" gave Internal Service Error
I then decided to see what would happen if I did a capture with Wireshark.  I was hoping to see how much information it was sending over, but I couldn't get the live capture to give me anything resembling HTTP protocols.

I wasn't sure how the site was detecting the SQL injections so I googled ways to detect injections and tried to add 
1337bank.money:5000/item='ALTER EVENT SESSION MonitorSuspiciousErrors ON SERVER STATE = STOP; as online this was a way to monitor potential injections (although MonitorSuspiciousErrors was a name they chose).  It still gave me a "ERROR:ATTEMPTED SQL INJECTION".

I needed to figure out what was setting off the error so I tried something simple "http://1337bank.money:5000/item?id=0%20or%201=1" and still got the error.

Putting a simple ' after the url with the id sent me back to the main page.
 
I tried to insert into the table by finishing the id statement with a semicolon and then guessing how to add it into the table.  "http://1337bank.money:5000/item?id=1;%20INSERT%20INTO%20items%20values(4,%20%22TITLE%22,%20%22%22,%20%22sdfadf%22,%2056);%20--".  It didn't give me an error, simply a blank page.

After a few more attempts, it looks like when it doesn't catch the SQL injection, but the SQL injection was wrong or caused an error, it goes back to the original page. 

### Part 2 (60 Pts)

Part 1:

We just put a script tag into the search box and it executes an alert: <script>alert("hi");</script>

Part 2:

I admit that I looked at some hints for this one.  It suggested an img with an onerror of the alert.
<img src="http://isdfsd.dsf" onerror="javascript:alert('hi')"/>

Part 3:

Looking at the source code, I originally tried to close off the quotes and add in an alert(), but this didn't seem to work.   I then used what I learned from the last level of using onerror for an img src and applied that to the url.  Based on the code, it looked like it was taking in the "number" after frame and using that as the argument.  When I put in a bunch of junk in place of the 1,2, or 3 it gave back a Nan and a missing image link.  I then tried "https://xss-game.appspot.com/level3/frame#sdfasdf' onerror="javascript:alert('hi')"/>" and got through.

Part 4: 

Without looking at the code, my first thought was to try something like "https://xss-game.appspot.com/level4/frame?timer=<script>alert("hi"); </script>".
However after looking at the code it seems that it takes the input and puts it in {{}}.  With a ' the timer seems to not terminate.  With just a '); alert('hi');' the error console said that there was an unexpected string, so I assumed there must be another quotation mark lingering so I commented it out.  I put ');alert('hi'); // into the input box.  Alternatively I could have put it in the url too.

Part 5:

I first started trying some XSS in the email box, but after reading the top I suspected this was not what they were going for.  I thought the next in the URL looked strange and decided to try to work with that.  In signup.html it's used as an href for the next button. So I did something similar to the image onerror from before and did "https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert('hi')"

Part 6:

One of the hints says if you can't easily host your own file to use google.com/jsapi?callback=foo.  This made me wonder what would happen if you changed the callback to an alert and that was the answer.  https://xss-game.appspot.com/level6/frame#//google.com/jsapi?callback=alert
