# Writeup 3 - Operational Security and Social Engineering

Name: Sara Bittner
Section: 101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Sara Bittner

## Assignment Writeup

### Part 1 (40 pts)

Option one: Send her a link that looks like it comes from her bank (people usually have accounts in more than one bank, so let’s make this look like it’s coming from bank 2, a bank she has an account with but is not the bank she works at).  The email will say how there was a breach of atm numbers and pins and ask her to click it to reset her ATM pin and that it needs to be done immediately to prevent fraudulent withdrawals.  If she clicks it, then we can ask some “security” questions to verify that it’s her and ask, “What’s her mother’s maiden name?”, “What city was she born in?”, “What was the name of her first pet?”.  Once she answers those (and we’ll just say correct for all of them), then it’ll say enter your old ATM pin and then enter your new ATM pin.  We can check which browser she used to open the email and go to the link.

Alternatively, we can call her and pose the same scenario by pretending we are a worker at the bank.  We say that we know there has been a breach and are calling to change her ATM pin for her own protection and that we need to do it immediately so that no money is removed from her account.  We make it seem that we are helping her and that it is urgent.  First we say that we need to ask security questions to verify who she is and ask “What’s her mother’s maiden name?”, “What city was she born in?”, “What was the name of her first pet?”.    Then we can ask what her old PIN was as a last measure of authentication and then ask what she wants to change it to.  It would be harder to fit in asking what browser she primarily used but I could ask it like I was concerned about her internet safety and ask like, “In regards to safety some browsers are more safe to use to do banking.  What browser do you use?”  I would definitely make sure to continue the conversation until it came to a natural end so that it wouldn’t be suspicious.  Towards the end, I would ask questions like “Do you have any questions?” or “Is there anything else I can do for you today?”



### Part 2 (60 pts)

Vulnerability 1: Weak passwords: First of all, make it so that when employees create their passwords, they are forced to make more secure passwords.  For instance, make them include a capital, a symbol, a number, a certain amount of characters etc.  It is also helpful to educate employees on what a good password actually looks like and what passwords are considered weak.  You can show them which passwords are the most frequently used and encourage them not to use them.  People are still the weakest link so it would make sense to make the employees do multifactor authentication.  That way even if the password is weak and someone guesses it, then the attacker doesn’t automatically get in.

Vulnerability 2: Exposed ports:  It can be dangerous to have port 22 open, which they did.  If the company does not need that port to be open, they should close it.  Otherwise, you can get a firewall and only let certain IP addresses connect via that port.  To further protect your server, you could do IDS/IPS, which are Intrusion detection systems (IDS) and intrusion prevention systems (IPS).  IDS and IPS monitor the system and look for possible security incidents and stop them (https://www.juniper.net/us/en/products-services/what-is/ids-ips/).

Vulnerability 3: Using the same user name: It is probably not a good idea to use your work username as your username for things like Twitter.  This makes it easier to link someone through different accounts and learn more about them through OSINT.  This suggestion is simple.  Use different user names.


Citations:
What is IDS and IPS? (n.d.). Retrieved February 26, 2019, from https://www.juniper.net/us/en/products-services/what-is/ids-ips/
