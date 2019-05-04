# Crypto II Writeup

Name: Sara Bittner
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Sara Bittner

## Assignment Writeup

### Part 1 (70 Pts)

CMSC389R-{m3ss@g3_!n_A_b0ttl3}

screenshot in writeup/screenshot.jpg


![alt text](https://github.com/chakotayka/389Rspring19/blob/master/assignments/10_Crypto_II/writeup/screenshot.jpg)




### Part 2 (30 Pts)

ECB: 

![alt text](https://github.com/chakotayka/389Rspring19/blob/master/assignments/10_Crypto_II/ecb.bmp)


CBC:

![alt text](https://github.com/chakotayka/389Rspring19/blob/master/assignments/10_Crypto_II/cbc.bmp)


What do you notice about both pictures?

The ECB one is somewhat changed but it looks like parts that were the same color were changed similarly because you can still clearly see a circle and square like the original drawing.
However, the CBC bmp looks like a random assortment of colors. 



Which block cipher mode is less secure? Why? Explain using information about how the different block cipher modes of operation work.


ECB is less secure because you can still pick out the original picture even by just looking at it.  It is more insecure because you are taking the key and plaintext and just running it through the block cipher encryption. With the same input, this will give the same output so the same block of inputted plaintext will result in the same ciphertext, which is why we can still determine the shapes in the picture.  On the other hand CBC uses the result of the last block to XOR with the plaintext before the encryption and this adds in some more randomness to the output (at least to the naked eye). 