"""Implements the simple deciphering algorithms."""
from string import ascii_letters


def atbash(ciphertext: str) -> str:
    """Decipher text using Atbash algorithm.

    Parameters
    ----------
    text: str
        The encrypted string to be decrypted.

    Returns
    -------
    plaintext: str
        The decrypted string
    """
    plaintext = ""
    for character in ciphertext:
        if character in ascii_letters:
            k = 25 - ascii_letters.index(character)
            if k < 0:
                k += 52
            plaintext += ascii_letters[k]
        else:
            plaintext += character
    return plaintext


def caeser(ciphertext: str, key: str = None) -> str:
    """Decipher text using Caesar algorithm.

    Parameters
    ----------
    ciphertext: str
        The encrypted string to be decrypted.

    Returns
    -------
    plaintext: str
        The decrypted string
    """
    if key is None:
        raise ValueError("key cannot be None for Caeser cipher")
    plaintext = ""
    for character in ciphertext:
        if character in ascii_letters:
            idx = ascii_letters.index(character)
            if idx > 25:
                idx = (idx + key) % 26 + 26
            else:
                idx = (idx + key) % 26
            plaintext += ascii_letters[idx]
        else:
            plaintext += character
    return plaintext
