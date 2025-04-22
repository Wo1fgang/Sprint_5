import random
import secrets
import string


def generate_login():
    return f'Sergey_Podlesov_20_{random.randint(100, 999)}@yandex.ru'


def generate_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))
    return password


def generate_invalid_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(5))
    return password
