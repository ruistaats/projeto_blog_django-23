from random import SystemRandom
import string
from django.utils.text import slugify


def random_letters(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_letters + string.digits, k=k
    ))


def slugfy_new(text, k=5):
    return slugify(text) + '-' + random_letters(k)

# print(slugfy_new('bla bal bla atenção'))
