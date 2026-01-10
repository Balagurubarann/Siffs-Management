from string import ascii_letters, digits
from secrets import choice

def generate_password() -> str:

    characters = ascii_letters + digits

    return "".join(choice(characters) for _ in range(10))
