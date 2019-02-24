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


def arabic(n, i, v, w, f, t):
    if n == 0:
        return "zero"
    if n == 1:
        return "one"
    if n == 2:
        return 'two'
    if i == n:
        n100 = i % 100
        if 3 <= n100 <= 10:
            return "few"
        if 11 <= n100 <= 99:
            return "many"
    return "other"


def croatian(n, i, v, w, f, t):
    v0 = i > 10
    i10 = i % 10
    i100 = i % 100
    f10 = w % 10
    f100 = w % 100

    if v0 and i10 == 1 and i100 != 11 or f10 == 1 and f100 != 11:
        return "one"
    if v0 and (2 <= i10 <= 4) and (i100 < 12 or i100 > 14) or 2 <= f10 <= 4 or (f100 < 12 or f100 > 14):
        return "few"

    return "other"


def danish(n, i, v, w, f, t):
    if n == 1 or (not (i == n)) and (i == 0 or i == 1):
        return "one"
    return "other"


def hebrew(n, i, v, w, f, t):
    if v != 0:
        return 'other'
    if n == 1:
        return "one"
    if i == 2:
        return "two"
    if (n < 0 or n > 10) and i % 10 == 0:
        return "many"
    return "other"


def hungarian(n, i, v, w, f, t):
    if n == 1 or n == 5:
        return "one"
    return "other"

def lithuanian(n, i, v, w, f, t):

    n10 = n % 10
    n100 = n % 100

    if n10 == 1 and (n100 < 11 or n100 > 19) and v == 0:
        return "one"
    if 2 <= n10 <= 9 and (n100 < 11 or n100 > 19) and v == 0:
        return "few"
    if v != 0:
        return "many"

    return "other"


def polish(n, i, v, w, f, t):
    if v != 0:
        return "other"
    if n == 1:
        return "one"
    i10 = i % 10
    i100 = i % 100
    if (2 <= i10 <= 4) and (i100 < 12 or i100 > 14):
        return "few"
    if i != 1 and (i10 == 0 or i10 == 1) or (5 <= i10 <= 9) or (12 <= i100 <= 14):
        return "many"

    return "other"

def romanian(n, i, v, w, f, t):
    if n==1:
        return "one"
    n100=n % 100
    if v != 0 or n==0 or n!=1 and (1 <= n100 <= 19):
        return "few"
    return "other"

def russian(n, i, v, w, f, t):
    if v != 0:
        return 'other'
    i10 = i % 10
    i100 = i % 100
    if i10 == 1 and i100 != 11:
        return "one"
    
    if (2 <= i10 <= 4) and (i100 < 12 or i100 > 14):
        return "few"
    if i10 == 0 or (5 <= i10 <= 9) or  (11 <= i100 <= 14):
        return "many"
    return "other"


def swedish(n, i, v, w, f, t):
    if v != 0:
        return "other"
    n10 = i % 10
    n100 = i % 100
    if (n10 == 1 or n10 == 2) and n100 != 11 and n100 != 12:
        return "one"
    return "other"


LOCALE_FUNCTIONS = {
    'ar': arabic,
    'cs': czech,
    'da': danish,
    'de': one_or_other,
    'en': one_or_other,
    'fi': one_or_other,
    'el': one_or_other,
    'fr': french,
    'he': hebrew,
    'hu': hungarian,
    'hr': croatian,
    'id': other,
    'it': one_or_other,
    'ja': other,
    'ko': other,
    'lt': lithuanian,
    'nl': one_or_other,
    'pl': polish,
    'ro': romanian,
    'ru': russian,
    'pt': brazilian_pt,
    'pt_PT': one_or_other,
    'sv': swedish,
    'tr': one_or_other,
    'zh': other,
    'es': spanish,
}
