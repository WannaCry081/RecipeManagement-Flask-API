from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits
)
from random import choice


def secretKeyGenerator(keyLength : int) -> str:

    symbols : str = ascii_lowercase + ascii_uppercase + digits
    secretKey : str = "".join([ choice(symbols) for i in range(keyLength)])
    return secretKey
