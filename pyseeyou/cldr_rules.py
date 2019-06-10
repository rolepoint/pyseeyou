import math

# ========================
# GENERATED AUTOMATICALLY
# DON'T MODIFY MANUALLY
# ========================

def cardinal_af(n, i, v, w, f, t):
    if n == 1:
        return 'one'

    return 'other'

def cardinal_ak(n, i, v, w, f, t):
    mf_n = math.floor(n) == n
    if mf_n and n >= 0 and n <= 1:
        return 'one'

    return 'other'

def cardinal_am(n, i, v, w, f, t):
    if i == 0 or n == 1:
        return 'one'

    return 'other'

def cardinal_ar(n, i, v, w, f, t):
    n100 = n % 100
    mf_n100 = math.floor(n100) == n100
    if n == 0:
        return 'zero'
    if n == 1:
        return 'one'
    if n == 2:
        return 'two'
    if mf_n100 and n100 >= 3 and n100 <= 10:
        return 'few'
    if mf_n100 and n100 >= 11 and n100 <= 99:
        return 'many'

    return 'other'

def cardinal_ast(n, i, v, w, f, t):
    if i == 1 and v == 0:
        return 'one'

    return 'other'

def cardinal_be(n, i, v, w, f, t):
    n10 = n % 10
    n100 = n % 100
    mf_n10 = math.floor(n10) == n10
    mf_n100 = math.floor(n100) == n100
    if n10 == 1 and n100 != 11:
        return 'one'
    if mf_n10 and n10 >= 2 and n10 <= 4 and mf_n100 and not (n100 >= 12 and n100 <= 14):
        return 'few'
    if n10 == 0 or mf_n10 and n10 >= 5 and n10 <= 9 or mf_n100 and n100 >= 11 and n100 <= 14:
        return 'many'

    return 'other'

def cardinal_bm(n, i, v, w, f, t):

    return 'other'

def cardinal_br(n, i, v, w, f, t):
    n10 = n % 10
    n100 = n % 100
    mf_n10 = math.floor(n10) == n10
    mf_n100 = math.floor(n100) == n100
    n1000000 = n % 1000000
    if n10 == 1 and (not (n100 == 11 or n100 == 71 or n100 == 91)):
        return 'one'
    if n10 == 2 and (not (n100 == 12 or n100 == 72 or n100 == 92)):
        return 'two'
    if (mf_n10 and n10 >= 3 and n10 <= 4 or n10 == 9) and (mf_n100 and not (n100 >= 10 and n100 <= 19) or mf_n100 and not (n100 >= 70 and n100 <= 79) or mf_n100 and not (n100 >= 90 and n100 <= 99)):
        return 'few'
    if n != 0 and n1000000 == 0:
        return 'many'

    return 'other'

def cardinal_bs(n, i, v, w, f, t):
    i10 = i % 10
    i100 = i % 100
    f10 = f % 10
    f100 = f % 100
    mf_i10 = math.floor(i10) == i10
    mf_i100 = math.floor(i100) == i100
    mf_f10 = math.floor(f10) == f10
    mf_f100 = math.floor(f100) == f100
    if v == 0 and i10 == 1 and i100 != 11 or f10 == 1 and f100 != 11:
        return 'one'
    if v == 0 and mf_i10 and i10 >= 2 and i10 <= 4 and mf_i100 and not (i100 >= 12 and i100 <= 14) or mf_f10 and f10 >= 2 and f10 <= 4 and mf_f100 and not (f100 >= 12 and f100 <= 14):
        return 'few'

    return 'other'

def cardinal_ceb(n, i, v, w, f, t):
    i10 = i % 10
    f10 = f % 10
    if v == 0 and (i == 1 or i == 2 or i == 3) or v == 0 and (not (i10 == 4 or i10 == 6 or i10 == 9)) or v != 0 and (not (f10 == 4 or f10 == 6 or f10 == 9)):
        return 'one'

    return 'other'

def cardinal_cs(n, i, v, w, f, t):
    mf_i = math.floor(i) == i
    if i == 1 and v == 0:
        return 'one'
    if mf_i and i >= 2 and i <= 4 and v == 0:
        return 'few'
    if v != 0:
        return 'many'

    return 'other'

def cardinal_cy(n, i, v, w, f, t):
    if n == 0:
        return 'zero'
    if n == 1:
        return 'one'
    if n == 2:
        return 'two'
    if n == 3:
        return 'few'
    if n == 6:
        return 'many'

    return 'other'

def cardinal_da(n, i, v, w, f, t):
    if n == 1 or t != 0 and (i == 0 or i == 1):
        return 'one'

    return 'other'

def cardinal_dsb(n, i, v, w, f, t):
    i100 = i % 100
    f100 = f % 100
    mf_i100 = math.floor(i100) == i100
    mf_f100 = math.floor(f100) == f100
    if v == 0 and i100 == 1 or f100 == 1:
        return 'one'
    if v == 0 and i100 == 2 or f100 == 2:
        return 'two'
    if v == 0 and mf_i100 and i100 >= 3 and i100 <= 4 or mf_f100 and f100 >= 3 and f100 <= 4:
        return 'few'

    return 'other'

def cardinal_ff(n, i, v, w, f, t):
    if (i == 0 or i == 1):
        return 'one'

    return 'other'

def cardinal_ga(n, i, v, w, f, t):
    mf_n = math.floor(n) == n
    if n == 1:
        return 'one'
    if n == 2:
        return 'two'
    if mf_n and n >= 3 and n <= 6:
        return 'few'
    if mf_n and n >= 7 and n <= 10:
        return 'many'

    return 'other'

def cardinal_gd(n, i, v, w, f, t):
    mf_n = math.floor(n) == n
    if (n == 1 or n == 11):
        return 'one'
    if (n == 2 or n == 12):
        return 'two'
    if (mf_n and n >= 3 and n <= 10 or mf_n and n >= 13 and n <= 19):
        return 'few'

    return 'other'

def cardinal_gv(n, i, v, w, f, t):
    i10 = i % 10
    i100 = i % 100
    if v == 0 and i10 == 1:
        return 'one'
    if v == 0 and i10 == 2:
        return 'two'
    if v == 0 and (i100 == 0 or i100 == 20 or i100 == 40 or i100 == 60 or i100 == 80):
        return 'few'
    if v != 0:
        return 'many'

    return 'other'

def cardinal_he(n, i, v, w, f, t):
    n10 = n % 10
    mf_n = math.floor(n) == n
    if i == 1 and v == 0:
        return 'one'
    if i == 2 and v == 0:
        return 'two'
    if v == 0 and mf_n and not (n >= 0 and n <= 10) and n10 == 0:
        return 'many'

    return 'other'

def cardinal_is(n, i, v, w, f, t):
    i10 = i % 10
    i100 = i % 100
    if t == 0 and i10 == 1 and i100 != 11 or t != 0:
        return 'one'

    return 'other'

def cardinal_iu(n, i, v, w, f, t):
    if n == 1:
        return 'one'
    if n == 2:
        return 'two'

    return 'other'

def cardinal_ksh(n, i, v, w, f, t):
    if n == 0:
        return 'zero'
    if n == 1:
        return 'one'

    return 'other'

def cardinal_kw(n, i, v, w, f, t):
    n100 = n % 100
    n1000 = n % 1000
    n100000 = n % 100000
    n1000000 = n % 1000000
    mf_n100000 = math.floor(n100000) == n100000
    if n == 0:
        return 'zero'
    if n == 1:
        return 'one'
    if (n100 == 2 or n100 == 22 or n100 == 42 or n100 == 62 or n100 == 82) or n1000 == 0 and (mf_n100000 and n100000 >= 1000 and n100000 <= 20000 or n100000 == 40000 or n100000 == 60000 or n100000 == 80000) or n != 0 and n1000000 == 100000:
        return 'two'
    if (n100 == 3 or n100 == 23 or n100 == 43 or n100 == 63 or n100 == 83):
        return 'few'
    if n != 1 and (n100 == 1 or n100 == 21 or n100 == 41 or n100 == 61 or n100 == 81):
        return 'many'

    return 'other'

def cardinal_lag(n, i, v, w, f, t):
    if n == 0:
        return 'zero'
    if (i == 0 or i == 1) and n != 0:
        return 'one'

    return 'other'

def cardinal_lt(n, i, v, w, f, t):
    n10 = n % 10
    n100 = n % 100
    mf_n100 = math.floor(n100) == n100
    mf_n10 = math.floor(n10) == n10
    if n10 == 1 and mf_n100 and not (n100 >= 11 and n100 <= 19):
        return 'one'
    if mf_n10 and n10 >= 2 and n10 <= 9 and mf_n100 and not (n100 >= 11 and n100 <= 19):
        return 'few'
    if f != 0:
        return 'many'

    return 'other'

def cardinal_lv(n, i, v, w, f, t):
    n10 = n % 10
    n100 = n % 100
    f100 = f % 100
    mf_n100 = math.floor(n100) == n100
    mf_f100 = math.floor(f100) == f100
    f10 = f % 10
    if n10 == 0 or mf_n100 and n100 >= 11 and n100 <= 19 or v == 2 and mf_f100 and f100 >= 11 and f100 <= 19:
        return 'zero'
    if n10 == 1 and n100 != 11 or v == 2 and f10 == 1 and f100 != 11 or v != 2 and f10 == 1:
        return 'one'

    return 'other'

def cardinal_mk(n, i, v, w, f, t):
    i10 = i % 10
    i100 = i % 100
    f10 = f % 10
    f100 = f % 100
    if v == 0 and i10 == 1 and i100 != 11 or f10 == 1 and f100 != 11:
        return 'one'

    return 'other'

def cardinal_mo(n, i, v, w, f, t):
    n100 = n % 100
    mf_n100 = math.floor(n100) == n100
    if i == 1 and v == 0:
        return 'one'
    if v != 0 or n == 0 or mf_n100 and n100 >= 2 and n100 <= 19:
        return 'few'

    return 'other'

def cardinal_mt(n, i, v, w, f, t):
    n100 = n % 100
    mf_n100 = math.floor(n100) == n100
    if n == 1:
        return 'one'
    if n == 0 or mf_n100 and n100 >= 2 and n100 <= 10:
        return 'few'
    if mf_n100 and n100 >= 11 and n100 <= 19:
        return 'many'

    return 'other'

def cardinal_pl(n, i, v, w, f, t):
    i10 = i % 10
    i100 = i % 100
    mf_i10 = math.floor(i10) == i10
    mf_i100 = math.floor(i100) == i100
    if i == 1 and v == 0:
        return 'one'
    if v == 0 and mf_i10 and i10 >= 2 and i10 <= 4 and mf_i100 and not (i100 >= 12 and i100 <= 14):
        return 'few'
    if v == 0 and i != 1 and mf_i10 and i10 >= 0 and i10 <= 1 or v == 0 and mf_i10 and i10 >= 5 and i10 <= 9 or v == 0 and mf_i100 and i100 >= 12 and i100 <= 14:
        return 'many'

    return 'other'

def cardinal_pt(n, i, v, w, f, t):
    mf_i = math.floor(i) == i
    if mf_i and i >= 0 and i <= 1:
        return 'one'

    return 'other'

def cardinal_ru(n, i, v, w, f, t):
    i10 = i % 10
    i100 = i % 100
    mf_i10 = math.floor(i10) == i10
    mf_i100 = math.floor(i100) == i100
    if v == 0 and i10 == 1 and i100 != 11:
        return 'one'
    if v == 0 and mf_i10 and i10 >= 2 and i10 <= 4 and mf_i100 and not (i100 >= 12 and i100 <= 14):
        return 'few'
    if v == 0 and i10 == 0 or v == 0 and mf_i10 and i10 >= 5 and i10 <= 9 or v == 0 and mf_i100 and i100 >= 11 and i100 <= 14:
        return 'many'

    return 'other'

def cardinal_shi(n, i, v, w, f, t):
    mf_n = math.floor(n) == n
    if i == 0 or n == 1:
        return 'one'
    if mf_n and n >= 2 and n <= 10:
        return 'few'

    return 'other'

def cardinal_si(n, i, v, w, f, t):
    if (n == 0 or n == 1) or i == 0 and f == 1:
        return 'one'

    return 'other'

def cardinal_sl(n, i, v, w, f, t):
    i100 = i % 100
    mf_i100 = math.floor(i100) == i100
    if v == 0 and i100 == 1:
        return 'one'
    if v == 0 and i100 == 2:
        return 'two'
    if v == 0 and mf_i100 and i100 >= 3 and i100 <= 4 or v != 0:
        return 'few'

    return 'other'

def cardinal_tzm(n, i, v, w, f, t):
    mf_n = math.floor(n) == n
    if mf_n and n >= 0 and n <= 1 or mf_n and n >= 11 and n <= 99:
        return 'one'

    return 'other'

CARDINALS = {
    'af': cardinal_af,
    'ak': cardinal_ak,
    'am': cardinal_am,
    'ar': cardinal_ar,
    'ars': cardinal_ar,
    'as': cardinal_am,
    'asa': cardinal_af,
    'ast': cardinal_ast,
    'az': cardinal_af,
    'be': cardinal_be,
    'bem': cardinal_af,
    'bez': cardinal_af,
    'bg': cardinal_af,
    'bh': cardinal_ak,
    'bm': cardinal_bm,
    'bn': cardinal_am,
    'bo': cardinal_bm,
    'br': cardinal_br,
    'brx': cardinal_af,
    'bs': cardinal_bs,
    'ca': cardinal_ast,
    'ce': cardinal_af,
    'ceb': cardinal_ceb,
    'cgg': cardinal_af,
    'chr': cardinal_af,
    'ckb': cardinal_af,
    'cs': cardinal_cs,
    'cy': cardinal_cy,
    'da': cardinal_da,
    'de': cardinal_ast,
    'dsb': cardinal_dsb,
    'dv': cardinal_af,
    'dz': cardinal_bm,
    'ee': cardinal_af,
    'el': cardinal_af,
    'en': cardinal_ast,
    'eo': cardinal_af,
    'es': cardinal_af,
    'et': cardinal_ast,
    'eu': cardinal_af,
    'fa': cardinal_am,
    'ff': cardinal_ff,
    'fi': cardinal_ast,
    'fil': cardinal_ceb,
    'fo': cardinal_af,
    'fr': cardinal_ff,
    'fur': cardinal_af,
    'fy': cardinal_ast,
    'ga': cardinal_ga,
    'gd': cardinal_gd,
    'gl': cardinal_ast,
    'gsw': cardinal_af,
    'gu': cardinal_am,
    'guw': cardinal_ak,
    'gv': cardinal_gv,
    'ha': cardinal_af,
    'haw': cardinal_af,
    'he': cardinal_he,
    'hi': cardinal_am,
    'hr': cardinal_bs,
    'hsb': cardinal_dsb,
    'hu': cardinal_af,
    'hy': cardinal_ff,
    'ia': cardinal_ast,
    'id': cardinal_bm,
    'ig': cardinal_bm,
    'ii': cardinal_bm,
    'in': cardinal_bm,
    'io': cardinal_ast,
    'is': cardinal_is,
    'it': cardinal_ast,
    'iu': cardinal_iu,
    'iw': cardinal_he,
    'ja': cardinal_bm,
    'jbo': cardinal_bm,
    'jgo': cardinal_af,
    'ji': cardinal_ast,
    'jmc': cardinal_af,
    'jv': cardinal_bm,
    'jw': cardinal_bm,
    'ka': cardinal_af,
    'kab': cardinal_ff,
    'kaj': cardinal_af,
    'kcg': cardinal_af,
    'kde': cardinal_bm,
    'kea': cardinal_bm,
    'kk': cardinal_af,
    'kkj': cardinal_af,
    'kl': cardinal_af,
    'km': cardinal_bm,
    'kn': cardinal_am,
    'ko': cardinal_bm,
    'ks': cardinal_af,
    'ksb': cardinal_af,
    'ksh': cardinal_ksh,
    'ku': cardinal_af,
    'kw': cardinal_kw,
    'ky': cardinal_af,
    'lag': cardinal_lag,
    'lb': cardinal_af,
    'lg': cardinal_af,
    'lkt': cardinal_bm,
    'ln': cardinal_ak,
    'lo': cardinal_bm,
    'lt': cardinal_lt,
    'lv': cardinal_lv,
    'mas': cardinal_af,
    'mg': cardinal_ak,
    'mgo': cardinal_af,
    'mk': cardinal_mk,
    'ml': cardinal_af,
    'mn': cardinal_af,
    'mo': cardinal_mo,
    'mr': cardinal_af,
    'ms': cardinal_bm,
    'mt': cardinal_mt,
    'my': cardinal_bm,
    'nah': cardinal_af,
    'naq': cardinal_iu,
    'nb': cardinal_af,
    'nd': cardinal_af,
    'ne': cardinal_af,
    'nl': cardinal_ast,
    'nn': cardinal_af,
    'nnh': cardinal_af,
    'no': cardinal_af,
    'nqo': cardinal_bm,
    'nr': cardinal_af,
    'nso': cardinal_ak,
    'ny': cardinal_af,
    'nyn': cardinal_af,
    'om': cardinal_af,
    'or': cardinal_af,
    'os': cardinal_af,
    'pa': cardinal_ak,
    'pap': cardinal_af,
    'pl': cardinal_pl,
    'prg': cardinal_lv,
    'ps': cardinal_af,
    'pt': cardinal_pt,
    'pt-PT': cardinal_ast,
    'rm': cardinal_af,
    'ro': cardinal_mo,
    'rof': cardinal_af,
    'root': cardinal_bm,
    'ru': cardinal_ru,
    'rwk': cardinal_af,
    'sah': cardinal_bm,
    'saq': cardinal_af,
    'sc': cardinal_ast,
    'scn': cardinal_ast,
    'sd': cardinal_af,
    'sdh': cardinal_af,
    'se': cardinal_iu,
    'seh': cardinal_af,
    'ses': cardinal_bm,
    'sg': cardinal_bm,
    'sh': cardinal_bs,
    'shi': cardinal_shi,
    'si': cardinal_si,
    'sk': cardinal_cs,
    'sl': cardinal_sl,
    'sma': cardinal_iu,
    'smi': cardinal_iu,
    'smj': cardinal_iu,
    'smn': cardinal_iu,
    'sms': cardinal_iu,
    'sn': cardinal_af,
    'so': cardinal_af,
    'sq': cardinal_af,
    'sr': cardinal_bs,
    'ss': cardinal_af,
    'ssy': cardinal_af,
    'st': cardinal_af,
    'sv': cardinal_ast,
    'sw': cardinal_ast,
    'syr': cardinal_af,
    'ta': cardinal_af,
    'te': cardinal_af,
    'teo': cardinal_af,
    'th': cardinal_bm,
    'ti': cardinal_ak,
    'tig': cardinal_af,
    'tk': cardinal_af,
    'tl': cardinal_ceb,
    'tn': cardinal_af,
    'to': cardinal_bm,
    'tr': cardinal_af,
    'ts': cardinal_af,
    'tzm': cardinal_tzm,
    'ug': cardinal_af,
    'uk': cardinal_ru,
    'ur': cardinal_ast,
    'uz': cardinal_af,
    've': cardinal_af,
    'vi': cardinal_bm,
    'vo': cardinal_af,
    'vun': cardinal_af,
    'wa': cardinal_ak,
    'wae': cardinal_af,
    'wo': cardinal_bm,
    'xh': cardinal_af,
    'xog': cardinal_af,
    'yi': cardinal_ast,
    'yo': cardinal_bm,
    'yue': cardinal_bm,
    'zh': cardinal_bm,
    'zu': cardinal_am
}

# ================================
# END AUTOMATICALLY GENERATED CODE
# ================================
