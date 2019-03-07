import pytest

from pyseeyou.locales import get_parts_of_num

# ========================
# GENERATED AUTOMATICALLY
# DON'T MODIFY MANUALLY
# ========================

from pyseeyou.cldr_rules import (
    cardinal_af, cardinal_ak, cardinal_am, cardinal_ar, cardinal_ast, cardinal_be, cardinal_bm, cardinal_br, cardinal_bs, cardinal_cs, cardinal_cy, cardinal_da, cardinal_dsb, cardinal_ff, cardinal_fil, cardinal_ga, cardinal_gd, cardinal_gv, cardinal_he, cardinal_is, cardinal_iu, cardinal_ksh, cardinal_lag, cardinal_lt, cardinal_lv, cardinal_mk, cardinal_mo, cardinal_mt, cardinal_pl, cardinal_pt, cardinal_ru, cardinal_shi, cardinal_si, cardinal_sl, cardinal_tzm)

def test_cardinal_af():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ak():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ak(*get_parts_of_num(sample)) == match

def test_cardinal_am():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_am(*get_parts_of_num(sample)) == match

def test_cardinal_ar():
    assertions = [
        ('zero', ['0','0.0','0.00','0.000']),
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('few', ['3','7','10','103','107','110','1003','3.0','4.0','5.0']),
        ('many', ['11','19','26','111','1011','11.0','12.0','13.0']),
        ('other', ['100','101','102','200','201','202','300','301','302','0.1','0.5','0.9','1.1','1.4','1.7','10.1'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ar(*get_parts_of_num(sample)) == match

def test_cardinal_ars():
    assertions = [
        ('zero', ['0','0.0','0.00','0.000']),
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('few', ['3','7','10','103','107','110','1003','3.0','4.0','5.0']),
        ('many', ['11','19','26','111','1011','11.0','12.0','13.0']),
        ('other', ['100','101','102','200','201','202','300','301','302','0.1','0.5','0.9','1.1','1.4','1.7','10.1'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ar(*get_parts_of_num(sample)) == match

def test_cardinal_as():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_am(*get_parts_of_num(sample)) == match

def test_cardinal_asa():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ast():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_az():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_be():
    assertions = [
        ('one', ['1','21','31','1.0','21.0','31.0']),
        ('few', ['2','3','4','22','23','24','32','33','34','2.0','3.0','4.0']),
        ('many', ['0','5','12','19','100','0.0','5.0','6.0']),
        ('other', ['0.1','0.5','0.9','1.1','1.4','1.7','10.1'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_be(*get_parts_of_num(sample)) == match

def test_cardinal_bem():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_bez():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_bg():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_bh():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ak(*get_parts_of_num(sample)) == match

def test_cardinal_bm():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_bn():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_am(*get_parts_of_num(sample)) == match

def test_cardinal_bo():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_br():
    assertions = [
        ('one', ['1','21','31','1.0','21.0','31.0']),
        ('two', ['2','22','32','2.0','22.0','32.0']),
        ('few', ['3','4','9','3.0','4.0','9.0']),
        ('many', ['1000000','1000000.0','1000000.00','1000000.000']),
        ('other', ['0','5','7','8','10','15','20','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_br(*get_parts_of_num(sample)) == match

def test_cardinal_brx():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_bs():
    assertions = [
        ('one', ['1','21','31','0.1','1.1','2.1']),
        ('few', ['2','3','4','22','23','24','32','33','34','0.2','0.3','0.4','1.2','1.3','1.4','2.2','2.3','2.4']),
        ('other', ['0','5','12','19','100','0.0','0.5','0.75','1.0','1.5','1.75','2.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bs(*get_parts_of_num(sample)) == match

def test_cardinal_ca():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_ce():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_cgg():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_chr():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ckb():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_cs():
    assertions = [
        ('one', ['1']),
        ('few', ['2','3','4']),
        ('many', ['0.0','0.75','1.5','10.0','100.0']),
        ('other', ['0','5','12','19','100'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_cs(*get_parts_of_num(sample)) == match

def test_cardinal_cy():
    assertions = [
        ('zero', ['0','0.0','0.00','0.000']),
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('few', ['3','3.0','3.00','3.000']),
        ('many', ['6','6.0','6.00','6.000']),
        ('other', ['4','5','7','14','20','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_cy(*get_parts_of_num(sample)) == match

def test_cardinal_da():
    assertions = [
        ('one', ['1','0.1','0.85','1.6']),
        ('other', ['0','2','9','16','100','0.0','2.0','2.7','3.4','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_da(*get_parts_of_num(sample)) == match

def test_cardinal_de():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_dsb():
    assertions = [
        ('one', ['1','101','201','0.1','1.1','2.1']),
        ('two', ['2','102','202','0.2','1.2','2.2']),
        ('few', ['3','4','103','0.3','0.4','1.3']),
        ('other', ['0','5','12','19','100','0.0','0.5','0.75','1.0','1.5','1.75','2.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_dsb(*get_parts_of_num(sample)) == match

def test_cardinal_dv():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_dz():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_ee():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_el():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_en():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_eo():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_es():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_et():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_eu():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_fa():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_am(*get_parts_of_num(sample)) == match

def test_cardinal_ff():
    assertions = [
        ('one', ['0','1','0.0','0.75','1.5']),
        ('other', ['2','10','17','100','1000','2.0','2.75','3.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ff(*get_parts_of_num(sample)) == match

def test_cardinal_fi():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_fil():
    assertions = [
        ('one', ['0','2','3','5','7','0.0','0.15','0.3','0.5','0.7']),
        ('other', ['4','6','9','0.4','0.6','0.9'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_fil(*get_parts_of_num(sample)) == match

def test_cardinal_fo():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_fr():
    assertions = [
        ('one', ['0','1','0.0','0.75','1.5']),
        ('other', ['2','10','17','100','1000','2.0','2.75','3.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ff(*get_parts_of_num(sample)) == match

def test_cardinal_fur():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_fy():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_ga():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('few', ['3','5','6','3.0','4.0','5.0']),
        ('many', ['7','9','10','7.0','8.0','9.0']),
        ('other', ['0','11','18','25','100','0.0','0.45','0.9','1.1','1.35','1.6','10.1'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ga(*get_parts_of_num(sample)) == match

def test_cardinal_gd():
    assertions = [
        ('one', ['1','11','1.0','11.0','1.00']),
        ('two', ['2','12','2.0','12.0','2.00']),
        ('few', ['3','7','10','13','16','19','3.0','4.0','5.0']),
        ('other', ['0','20','27','34','100','0.0','0.45','0.9','1.1','1.35','1.6','10.1'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_gd(*get_parts_of_num(sample)) == match

def test_cardinal_gl():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_gsw():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_gu():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_am(*get_parts_of_num(sample)) == match

def test_cardinal_guw():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ak(*get_parts_of_num(sample)) == match

def test_cardinal_gv():
    assertions = [
        ('one', ['1','11','21']),
        ('two', ['2','12','22']),
        ('few', ['0','20','40']),
        ('many', ['0.0','0.75','1.5','10.0','100.0']),
        ('other', ['3','7','10','13','16','19','23'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_gv(*get_parts_of_num(sample)) == match

def test_cardinal_ha():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_haw():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_he():
    assertions = [
        ('one', ['1']),
        ('two', ['2']),
        ('many', ['20','30','40']),
        ('other', ['0','3','10','17','101','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_he(*get_parts_of_num(sample)) == match

def test_cardinal_hi():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_am(*get_parts_of_num(sample)) == match

def test_cardinal_hr():
    assertions = [
        ('one', ['1','21','31','0.1','1.1','2.1']),
        ('few', ['2','3','4','22','23','24','32','33','34','0.2','0.3','0.4','1.2','1.3','1.4','2.2','2.3','2.4']),
        ('other', ['0','5','12','19','100','0.0','0.5','0.75','1.0','1.5','1.75','2.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bs(*get_parts_of_num(sample)) == match

def test_cardinal_hsb():
    assertions = [
        ('one', ['1','101','201','0.1','1.1','2.1']),
        ('two', ['2','102','202','0.2','1.2','2.2']),
        ('few', ['3','4','103','0.3','0.4','1.3']),
        ('other', ['0','5','12','19','100','0.0','0.5','0.75','1.0','1.5','1.75','2.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_dsb(*get_parts_of_num(sample)) == match

def test_cardinal_hu():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_hy():
    assertions = [
        ('one', ['0','1','0.0','0.75','1.5']),
        ('other', ['2','10','17','100','1000','2.0','2.75','3.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ff(*get_parts_of_num(sample)) == match

def test_cardinal_ia():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_id():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_ig():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_ii():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_in():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_io():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_is():
    assertions = [
        ('one', ['1','21','31','0.1','0.85','1.6','10.1','100.1']),
        ('other', ['0','2','9','16','100','0.0','2.0','3.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_is(*get_parts_of_num(sample)) == match

def test_cardinal_it():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_iu():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_iu(*get_parts_of_num(sample)) == match

def test_cardinal_iw():
    assertions = [
        ('one', ['1']),
        ('two', ['2']),
        ('many', ['20','30','40']),
        ('other', ['0','3','10','17','101','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_he(*get_parts_of_num(sample)) == match

def test_cardinal_ja():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_jbo():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_jgo():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ji():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_jmc():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_jv():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_jw():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_ka():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_kab():
    assertions = [
        ('one', ['0','1','0.0','0.75','1.5']),
        ('other', ['2','10','17','100','1000','2.0','2.75','3.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ff(*get_parts_of_num(sample)) == match

def test_cardinal_kaj():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_kcg():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_kde():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_kea():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_kk():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_kkj():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_kl():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_km():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_kn():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_am(*get_parts_of_num(sample)) == match

def test_cardinal_ko():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_ks():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ksb():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ksh():
    assertions = [
        ('zero', ['0','0.0','0.00','0.000']),
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ksh(*get_parts_of_num(sample)) == match

def test_cardinal_ku():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_kw():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_iu(*get_parts_of_num(sample)) == match

def test_cardinal_ky():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_lag():
    assertions = [
        ('zero', ['0','0.0','0.00','0.000']),
        ('one', ['1','0.1','0.85','1.6']),
        ('other', ['2','10','17','100','1000','2.0','2.75','3.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_lag(*get_parts_of_num(sample)) == match

def test_cardinal_lb():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_lg():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_lkt():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_ln():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ak(*get_parts_of_num(sample)) == match

def test_cardinal_lo():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_lt():
    assertions = [
        ('one', ['1','21','31','1.0','21.0','31.0']),
        ('few', ['2','6','9','22','26','29','102','2.0','3.0','4.0']),
        ('many', ['0.1','0.5','0.9','1.1','1.4','1.7','10.1']),
        ('other', ['0','10','15','20','30','0.0','10.0','11.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_lt(*get_parts_of_num(sample)) == match

def test_cardinal_lv():
    assertions = [
        ('zero', ['0','10','15','20','30','0.0','10.0','11.0']),
        ('one', ['1','21','31','0.1','1.0','1.1']),
        ('other', ['2','6','9','22','26','29','102','0.2','0.55','0.9','1.2','1.55','1.9','10.2'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_lv(*get_parts_of_num(sample)) == match

def test_cardinal_mas():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_mg():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ak(*get_parts_of_num(sample)) == match

def test_cardinal_mgo():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_mk():
    assertions = [
        ('one', ['1','21','31','0.1','1.1','2.1']),
        ('other', ['0','2','9','16','100','0.0','0.2','0.6','1.0','1.2','1.45','1.7'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_mk(*get_parts_of_num(sample)) == match

def test_cardinal_ml():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_mn():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_mo():
    assertions = [
        ('one', ['1']),
        ('few', ['0','2','9','16','101','0.0','0.75','1.5','10.0','100.0']),
        ('other', ['20','28','35','100','1000'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_mo(*get_parts_of_num(sample)) == match

def test_cardinal_mr():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_am(*get_parts_of_num(sample)) == match

def test_cardinal_ms():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_mt():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('few', ['0','2','6','10','102','105','107','0.0','2.0','3.0']),
        ('many', ['11','15','19','111','114','117','1011','11.0','12.0','13.0']),
        ('other', ['20','28','35','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.1'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_mt(*get_parts_of_num(sample)) == match

def test_cardinal_my():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_nah():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_naq():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_iu(*get_parts_of_num(sample)) == match

def test_cardinal_nb():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_nd():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ne():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_nl():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_nn():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_nnh():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_no():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_nqo():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_nr():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_nso():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ak(*get_parts_of_num(sample)) == match

def test_cardinal_ny():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_nyn():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_om():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_or():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_os():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_pa():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ak(*get_parts_of_num(sample)) == match

def test_cardinal_pap():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_pl():
    assertions = [
        ('one', ['1']),
        ('few', ['2','3','4','22','23','24','32','33','34']),
        ('many', ['0','5','12','19','100']),
        ('other', ['0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_pl(*get_parts_of_num(sample)) == match

def test_cardinal_prg():
    assertions = [
        ('zero', ['0','10','15','20','30','0.0','10.0','11.0']),
        ('one', ['1','21','31','0.1','1.0','1.1']),
        ('other', ['2','6','9','22','26','29','102','0.2','0.55','0.9','1.2','1.55','1.9','10.2'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_lv(*get_parts_of_num(sample)) == match

def test_cardinal_ps():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_pt():
    assertions = [
        ('one', ['0','1','0.0','0.75','1.5']),
        ('other', ['2','10','17','100','1000','2.0','2.75','3.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_pt(*get_parts_of_num(sample)) == match

def test_cardinal_pt_PT():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_rm():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ro():
    assertions = [
        ('one', ['1']),
        ('few', ['0','2','9','16','101','0.0','0.75','1.5','10.0','100.0']),
        ('other', ['20','28','35','100','1000'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_mo(*get_parts_of_num(sample)) == match

def test_cardinal_rof():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_root():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_ru():
    assertions = [
        ('one', ['1','21','31']),
        ('few', ['2','3','4','22','23','24','32','33','34']),
        ('many', ['0','5','12','19','100']),
        ('other', ['0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ru(*get_parts_of_num(sample)) == match

def test_cardinal_rwk():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_sah():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_saq():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_sc():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_scn():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_sd():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_sdh():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_se():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_iu(*get_parts_of_num(sample)) == match

def test_cardinal_seh():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ses():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_sg():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_sh():
    assertions = [
        ('one', ['1','21','31','0.1','1.1','2.1']),
        ('few', ['2','3','4','22','23','24','32','33','34','0.2','0.3','0.4','1.2','1.3','1.4','2.2','2.3','2.4']),
        ('other', ['0','5','12','19','100','0.0','0.5','0.75','1.0','1.5','1.75','2.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bs(*get_parts_of_num(sample)) == match

def test_cardinal_shi():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('few', ['2','6','10','2.0','3.0','4.0']),
        ('other', ['11','19','26','100','1000','1.1','1.5','1.9','2.1','2.4','2.7','10.1'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_shi(*get_parts_of_num(sample)) == match

def test_cardinal_si():
    assertions = [
        ('one', ['0','1','0.0','0.1','1.0']),
        ('other', ['2','10','17','100','1000','0.2','0.55','0.9','1.1','1.45','1.8','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_si(*get_parts_of_num(sample)) == match

def test_cardinal_sk():
    assertions = [
        ('one', ['1']),
        ('few', ['2','3','4']),
        ('many', ['0.0','0.75','1.5','10.0','100.0']),
        ('other', ['0','5','12','19','100'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_cs(*get_parts_of_num(sample)) == match

def test_cardinal_sl():
    assertions = [
        ('one', ['1','101','201']),
        ('two', ['2','102','202']),
        ('few', ['3','4','103','0.0','0.75','1.5','10.0','100.0']),
        ('other', ['0','5','12','19','100'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_sl(*get_parts_of_num(sample)) == match

def test_cardinal_sma():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_iu(*get_parts_of_num(sample)) == match

def test_cardinal_smi():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_iu(*get_parts_of_num(sample)) == match

def test_cardinal_smj():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_iu(*get_parts_of_num(sample)) == match

def test_cardinal_smn():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_iu(*get_parts_of_num(sample)) == match

def test_cardinal_sms():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_iu(*get_parts_of_num(sample)) == match

def test_cardinal_sn():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_so():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_sq():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_sr():
    assertions = [
        ('one', ['1','21','31','0.1','1.1','2.1']),
        ('few', ['2','3','4','22','23','24','32','33','34','0.2','0.3','0.4','1.2','1.3','1.4','2.2','2.3','2.4']),
        ('other', ['0','5','12','19','100','0.0','0.5','0.75','1.0','1.5','1.75','2.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bs(*get_parts_of_num(sample)) == match

def test_cardinal_ss():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ssy():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_st():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_sv():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_sw():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_syr():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ta():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_te():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_teo():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_th():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_ti():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ak(*get_parts_of_num(sample)) == match

def test_cardinal_tig():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_tk():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_tl():
    assertions = [
        ('one', ['0','2','3','5','7','0.0','0.15','0.3','0.5','0.7']),
        ('other', ['4','6','9','0.4','0.6','0.9'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_fil(*get_parts_of_num(sample)) == match

def test_cardinal_tn():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_to():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_tr():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ts():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_tzm():
    assertions = [
        ('one', ['0','1','11','18','24','0.0','1.0','11.0']),
        ('other', ['2','6','10','100','103','106','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_tzm(*get_parts_of_num(sample)) == match

def test_cardinal_ug():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_uk():
    assertions = [
        ('one', ['1','21','31']),
        ('few', ['2','3','4','22','23','24','32','33','34']),
        ('many', ['0','5','12','19','100']),
        ('other', ['0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ru(*get_parts_of_num(sample)) == match

def test_cardinal_ur():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_uz():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_ve():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_vi():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_vo():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_vun():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_wa():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ak(*get_parts_of_num(sample)) == match

def test_cardinal_wae():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_wo():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_xh():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_xog():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_af(*get_parts_of_num(sample)) == match

def test_cardinal_yi():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_ast(*get_parts_of_num(sample)) == match

def test_cardinal_yo():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_yue():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_zh():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_bm(*get_parts_of_num(sample)) == match

def test_cardinal_zu():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert cardinal_am(*get_parts_of_num(sample)) == match


# ================================
# END AUTOMATICALLY GENERATED CODE
# ================================
