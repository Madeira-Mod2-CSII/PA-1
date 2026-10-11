from monoalph import PLAINTEXT_ALPHABET
from monoalph import CIPHERTEXT_ALPHABET


def encipher(message, key):
    """
    Encrypt a message using the Caesar cipher.

    Purpose:
        Shift each letter forward by key positions in the alphabet.
        Ciphertext should be in uppercase and leave nonalphabetic characters and 
        punctuation unchanged.

    Parameters:
        message: The plaintext message to encrypt; str
        key: The number of positions to shift each letter.
            Negative values shift letters backward; int

    Return Value:
        The encrypted message; int

    Examples:
        >>> encipher("abc xyz", 3)
        'DEF ABC'
        >>> encipher("xyz", 3)
        'ABC'
        >>> encipher("hello, world!", 3)
        'KHOOR, ZRUOG!'
        >>> encipher("abc", 0)
        'ABC'
        >>> encipher("abc", 3)
        'DEF'
        >>> encipher("", 3)
        ''
    """
    


def decipher(message, key):
    """
    Decrypt a message encrypted using the Caesar cipher.

    Purpose:
        Shift each letter backward by key positions in the alphabet.
        Plaintext should be in uppercase and leave nonalphabetic characters 
        and punctuation unchanged.

    Parameters:
        message: The ciphertext message to decrypt; str
        key: The shift value used during encryption; int

    Return Value:
        The decrypted plaintext message; str

    Examples:
        >>> decipher("DEF ABC", 3)
        'abc xyz'
        >>> decipher("KHOOR, ZRUOG!", 3)
        'hello, world!'
        >>> decipher("DEF", 29)
        'abc'
        >>> decipher("ZAB", -1)
        'abc'
        >>> decipher("", 3)
        ''
    """
    




