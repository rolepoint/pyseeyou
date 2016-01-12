from __future__ import unicode_literals


def get_cardinal_category(num, lang):
    if lang in LOCALE_FUNCTIONS:
        return LOCALE_FUNCTIONS[lang](num)
    else:
        raise Exception()


def one_or_other(num):
    if num == 1:
        return 'one'

    return 'other'


def other(num):
    return 'other'


LOCALE_FUNCTIONS = {
    'en': one_or_other,
    'de': one_or_other,
    'it': one_or_other,
    'ja': other,
    'nl': one_or_other,
    'zh': other
}
