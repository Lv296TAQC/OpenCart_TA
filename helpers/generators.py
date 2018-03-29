"""
Better implementation of generators instead of Faker plugin
"""
import random
import string

DOMAINS = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
LETTERS = string.ascii_lowercase
DIGITS = string.digits
PASSWORDS = string.hexdigits


def get_random_domain(_domains: [str]) -> [str]:
    """
    Return random domain from DOMAINS list.

    :param _domains: Incoming list with domains.
    :return: Return random domain.
    """
    return random.choice(_domains)


def get_random_digit(length: int) -> str:
    """
    Return random numeric value in string of presetted length.

    :param length: Incoming value - number of digits in string.
    :return: Return string with randomly generated digits.
    """
    return ''.join(random.choice(DIGITS) for i in range(length))


def get_random_name(length: int) -> str:
    """
    Return random string of presetted length.

    :param length: Incoming value - number of letters in string.
    :return: Return string with randomly generated letters.
    """
    return ''.join(random.choice(LETTERS) for i in range(length))


def get_random_password(length: int) -> str:
    """
    Return random alphanumeric value in string of presetted length.

    :param length: Incoming value - number of characters in string.
    :return: Return string with randomly generated characters.
    """
    return ''.join(random.choice(PASSWORDS) for i in range(length))


def generate_random_email(length: int) -> [str]:
    """
    Return random email address in string with presetted length of local-part.

    :param length: Incoming value - number of characters in generated local-name.
    :return: Return string with randomly generated email.
    """
    return [get_random_name(length) + '@' + get_random_domain(DOMAINS)]
