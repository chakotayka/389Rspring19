# Extra Credit Writeup - Binaries II

Name: Sara Bittner
Section: 101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Sara Bittner

## Assignment Writeup

### Part 1 (100 Pts)

Flag:  CMSC389R-{0n3_st0p_l0cK_sh0P}

First I started by looking at the locker file in Binary Ninja and looking at the strings.  I saw a string that said "sorry use ida pro" so I downloaded Ida Pro and began to look at it.  Ida put it into nice boxes that cascaded down the screen.  They all seem to be somewhat like little conditionals that would just go straight to the end if they were not met.  The first few jumped if whatever was in register al was not equal to 'C', then 'M' then 'S' then 'C' then '-' and then '{' which made me feel like this was somewhat like a bunch of if statements.  Since the beginning of this looked like the flag I was looking for, I decided to look at the values used in the compares while constructing my flag.  There were however a few statements that did not plainly compare to the characters.  While I could have just tried to follow through the logic of the assembly, I instead decided to use another program called Ghidra. I let Ghidra analyze the file upon loading and then went to the section that contained these compares and jumps.  While it is usually messy, Ghidra creates its C interpretation of the assembly.   This section of locker, as expected, was a bunch of conditionals in an if statement strung together by &&'s.  For the characters that were not straightforward, I looked at this C like code.  This was still not completely straightforward or easy as there was a lot of uses of pointers and bitwise arithmetic, including and AND and an OR which are irreversible.  However with a little bit of persistance and guessing (based on what the rest of the flag looked like at that point) I was able to correctly construct the flag.

The sections that weren't just comparing the input characters to values did somewhat catch me off guard. It seemed like someone was purposely obfuscating the code in those parts.  This sometimes would happen in real life though to protect industry secrets and attempt to prevent reverse engineering.    

The least helpful tool was Binary Ninja, mostly because my free version can't break down that type of file into the graph like representation.  Ida pro was definitely the next most helpful and it would have definitely been possible to determine the flag with it.  I have had quite a bit of practice looking at binaries in another class so I imagine that I would have been able to figure it out with a bit more time and effort than using Ghidra.   However, Ghidra made looking at the binary the easiest out of all of the programs and was definitely the most helpful.  I particularly like that it tries to break the assembly into C code (although with some programs it comes across its C interpretation is just jibberish).  Another reason I might have found this the most helpful was that I was aware of its features as I had used it before.  For instance, ida might have a similar feature and I was simply unaware of it.   





![alt text](389 hw8 screenshot.png)
