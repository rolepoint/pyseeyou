from __future__ import unicode_literals

LOCALE_SEP = "-"


# Ported from https://github.com/format-message/format-message/blob/master/packages/lookup-closest-locale/index.js#L4-L15
def lookup_closest_locale(locale, available):
    if isinstance(locale, str) and locale in available:
        return locale

    locales = []
    if isinstance(locale, list):
        locales = [] + locale
    else:
        locales.append(locale)

    for i in range(len(locales)):
        current = locales[i].split(LOCALE_SEP)
        while len(current) != 0:
            candidate = LOCALE_SEP.join(current)
            if candidate in available:
                return candidate

            current.pop()


def get_cardinal_category(num_string, locale):
    n, i, v, w, f, t = get_parts_of_num(num_string)

    closest_locale = lookup_closest_locale(locale, cardinals)

    if not closest_locale:
        # Fallback to default locale
        locale = "en"

    cardinal_func = cardinals[closest_locale]

    if not cardinal_func:
        # Should be here different error message?
        raise Exception(f'Locale "{locale}" not supported')

    return cardinal_func(n, i, v, w, f, t);


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

    decimal_split = str(num_string).split('.')
    i = abs(int(decimal_split[0]))

    if len(decimal_split) != 2:
        n = int(num_string)
        return n, i, 0, 0, 0, 0

    n = float(num_string)

    decimal_part = decimal_split[1]
    v = len(decimal_part)
    f = int(decimal_part)

    dec_part_no_trailing_zeros = decimal_part.rstrip('0')
    if not dec_part_no_trailing_zeros:
        return n, i, v, 0, f, 0

    w = len(dec_part_no_trailing_zeros)
    t = int(dec_part_no_trailing_zeros)

    return n, i, v, w, f, t


# =================
# CODE BY GENERATOR
# =================

cardinals = {}


def cardinal_af(n, i, v, w, f, t):
    if n == 1:
        return "one"

    return "other"


cardinals["af"] = cardinal_af


def cardinal_ak(n, i, v, w, f, t):
    if (n >= 0 and n <= 1):
        return "one"

    return "other"


cardinals["ak"] = cardinal_ak


def cardinal_am(n, i, v, w, f, t):
    if i == 0 or n == 1:
        return "one"

    return "other"


cardinals["am"] = cardinal_am


def cardinal_ar(n, i, v, w, f, t):
    n100 = n % 100
    if n == 0:
        return "zero"
    elif n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif (n100 >= 3 and n100 <= 10):
        return "few"
    elif (n100 >= 11 and n100 <= 99):
        return "many"

    return "other"


cardinals["ar"] = cardinal_ar

cardinals["ars"] = cardinal_ar

cardinals["as"] = cardinal_am

cardinals["asa"] = cardinal_af


def cardinal_ast(n, i, v, w, f, t):
    if i == 1 and v == 0:
        return "one"

    return "other"


cardinals["ast"] = cardinal_ast

cardinals["az"] = cardinal_af


def cardinal_be(n, i, v, w, f, t):
    n10 = n % 10
    n100 = n % 100
    if n10 == 1 and n100 != 11:
        return "one"
    elif (n10 >= 2 and n10 <= 4) and not (n100 >= 12 and n100 <= 14):
        return "few"
    elif n10 == 0 or (n10 >= 5 and n10 <= 9) or (n100 >= 11 and n100 <= 14):
        return "many"

    return "other"


cardinals["be"] = cardinal_be

cardinals["bem"] = cardinal_af

cardinals["bez"] = cardinal_af

cardinals["bg"] = cardinal_af

cardinals["bh"] = cardinal_ak


def cardinal_bm(n, i, v, w, f, t):
    return "other"


cardinals["bm"] = cardinal_bm

cardinals["bn"] = cardinal_am

cardinals["bo"] = cardinal_bm


def cardinal_br(n, i, v, w, f, t):
    n10 = n % 10
    n100 = n % 100
    n1000000 = n % 1000000
    if n10 == 1 and n100 != 11 or n100 != 71 or n100 != 91:
        return "one"
    elif n10 == 2 and n100 != 12 or n100 != 72 or n100 != 92:
        return "two"
    elif (n10 >= 3 and n10 <= 4) or n10 == 9 and not (n100 >= 10 and n100 <= 19) or not (
            n100 >= 70 and n100 <= 79) or not (n100 >= 90 and n100 <= 99):
        return "few"
    elif n != 0 and n1000000 == 0:
        return "many"

    return "other"


cardinals["br"] = cardinal_br

cardinals["brx"] = cardinal_af


def cardinal_bs(n, i, v, w, f, t):
    i10 = i % 10
    i100 = i % 100
    f10 = f % 10
    f100 = f % 100
    if v == 0 and i10 == 1 and i100 != 11 or f10 == 1 and f100 != 11:
        return "one"
    elif v == 0 and (i10 >= 2 and i10 <= 4) and not (i100 >= 12 and i100 <= 14) or (f10 >= 2 and f10 <= 4) and not (
            f100 >= 12 and f100 <= 14):
        return "few"

    return "other"


cardinals["bs"] = cardinal_bs

cardinals["ca"] = cardinal_ast

cardinals["ce"] = cardinal_af

cardinals["cgg"] = cardinal_af

cardinals["chr"] = cardinal_af

cardinals["ckb"] = cardinal_af


def cardinal_cs(n, i, v, w, f, t):
    if i == 1 and v == 0:
        return "one"
    elif (i >= 2 and i <= 4) and v == 0:
        return "few"
    elif v != 0:
        return "many"

    return "other"


cardinals["cs"] = cardinal_cs


def cardinal_cy(n, i, v, w, f, t):
    if n == 0:
        return "zero"
    elif n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n == 3:
        return "few"
    elif n == 6:
        return "many"

    return "other"


cardinals["cy"] = cardinal_cy


def cardinal_da(n, i, v, w, f, t):
    if n == 1 or t != 0 and i == 0 or i == 1:
        return "one"

    return "other"


cardinals["da"] = cardinal_da

cardinals["de"] = cardinal_ast


def cardinal_dsb(n, i, v, w, f, t):
    i100 = i % 100
    f100 = f % 100
    if v == 0 and i100 == 1 or f100 == 1:
        return "one"
    elif v == 0 and i100 == 2 or f100 == 2:
        return "two"
    elif v == 0 and (i100 >= 3 and i100 <= 4) or (f100 >= 3 and f100 <= 4):
        return "few"

    return "other"


cardinals["dsb"] = cardinal_dsb

cardinals["dv"] = cardinal_af

cardinals["dz"] = cardinal_bm

cardinals["ee"] = cardinal_af

cardinals["el"] = cardinal_af

cardinals["en"] = cardinal_ast

cardinals["eo"] = cardinal_af

cardinals["es"] = cardinal_af

cardinals["et"] = cardinal_ast

cardinals["eu"] = cardinal_af

cardinals["fa"] = cardinal_am


def cardinal_ff(n, i, v, w, f, t):
    if i == 0 or i == 1:
        return "one"

    return "other"


cardinals["ff"] = cardinal_ff

cardinals["fi"] = cardinal_ast


def cardinal_fil(n, i, v, w, f, t):
    i10 = i % 10
    f10 = f % 10
    if v == 0 and i == 1 or i == 2 or i == 3 or v == 0 and i10 != 4 or i10 != 6 or i10 != 9 or v != 0 and f10 != 4 or f10 != 6 or f10 != 9:
        return "one"

    return "other"


cardinals["fil"] = cardinal_fil

cardinals["fo"] = cardinal_af

cardinals["fr"] = cardinal_ff

cardinals["fur"] = cardinal_af

cardinals["fy"] = cardinal_ast


def cardinal_ga(n, i, v, w, f, t):
    if n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif (n >= 3 and n <= 6):
        return "few"
    elif (n >= 7 and n <= 10):
        return "many"

    return "other"


cardinals["ga"] = cardinal_ga


def cardinal_gd(n, i, v, w, f, t):
    if n == 1 or n == 11:
        return "one"
    elif n == 2 or n == 12:
        return "two"
    elif (n >= 3 and n <= 10) or (n >= 13 and n <= 19):
        return "few"

    return "other"


cardinals["gd"] = cardinal_gd

cardinals["gl"] = cardinal_ast

cardinals["gsw"] = cardinal_af

cardinals["gu"] = cardinal_am

cardinals["guw"] = cardinal_ak


def cardinal_gv(n, i, v, w, f, t):
    i10 = i % 10
    i100 = i % 100
    if v == 0 and i10 == 1:
        return "one"
    elif v == 0 and i10 == 2:
        return "two"
    elif v == 0 and i100 == 0 or i100 == 20 or i100 == 40 or i100 == 60 or i100 == 80:
        return "few"
    elif v != 0:
        return "many"

    return "other"


cardinals["gv"] = cardinal_gv

cardinals["ha"] = cardinal_af

cardinals["haw"] = cardinal_af


def cardinal_he(n, i, v, w, f, t):
    n10 = n % 10
    if i == 1 and v == 0:
        return "one"
    elif i == 2 and v == 0:
        return "two"
    elif v == 0 and not (n >= 0 and n <= 10) and n10 == 0:
        return "many"

    return "other"


cardinals["he"] = cardinal_he

cardinals["hi"] = cardinal_am

cardinals["hr"] = cardinal_bs

cardinals["hsb"] = cardinal_dsb

cardinals["hu"] = cardinal_af

cardinals["hy"] = cardinal_ff

cardinals["ia"] = cardinal_ast

cardinals["id"] = cardinal_bm

cardinals["ig"] = cardinal_bm

cardinals["ii"] = cardinal_bm

cardinals["in"] = cardinal_bm

cardinals["io"] = cardinal_ast


def cardinal_is(n, i, v, w, f, t):
    i10 = i % 10
    i100 = i % 100
    if t == 0 and i10 == 1 and i100 != 11 or t != 0:
        return "one"

    return "other"


cardinals["is"] = cardinal_is

cardinals["it"] = cardinal_ast


def cardinal_iu(n, i, v, w, f, t):
    if n == 1:
        return "one"
    elif n == 2:
        return "two"

    return "other"


cardinals["iu"] = cardinal_iu

cardinals["iw"] = cardinal_he

cardinals["ja"] = cardinal_bm

cardinals["jbo"] = cardinal_bm

cardinals["jgo"] = cardinal_af

cardinals["ji"] = cardinal_ast

cardinals["jmc"] = cardinal_af

cardinals["jv"] = cardinal_bm

cardinals["jw"] = cardinal_bm

cardinals["ka"] = cardinal_af

cardinals["kab"] = cardinal_ff

cardinals["kaj"] = cardinal_af

cardinals["kcg"] = cardinal_af

cardinals["kde"] = cardinal_bm

cardinals["kea"] = cardinal_bm

cardinals["kk"] = cardinal_af

cardinals["kkj"] = cardinal_af

cardinals["kl"] = cardinal_af

cardinals["km"] = cardinal_bm

cardinals["kn"] = cardinal_am

cardinals["ko"] = cardinal_bm

cardinals["ks"] = cardinal_af

cardinals["ksb"] = cardinal_af


def cardinal_ksh(n, i, v, w, f, t):
    if n == 0:
        return "zero"
    elif n == 1:
        return "one"

    return "other"


cardinals["ksh"] = cardinal_ksh

cardinals["ku"] = cardinal_af

cardinals["kw"] = cardinal_iu

cardinals["ky"] = cardinal_af


def cardinal_lag(n, i, v, w, f, t):
    if n == 0:
        return "zero"
    elif i == 0 or i == 1 and n != 0:
        return "one"

    return "other"


cardinals["lag"] = cardinal_lag

cardinals["lb"] = cardinal_af

cardinals["lg"] = cardinal_af

cardinals["lkt"] = cardinal_bm

cardinals["ln"] = cardinal_ak

cardinals["lo"] = cardinal_bm


def cardinal_lt(n, i, v, w, f, t):
    n10 = n % 10
    n100 = n % 100
    if n10 == 1 and not (n100 >= 11 and n100 <= 19):
        return "one"
    elif (n10 >= 2 and n10 <= 9) and not (n100 >= 11 and n100 <= 19):
        return "few"
    elif f != 0:
        return "many"

    return "other"


cardinals["lt"] = cardinal_lt


def cardinal_lv(n, i, v, w, f, t):
    n10 = n % 10
    n100 = n % 100
    f100 = f % 100
    f10 = f % 10
    if n10 == 0 or (n100 >= 11 and n100 <= 19) or v == 2 and (f100 >= 11 and f100 <= 19):
        return "zero"
    elif n10 == 1 and n100 != 11 or v == 2 and f10 == 1 and f100 != 11 or v != 2 and f10 == 1:
        return "one"

    return "other"


cardinals["lv"] = cardinal_lv

cardinals["mas"] = cardinal_af

cardinals["mg"] = cardinal_ak

cardinals["mgo"] = cardinal_af


def cardinal_mk(n, i, v, w, f, t):
    i10 = i % 10
    i100 = i % 100
    f10 = f % 10
    f100 = f % 100
    if v == 0 and i10 == 1 and i100 != 11 or f10 == 1 and f100 != 11:
        return "one"

    return "other"


cardinals["mk"] = cardinal_mk

cardinals["ml"] = cardinal_af

cardinals["mn"] = cardinal_af


def cardinal_mo(n, i, v, w, f, t):
    n100 = n % 100
    if i == 1 and v == 0:
        return "one"
    elif v != 0 or n == 0 or n != 1 and (n100 >= 1 and n100 <= 19):
        return "few"

    return "other"


cardinals["mo"] = cardinal_mo

cardinals["mr"] = cardinal_am

cardinals["ms"] = cardinal_bm


def cardinal_mt(n, i, v, w, f, t):
    n100 = n % 100
    if n == 1:
        return "one"
    elif n == 0 or (n100 >= 2 and n100 <= 10):
        return "few"
    elif (n100 >= 11 and n100 <= 19):
        return "many"

    return "other"


cardinals["mt"] = cardinal_mt

cardinals["my"] = cardinal_bm

cardinals["nah"] = cardinal_af

cardinals["naq"] = cardinal_iu

cardinals["nb"] = cardinal_af

cardinals["nd"] = cardinal_af

cardinals["ne"] = cardinal_af

cardinals["nl"] = cardinal_ast

cardinals["nn"] = cardinal_af

cardinals["nnh"] = cardinal_af

cardinals["no"] = cardinal_af

cardinals["nqo"] = cardinal_bm

cardinals["nr"] = cardinal_af

cardinals["nso"] = cardinal_ak

cardinals["ny"] = cardinal_af

cardinals["nyn"] = cardinal_af

cardinals["om"] = cardinal_af

cardinals["or"] = cardinal_af

cardinals["os"] = cardinal_af

cardinals["pa"] = cardinal_ak

cardinals["pap"] = cardinal_af


def cardinal_pl(n, i, v, w, f, t):
    i10 = i % 10
    i100 = i % 100
    if i == 1 and v == 0:
        return "one"
    elif v == 0 and (i10 >= 2 and i10 <= 4) and not (i100 >= 12 and i100 <= 14):
        return "few"
    elif v == 0 and i != 1 and (i10 >= 0 and i10 <= 1) or v == 0 and (i10 >= 5 and i10 <= 9) or v == 0 and (
            i100 >= 12 and i100 <= 14):
        return "many"

    return "other"


cardinals["pl"] = cardinal_pl

cardinals["prg"] = cardinal_lv

cardinals["ps"] = cardinal_af


def cardinal_pt(n, i, v, w, f, t):
    if (i >= 0 and i <= 1):
        return "one"

    return "other"


cardinals["pt"] = cardinal_pt

cardinals["pt-PT"] = cardinal_ast

cardinals["rm"] = cardinal_af

cardinals["ro"] = cardinal_mo

cardinals["rof"] = cardinal_af

cardinals["root"] = cardinal_bm


def cardinal_ru(n, i, v, w, f, t):
    i10 = i % 10
    i100 = i % 100
    if v == 0 and i10 == 1 and i100 != 11:
        return "one"
    elif v == 0 and (i10 >= 2 and i10 <= 4) and not (i100 >= 12 and i100 <= 14):
        return "few"
    elif v == 0 and i10 == 0 or v == 0 and (i10 >= 5 and i10 <= 9) or v == 0 and (i100 >= 11 and i100 <= 14):
        return "many"

    return "other"


cardinals["ru"] = cardinal_ru

cardinals["rwk"] = cardinal_af

cardinals["sah"] = cardinal_bm

cardinals["saq"] = cardinal_af

cardinals["sc"] = cardinal_ast

cardinals["scn"] = cardinal_ast

cardinals["sd"] = cardinal_af

cardinals["sdh"] = cardinal_af

cardinals["se"] = cardinal_iu

cardinals["seh"] = cardinal_af

cardinals["ses"] = cardinal_bm

cardinals["sg"] = cardinal_bm

cardinals["sh"] = cardinal_bs


def cardinal_shi(n, i, v, w, f, t):
    if i == 0 or n == 1:
        return "one"
    elif (n >= 2 and n <= 10):
        return "few"

    return "other"


cardinals["shi"] = cardinal_shi


def cardinal_si(n, i, v, w, f, t):
    if n == 0 or n == 1 or i == 0 and f == 1:
        return "one"

    return "other"


cardinals["si"] = cardinal_si

cardinals["sk"] = cardinal_cs


def cardinal_sl(n, i, v, w, f, t):
    i100 = i % 100
    if v == 0 and i100 == 1:
        return "one"
    elif v == 0 and i100 == 2:
        return "two"
    elif v == 0 and (i100 >= 3 and i100 <= 4) or v != 0:
        return "few"

    return "other"


cardinals["sl"] = cardinal_sl

cardinals["sma"] = cardinal_iu

cardinals["smi"] = cardinal_iu

cardinals["smj"] = cardinal_iu

cardinals["smn"] = cardinal_iu

cardinals["sms"] = cardinal_iu

cardinals["sn"] = cardinal_af

cardinals["so"] = cardinal_af

cardinals["sq"] = cardinal_af

cardinals["sr"] = cardinal_bs

cardinals["ss"] = cardinal_af

cardinals["ssy"] = cardinal_af

cardinals["st"] = cardinal_af

cardinals["sv"] = cardinal_ast

cardinals["sw"] = cardinal_ast

cardinals["syr"] = cardinal_af

cardinals["ta"] = cardinal_af

cardinals["te"] = cardinal_af

cardinals["teo"] = cardinal_af

cardinals["th"] = cardinal_bm

cardinals["ti"] = cardinal_ak

cardinals["tig"] = cardinal_af

cardinals["tk"] = cardinal_af

cardinals["tl"] = cardinal_fil

cardinals["tn"] = cardinal_af

cardinals["to"] = cardinal_bm

cardinals["tr"] = cardinal_af

cardinals["ts"] = cardinal_af


def cardinal_tzm(n, i, v, w, f, t):
    if (n >= 0 and n <= 1) or (n >= 11 and n <= 99):
        return "one"

    return "other"


cardinals["tzm"] = cardinal_tzm

cardinals["ug"] = cardinal_af

cardinals["uk"] = cardinal_ru

cardinals["ur"] = cardinal_ast

cardinals["uz"] = cardinal_af

cardinals["ve"] = cardinal_af

cardinals["vi"] = cardinal_bm

cardinals["vo"] = cardinal_af

cardinals["vun"] = cardinal_af

cardinals["wa"] = cardinal_ak

cardinals["wae"] = cardinal_af

cardinals["wo"] = cardinal_bm

cardinals["xh"] = cardinal_af

cardinals["xog"] = cardinal_af

cardinals["yi"] = cardinal_ast

cardinals["yo"] = cardinal_bm

cardinals["yue"] = cardinal_bm

cardinals["zh"] = cardinal_bm

cardinals["zu"] = cardinal_am

# =====================
# END CODE BY GENERATOR
# =====================