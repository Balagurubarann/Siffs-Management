from string import ascii_letters, digits
from secrets import choice
from random import randint
from src.models.Product import ProductType

def generate_password() -> str:

    characters = "ABCDEFabcdef" + digits

    return "".join(choice(characters) for _ in range(10))

def generate_accno() -> str:

    prefix = "614809"
    suffix = "".join(choice(digits) for _ in range(7))

    return prefix + suffix

def generate_product_no(productType: ProductType) -> str:

    productNo = randint(7001, 9999)

    if productType == ProductType.FISH:

        productNo = randint(2000, 4000)

    if productType == ProductType.CRAB:

        productNo = randint(4001, 5500)

    if productType == ProductType.PRAWN:

        productNo = randint(5501, 7000)

    return str(productNo)
