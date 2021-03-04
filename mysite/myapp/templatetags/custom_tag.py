from django import template
from random import randint, choice
from string import ascii_letters


register = template.Library()


@register.simple_tag
def random_num():
    return randint(1, 10)


@register.simple_tag
def random_slug():
    return ''.join(choice(ascii_letters) for i in range(5, 11))
