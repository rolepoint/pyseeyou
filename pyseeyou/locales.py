from __future__ import unicode_literals


def get_cardinal_category(num_string, lang):
    if lang in LOCALE_FUNCTIONS:
        return LOCALE_FUNCTIONS[lang](num_string)
    else:
        raise Exception()


def get_parts_of_num(num_string):
    '''
    Gets the different parts of a number in order to calculate which plurality
    rule to apply.

    Parts are specified at this URL:
    http://unicode.org/reports/tr35/tr35-numbers.html#Operands

    :returns:
        n: absolute value of the source number (integer and decimals).
        i: integer digits of n.
        v: number of visible fraction digits in n, with trailing zeros.
        w: number of visible fraction digits in n, without trailing zeros.
        f: visible fractional digits in n, with trailing zeros.
        t: visible fractional digits in n, without trailing zeros.
    '''
    n = num_string

    decimal_split = n.split('.')
    i = int(decimal_split[0])

    if len(decimal_split) != 2:
        return n, i, 0, 0, 0, 0

    decimal_part = decimal_split[1]
    v = len(decimal_part)
    f = int(decimal_part)

    dec_part_no_trailing_zeros = decimal_part.rstrip('0')
    if not dec_part_no_trailing_zeros:
        return n, i, v, 0, f, 0

    w = len(dec_part_no_trailing_zeros)
    t = int(dec_part_no_trailing_zeros)

    return n, i, v, w, f, t


def one_or_other(num_string):
    n, i, v, w, f, t = get_parts_of_num(num_string)

    if i == 1 and v == 0:
        return 'one'

    return 'other'


def other(num_string):
    n, i, v, w, f, t = get_parts_of_num(num_string)

    return 'other'


LOCALE_FUNCTIONS = {
    'en': one_or_other,
    'de': one_or_other,
    'it': one_or_other,
    'ja': other,
    'nl': one_or_other,
    'zh': other
}
