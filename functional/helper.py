import random
import string

_domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
_letters = string.ascii_lowercase
_digits = string.digits
_passwords = string.hexdigits


def get_random_domain(_domains):
    return random.choice(_domains)


def get_random_digit(length):
    return ''.join(random.choice(_digits) for i in range(length))


def get_random_name(length):
    return ''.join(random.choice(_letters) for i in range(length))


def get_random_password(length):
    return ''.join(random.choice(_passwords) for i in range(length))


def generate_random_email(length):
    return [get_random_name(length) + '@' + get_random_domain(_domains)]
