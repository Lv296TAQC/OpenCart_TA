import random
import string

domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase
digits = string.digits
passwords = string.hexdigits


def get_random_domain(domains):
    return random.choice(domains)


def get_random_digit(length):
    return ''.join(random.choice(digits) for i in range(length))


def get_random_name(length):
    return ''.join(random.choice(letters) for i in range(length))


def get_random_password(length):
    return ''.join(random.choice(passwords) for i in range(length))


def generate_random_email(length):
    return [get_random_name(length) + '@' + get_random_domain(domains)]
