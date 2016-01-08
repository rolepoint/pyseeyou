from __future__ import unicode_literals


def get_cardinal_category(num, lang):
    locale = globals().get(lang)
    if locale:
        return locale(num)

    else:
        raise Exception()


def en(number):
    if number == 1:
        return 'one'

    return 'other'
