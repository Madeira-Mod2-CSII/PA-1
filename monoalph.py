
PLAINTEXT_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
CIPHERTEXT_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def monoalph(keyword):
    """
    Construct a plaintext-to-ciphertext substitution dictionary.

    Purpose:
        Construct a monoalphabetic substitution alphabet from a keyword.
        Repeated letters in the keyword are removed, preserving their
        first occurrence. The remaining letters of the alphabet are
        appended in alphabetical order.

    Parameters:
        keyword: The keyword used to construct the cipher alphabet; str

    Return Value:
        A dictionary mapping each plaintext letter to its
        corresponding ciphertext letter; dict

    Examples:
        >>> cipher = monoalph("SECRET")
        >>> cipher["a"]
        'S'
        >>> cipher["b"]
        'E'
        >>> cipher["z"]
        'Y'
        >>> len(cipher)
        26
        >>> len(set(cipher.values()))
        26
    """
    keyword = keyword.upper()
    cipher_key = ""

    for letter in keyword + CIPHERTEXT_ALPHABET:
        if letter in CIPHERTEXT_ALPHABET and letter not in cipher_key:
            cipher_key += letter

    return dict(zip(PLAINTEXT_ALPHABET, cipher_key))

def decipher_dict(cipher_dict):
    """
    Construct the inverse of a substitution dictionary.

    Purpose:
        Reverse a plaintext-to-ciphertext dictionary so that ciphertext
        letters map back to their corresponding plaintext letters.

    Parameters:
        cipher_dict: A dictionary mapping plaintext letters
            to ciphertext letters; dict

    Return Value:
        A dictionary mapping ciphertext letters to plaintext
        letters; dict

    Examples:
        >>> cipher = monoalph("SECRET")
        >>> decipher = decipher_dict(cipher)
        >>> decipher["S"]
        'a'
        >>> decipher["E"]
        'b'
        >>> decipher["Y"]
        'z'
        >>> len(decipher)
        26
    """
    

def encipher(message, cipher_dict):
    """
    Encrypt a message using a substitution dictionary.

    Purpose:
        Replace each uppercase or lowercase letter in the message
        according to the substitution dictionary. Preserve the case
        of letters and leave nonalphabetic characters unchanged.

    Parameters:
        message: The plaintext message to encrypt; str
        cipher_dict: A dictionary mapping uppercase plaintext
            letters to uppercase ciphertext letters; dict

    Return Value:
        The encrypted message; str

    Examples:
        >>> cipher = monoalph("SECRET")
        >>> encipher("abc", cipher)
        'SEC'
        >>> encipher("hello, world!", cipher)
        'ITSSG, VGKST!'
        >>> encipher("python 123!", cipher)
        'PZTSGN 123!'
        >>> encipher("", cipher)
        ''
    """
    

def decipher(message, cipher_dict):
    """
    Decrypt a message using a substitution dictionary.

    Purpose:
        Reverse a monoalphabetic substitution by constructing the
        inverse dictionary and applying it to the ciphertext.

    Parameters:
        message: The ciphertext message to decrypt; str
        cipher_dict: A dictionary mapping plaintext letters
            to ciphertext letters; dict

    Return Value:
        The decrypted plaintext message; str

    Examples:
        >>> cipher = monoalph("SECRET")
        >>> decipher("SEC", cipher)
        'abc'
        >>> decipher("ITSSG, VGKST!", cipher)
        'hello, world!'
        >>> decipher("PZTSGN 123!", cipher)
        'python 123!'
        >>> decipher("", cipher)
        ''
    """

