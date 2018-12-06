from __future__ import unicode_literals


def get_cardinal_category(num_string, lang):
    n, i, v, w, f, t = get_parts_of_num(num_string)

    if lang in LOCALE_FUNCTIONS:
        return LOCALE_FUNCTIONS[lang](n, i, v, w, f, t)
    else:
        raise Exception('Unknown locale code.')


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


def brazilian_pt(n, i, v, w, f, t):
    if 0 <= i < 2 and f == 0:
        return 'one'

    return 'other'


def czech(n, i, v, w, f, t):
    if i == 1 and v == 0:
        return 'one'

    if 2 <= i <= 4 and v == 0:
        return 'few'

    if v != 0:
        return 'many'

    return 'other'


def french(n, i, v, w, f, t):
    if i == 0 or i == 1:
        return 'one'

    return 'other'


def one_or_other(n, i, v, w, f, t):
    if i == 1 and v == 0:
        return 'one'

    return 'other'


def other(n, i, v, w, f, t):
    return 'other'


def spanish(n, i, v, w, f, t):
    if i == 1 and w == 0:
        return 'one'
    return 'other'


LOCALE_FUNCTIONS = {
    'cs': czech,
    'de': one_or_other,
    'en': one_or_other,
    'fr': french,
    'it': one_or_other,
    'ja': other,
    'nl': one_or_other,
    'pt': brazilian_pt,
    'pt_PT': one_or_other,
    'zh': other,
    'es': spanish
}
