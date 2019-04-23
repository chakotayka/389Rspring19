/*
 * Name: Sara Bittner
 * Section: 0101
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Sara Bittner
 */

/* your code goes here */
#include <stdio.h>

int main(void) {

    unsigned long a, b;  // unsigned long because dword

    a = 0xfeedface;
    b = 0x1ceb00da;

    unsigned long eax = a;
    unsigned long esi = eax;  // our second argument
    char *edi = "a = %d\n""; // our first argument
    eax= 0; //since we have 0 floating point arguments
    printf(edi, esi);

    eax = b;
    esi = eax; // our second argument
    edi = "b = %d\n"; // our first argument
    eax = 0; // since we have 0 floating point arguments
    printf(edi, esi);

    eax = b;
    a = a^eax;
    eax = a;
    b = b^eax;
    eax = b;
    a = a^eax;


    eax = a;
    esi = eax; // our second argument
    edi = "a = %d\n"; // our first argument
    eax = 0; // since we have 0 floating point arguments
    printf(edi, esi);

    eax = b;
    esi = eax; // our second argument
    edi = "b = %d\n"; // our first argument
    eax = 0; // since we have 0 floating point arguments
    printf(edi, esi);

    eax = 0;

    return 0;


}