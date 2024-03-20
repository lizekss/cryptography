### Cryptography Course Assignments
This repository contains assignments completed for the Cryptography course at Free University of Tbilisi.

## Assignment 1
## Description
In this task, you are required to solve the first six challenges from [CryptoPals](https://cryptopals.com/sets/1).
The tasks are implemented in Python 3, with each challenge solved in a separate Python script named challengeX.py. 
Test data is input via stdin, and the response should be output on stdout.


## Assignment 2
## Description
This assignment consists of two parts, both implemented in Python 3.

- Task 1 - Deciphering the Block Code (60 points)
Decrypt a message (ctext.txt) received with AES-128 in CBC-mode with PKCS #7 padding and random IV.
Implement the code in decipher.py, which decrypts the message without padding to stdout.
Test your code locally using provided server setup instructions.
- Task 2 - CBC-MAC (40 points)
Attack the raw CBC-MAC to show its vulnerability for messages of different lengths.
Implement the attack in forge.py, which outputs the tag as a hex string to stdout.
Test your code locally using provided server setup instructions.


## Assignment 3
## Description
This assignment consists of two problems, both implemented in Python 3.

- Problem 1 - Meet-in-the-middle Attack on Discrete Logarithm (50 points)
Calculate the discrete logarithm in Zp*, where p is a prime number.
Implement the attack in dlog.py, which outputs the value of x to stdout.
The code should complete within 1 minute to receive points.
- Problem 2 - Forging an RSA-based Signature (50 points)
Generate signatures for 63-byte messages using a specific RSA scheme.
Implement the signature generation in sign.py, which outputs the signature to stdout.
Test your code locally using provided server setup instructions.
