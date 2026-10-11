# PA-1: Classical Substitution Ciphers

We will be exploring a couple of classical cryptography algorithms. A *monoalphabetic* cipher is a cipher that substitutes a single letter of plaintext with a single letter of ciphertext. Any fixed piece of plaintext always gets mapped to the same ciphertext letter. For example, if 'r'->'Z' then the plaintext 'r' will always be 'Z' in ciphertext. 

Two examples:

- **Caesar Example:** 'cat' -> 'DBT'

- **Monoalph Example:** 'door' -> 'STTZ'

## Plaintext \& Ciphertext

The *plaintext* is the original message that is being sent. We will assume that it is only letters being enciphered. Punctuation and numbers will remain unchanged. For our context, the plaintext will always be in *lower case* characters, punctuation, and numbers.

The *ciphertext* is the enciphered text. This is what someone listening to the message traffic will encounter. Hopefully, the plaintext cannot be recovered from the ciphertext. For our situation, the ciphertext will always be *upper case* letters, numbers and punctuation.

*Note:* The characters being enciphered will be a-z. Numbers and punctuation encountered will remain the same from the plaintext to the ciphertext.

## Caesar Cipher

The Caesar cipher is an example of a shift cipher. Every letter of the alphabet a-z is assigned a number 0-25 just as we did in the discussion about error correction.

One chooses a number, between 0 and 25, as the key and then adds it to the numerical value for the number $E_k(p) = C$. For example, if $k=6$ and we want to encrypt 'cat', this corresponds to the sequence $2 0 19$. Adding the key to each we get the sequence $8 6 25$, which corresponds to the ciphertext 'I G Z'. 

*Note:* Everything must be done modulo 26. For instance, if we want to encrypt 'w' we add 6 to 22 and get 28, which is larger than 25. We take $25 \mod 26$ to get 2, so $E_6('w') = 'C'$.

Deciphering happens in reverse of enciphering. This is what's referred to as a *symmetric* cipher. Using our example above $D_6('C') = 'w'$. If we want to undo the ciphering process, we need to subtract six from the ciphertext value. Hence, $D_k(C) = p$ and subtracting $k$ is the same as adding $26-k$. This is a fact of modular arithmetic. 

*The Why:* If you're interested in why, think about a clock labeled 1 - 12. If we're at 3 o'clock and we subtract 2 hours we're at 1 o'clock. Subtracting 2 is the same as adding 10 hours to 3 o'clock.


## Substitution Cipher

A monoalphabetic substitution cipher implements a letter-for-letter substitution. One way to come up with a key, is to start with a keyword, say 'SECRET'. We delete the repeated 'E's to get 'SECRT'. We then use this to start the transformation and then shift the rest of the alphabet accordingly.

**Example:**


| plaintext | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
ciphertext | S | E | C | R | T | A | B | D | F | G | H | I | J | K | L | M | N | O | P | Q | U | V | W | X | Y | Z |

Using this key, we get

| plaintext | c | o | m | p | u | t | e | r |
|---|---|---|---|---|---|---|---|---|
| ciphertext | C | L | J | M | U | Q | T | O |


## Implementation

### ```caesar.py```

In ```caesar.py```, you will find stubs for the following functions.

- ```encipher(message, key)``` takes a plaintext message and an integer key. Returns the ciphertext yielded from the message being shifted by the key.

- ```decipher(message, key)``` this function should undo the ```encipher``` function.


### ```monoalph.py```

In ```monalph.py```, you will find stubs for the following functions:

- ```monoalph(keyword)``` takes a keyword and returns a dictionary with the plaintext ciphertext pairs, as described above, made using the keyword passed into the function. This function has already been implemented for you. In the above 'a' is mapped to 'S' so the dictionary will contain the pair ```{'a':'S'}```

*Note:* You don't need to understand how this function is implemented in order to complete the assignment.

- ```decipher(cipher_dict)``` should reverse the process from ```monoalph```. Given a dictionary of plaintext keys and ciphertext values, the dictionary returned by ```decipher``` should contain ciphertext keys and plaintext values. To reverse the pairing above, the dictionary returned by ```decipher``` will contain the pair ```{'S':'a'}```.

-```encipher(message, cipher_dict)``` should take a message and a dictionary of plaintext : ciphertext pairs and returns the ciphertext encrypted using ```cipher_dict```.

-```decipher(message, cipher_dict)``` should take the message and a dictionary of ciphertext : plaintext pairs and returns the plaintext decrypted using ```cipher_dict```.

### ```main.py```

In the ```main.py```, you will implement two functions that use the functions you implemented in ```monoalph.py``` and ```caesar.py```. This combination cipher will use both a keyword and a shift to do the encrypting and decrypting. The encipher and decipher functions look like this:

**Examples:**

We again use our keyword "secret" and a shift of 6. To encrypt the letter 'd', the steps are as follows:

1. Encrypt using the monoalph 'd' -> 'R'

2. Then use the shift adding 6 to 'r' we get 'X'

3. So, with this combination cipher 'd' is encrypted to 'X'.

To decrypt using the combination cipher, you reverse the steps:

1. Undo the shift.

2. Undo the monoalph using the inverse dictionary of the one used to encrypt.

3. Get the ciphertext.

In the example above, 'X' will be decrypted to 'd'.

- ```combo_encipher``` should encrypt the given plaitntext messsage with the keyword and shift passed as arguments using combination cipher described above.

- ```combo_decipher``` should decrypt the given ciphertext message with the keyword and shift passed as arguments using the combination cipher described above.

*Note:* In implementing the combination functions, you should call the functions you wrote in ```monoalph.py``` and ```caesar.py```.

## Technical Note: Implementation Restrictions

If you want to use concepts that we have not discussed in class, please discuss it with me first. In particular, you should not use ```map``` or ```zip``` so that you can practice using looping constructs. Please also refrain from using *list comprehensions* or *dictionary comprehensions* if you are familiar with such things. 

These restrictions aren't meant to keep you from learning advanced Python concepts, but to give you the opportunity to practice iteration, conditional logic, and using dictionaries.