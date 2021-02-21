"""
Default configuration for cipher.
It can be extended by adding new ciphers.
"""
from ciphers.algo import caeser, atbash

CIPHER_OPTIONS = {
    "Atbash": {
        "example": "Sld wl blf hloev zmb vjfzgrlm?",
        "requires_key": False,
        "fn": atbash,
    },
    "Caeser": {
        "example": "Zhygvcyl obgu fvqrf ol mreb.",
        "requires_key": True,
        "key": 13,
        "fn": caeser,
    },
}
