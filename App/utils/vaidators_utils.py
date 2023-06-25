import re


def isValidEmail(email : str) -> bool:
    pattern : str = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)