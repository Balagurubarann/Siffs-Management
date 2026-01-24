from string import ascii_letters, digits
from secrets import choice

def generate_password() -> str:

    characters = "ABCDEFabcdef" + digits

    return "".join(choice(characters) for _ in range(10))

def generate_accno() -> str:

    prefix = "614809"
    suffix = "".join(choice(digits) for _ in range(7))

    return prefix + suffix
