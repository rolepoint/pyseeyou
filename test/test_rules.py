import pytest

from pyseeyou.locales import get_parts_of_num
from pyseeyou.cldr_rules import CARDINALS

# ========================
# GENERATED AUTOMATICALLY
# DON'T MODIFY MANUALLY
# ========================


def check(assertions, plural_fn):
    for assertion in assertions:
        match, samples = assertion
        for sample in samples:
            assert plural_fn(*get_parts_of_num(sample)) == match

def test_cardinal_af():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['af'])

def test_cardinal_ak():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    check(assertions, CARDINALS['ak'])

def test_cardinal_am():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    check(assertions, CARDINALS['am'])

def test_cardinal_ar():
    assertions = [
        ('zero', ['0','0.0','0.00','0.000']),
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('few', ['3','7','10','103','107','110','1003','3.0','4.0','5.0']),
        ('many', ['11','19','26','111','1011','11.0','12.0','13.0']),
        ('other', ['100','101','102','200','201','202','300','301','302','0.1','0.5','0.9','1.1','1.4','1.7','10.1'])
    ]

    check(assertions, CARDINALS['ar'])

def test_cardinal_ars():
    assertions = [
        ('zero', ['0','0.0','0.00','0.000']),
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('few', ['3','7','10','103','107','110','1003','3.0','4.0','5.0']),
        ('many', ['11','19','26','111','1011','11.0','12.0','13.0']),
        ('other', ['100','101','102','200','201','202','300','301','302','0.1','0.5','0.9','1.1','1.4','1.7','10.1'])
    ]

    check(assertions, CARDINALS['ars'])

def test_cardinal_as():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    check(assertions, CARDINALS['as'])

def test_cardinal_asa():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['asa'])

def test_cardinal_ast():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ast'])

def test_cardinal_az():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['az'])

def test_cardinal_be():
    assertions = [
        ('one', ['1','21','31','1.0','21.0','31.0']),
        ('few', ['2','3','4','22','23','24','32','33','34','2.0','3.0','4.0']),
        ('many', ['0','5','12','19','100','0.0','5.0','6.0']),
        ('other', ['0.1','0.5','0.9','1.1','1.4','1.7','10.1'])
    ]

    check(assertions, CARDINALS['be'])

def test_cardinal_bem():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['bem'])

def test_cardinal_bez():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['bez'])

def test_cardinal_bg():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['bg'])

def test_cardinal_bh():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    check(assertions, CARDINALS['bh'])

def test_cardinal_bm():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['bm'])

def test_cardinal_bn():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    check(assertions, CARDINALS['bn'])

def test_cardinal_bo():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['bo'])

def test_cardinal_br():
    assertions = [
        ('one', ['1','21','31','1.0','21.0','31.0']),
        ('two', ['2','22','32','2.0','22.0','32.0']),
        ('few', ['3','4','9','3.0','4.0','9.0']),
        ('many', ['1000000','1000000.0','1000000.00','1000000.000']),
        ('other', ['0','5','7','8','10','15','20','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['br'])

def test_cardinal_brx():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['brx'])

def test_cardinal_bs():
    assertions = [
        ('one', ['1','21','31','0.1','1.1','2.1']),
        ('few', ['2','3','4','22','23','24','32','33','34','0.2','0.3','0.4','1.2','1.3','1.4','2.2','2.3','2.4']),
        ('other', ['0','5','12','19','100','0.0','0.5','0.75','1.0','1.5','1.75','2.0'])
    ]

    check(assertions, CARDINALS['bs'])

def test_cardinal_ca():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ca'])

def test_cardinal_ce():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ce'])

def test_cardinal_cgg():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['cgg'])

def test_cardinal_chr():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['chr'])

def test_cardinal_ckb():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ckb'])

def test_cardinal_cs():
    assertions = [
        ('one', ['1']),
        ('few', ['2','3','4']),
        ('many', ['0.0','0.75','1.5','10.0','100.0']),
        ('other', ['0','5','12','19','100'])
    ]

    check(assertions, CARDINALS['cs'])

def test_cardinal_cy():
    assertions = [
        ('zero', ['0','0.0','0.00','0.000']),
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('few', ['3','3.0','3.00','3.000']),
        ('many', ['6','6.0','6.00','6.000']),
        ('other', ['4','5','7','14','20','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    check(assertions, CARDINALS['cy'])

def test_cardinal_da():
    assertions = [
        ('one', ['1','0.1','0.85','1.6']),
        ('other', ['0','2','9','16','100','0.0','2.0','2.7','3.4','10.0'])
    ]

    check(assertions, CARDINALS['da'])

def test_cardinal_de():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['de'])

def test_cardinal_dsb():
    assertions = [
        ('one', ['1','101','201','0.1','1.1','2.1']),
        ('two', ['2','102','202','0.2','1.2','2.2']),
        ('few', ['3','4','103','0.3','0.4','1.3']),
        ('other', ['0','5','12','19','100','0.0','0.5','0.75','1.0','1.5','1.75','2.0'])
    ]

    check(assertions, CARDINALS['dsb'])

def test_cardinal_dv():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['dv'])

def test_cardinal_dz():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['dz'])

def test_cardinal_ee():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ee'])

def test_cardinal_el():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['el'])

def test_cardinal_en():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['en'])

def test_cardinal_eo():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['eo'])

def test_cardinal_es():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['es'])

def test_cardinal_et():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['et'])

def test_cardinal_eu():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['eu'])

def test_cardinal_fa():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    check(assertions, CARDINALS['fa'])

def test_cardinal_ff():
    assertions = [
        ('one', ['0','1','0.0','0.75','1.5']),
        ('other', ['2','10','17','100','1000','2.0','2.75','3.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ff'])

def test_cardinal_fi():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['fi'])

def test_cardinal_fil():
    assertions = [
        ('one', ['0','2','3','5','7','0.0','0.15','0.3','0.5','0.7']),
        ('other', ['4','6','9','0.4','0.6','0.9'])
    ]

    check(assertions, CARDINALS['fil'])

def test_cardinal_fo():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['fo'])

def test_cardinal_fr():
    assertions = [
        ('one', ['0','1','0.0','0.75','1.5']),
        ('other', ['2','10','17','100','1000','2.0','2.75','3.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['fr'])

def test_cardinal_fur():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['fur'])

def test_cardinal_fy():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['fy'])

def test_cardinal_ga():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('few', ['3','5','6','3.0','4.0','5.0']),
        ('many', ['7','9','10','7.0','8.0','9.0']),
        ('other', ['0','11','18','25','100','0.0','0.45','0.9','1.1','1.35','1.6','10.1'])
    ]

    check(assertions, CARDINALS['ga'])

def test_cardinal_gd():
    assertions = [
        ('one', ['1','11','1.0','11.0','1.00']),
        ('two', ['2','12','2.0','12.0','2.00']),
        ('few', ['3','7','10','13','16','19','3.0','4.0','5.0']),
        ('other', ['0','20','27','34','100','0.0','0.45','0.9','1.1','1.35','1.6','10.1'])
    ]

    check(assertions, CARDINALS['gd'])

def test_cardinal_gl():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['gl'])

def test_cardinal_gsw():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['gsw'])

def test_cardinal_gu():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    check(assertions, CARDINALS['gu'])

def test_cardinal_guw():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    check(assertions, CARDINALS['guw'])

def test_cardinal_gv():
    assertions = [
        ('one', ['1','11','21']),
        ('two', ['2','12','22']),
        ('few', ['0','20','40']),
        ('many', ['0.0','0.75','1.5','10.0','100.0']),
        ('other', ['3','7','10','13','16','19','23'])
    ]

    check(assertions, CARDINALS['gv'])

def test_cardinal_ha():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ha'])

def test_cardinal_haw():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['haw'])

def test_cardinal_he():
    assertions = [
        ('one', ['1']),
        ('two', ['2']),
        ('many', ['20','30','40']),
        ('other', ['0','3','10','17','101','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['he'])

def test_cardinal_hi():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    check(assertions, CARDINALS['hi'])

def test_cardinal_hr():
    assertions = [
        ('one', ['1','21','31','0.1','1.1','2.1']),
        ('few', ['2','3','4','22','23','24','32','33','34','0.2','0.3','0.4','1.2','1.3','1.4','2.2','2.3','2.4']),
        ('other', ['0','5','12','19','100','0.0','0.5','0.75','1.0','1.5','1.75','2.0'])
    ]

    check(assertions, CARDINALS['hr'])

def test_cardinal_hsb():
    assertions = [
        ('one', ['1','101','201','0.1','1.1','2.1']),
        ('two', ['2','102','202','0.2','1.2','2.2']),
        ('few', ['3','4','103','0.3','0.4','1.3']),
        ('other', ['0','5','12','19','100','0.0','0.5','0.75','1.0','1.5','1.75','2.0'])
    ]

    check(assertions, CARDINALS['hsb'])

def test_cardinal_hu():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['hu'])

def test_cardinal_hy():
    assertions = [
        ('one', ['0','1','0.0','0.75','1.5']),
        ('other', ['2','10','17','100','1000','2.0','2.75','3.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['hy'])

def test_cardinal_ia():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ia'])

def test_cardinal_id():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['id'])

def test_cardinal_ig():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ig'])

def test_cardinal_ii():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ii'])

def test_cardinal_in():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['in'])

def test_cardinal_io():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['io'])

def test_cardinal_is():
    assertions = [
        ('one', ['1','21','31','0.1','0.85','1.6','10.1','100.1']),
        ('other', ['0','2','9','16','100','0.0','2.0','3.0'])
    ]

    check(assertions, CARDINALS['is'])

def test_cardinal_it():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['it'])

def test_cardinal_iu():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['iu'])

def test_cardinal_iw():
    assertions = [
        ('one', ['1']),
        ('two', ['2']),
        ('many', ['20','30','40']),
        ('other', ['0','3','10','17','101','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['iw'])

def test_cardinal_ja():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ja'])

def test_cardinal_jbo():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['jbo'])

def test_cardinal_jgo():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['jgo'])

def test_cardinal_ji():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ji'])

def test_cardinal_jmc():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['jmc'])

def test_cardinal_jv():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['jv'])

def test_cardinal_jw():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['jw'])

def test_cardinal_ka():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ka'])

def test_cardinal_kab():
    assertions = [
        ('one', ['0','1','0.0','0.75','1.5']),
        ('other', ['2','10','17','100','1000','2.0','2.75','3.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['kab'])

def test_cardinal_kaj():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['kaj'])

def test_cardinal_kcg():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['kcg'])

def test_cardinal_kde():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['kde'])

def test_cardinal_kea():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['kea'])

def test_cardinal_kk():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['kk'])

def test_cardinal_kkj():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['kkj'])

def test_cardinal_kl():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['kl'])

def test_cardinal_km():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['km'])

def test_cardinal_kn():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    check(assertions, CARDINALS['kn'])

def test_cardinal_ko():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ko'])

def test_cardinal_ks():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ks'])

def test_cardinal_ksb():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ksb'])

def test_cardinal_ksh():
    assertions = [
        ('zero', ['0','0.0','0.00','0.000']),
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    check(assertions, CARDINALS['ksh'])

def test_cardinal_ku():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ku'])

def test_cardinal_kw():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['kw'])

def test_cardinal_ky():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ky'])

def test_cardinal_lag():
    assertions = [
        ('zero', ['0','0.0','0.00','0.000']),
        ('one', ['1','0.1','0.85','1.6']),
        ('other', ['2','10','17','100','1000','2.0','2.75','3.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['lag'])

def test_cardinal_lb():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['lb'])

def test_cardinal_lg():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['lg'])

def test_cardinal_lkt():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['lkt'])

def test_cardinal_ln():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    check(assertions, CARDINALS['ln'])

def test_cardinal_lo():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['lo'])

def test_cardinal_lt():
    assertions = [
        ('one', ['1','21','31','1.0','21.0','31.0']),
        ('few', ['2','6','9','22','26','29','102','2.0','3.0','4.0']),
        ('many', ['0.1','0.5','0.9','1.1','1.4','1.7','10.1']),
        ('other', ['0','10','15','20','30','0.0','10.0','11.0'])
    ]

    check(assertions, CARDINALS['lt'])

def test_cardinal_lv():
    assertions = [
        ('zero', ['0','10','15','20','30','0.0','10.0','11.0']),
        ('one', ['1','21','31','0.1','1.0','1.1']),
        ('other', ['2','6','9','22','26','29','102','0.2','0.55','0.9','1.2','1.55','1.9','10.2'])
    ]

    check(assertions, CARDINALS['lv'])

def test_cardinal_mas():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['mas'])

def test_cardinal_mg():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    check(assertions, CARDINALS['mg'])

def test_cardinal_mgo():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['mgo'])

def test_cardinal_mk():
    assertions = [
        ('one', ['1','21','31','0.1','1.1','2.1']),
        ('other', ['0','2','9','16','100','0.0','0.2','0.6','1.0','1.2','1.45','1.7'])
    ]

    check(assertions, CARDINALS['mk'])

def test_cardinal_ml():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ml'])

def test_cardinal_mn():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['mn'])

def test_cardinal_mo():
    assertions = [
        ('one', ['1']),
        ('few', ['0','2','9','16','101','0.0','0.75','1.5','10.0','100.0']),
        ('other', ['20','28','35','100','1000'])
    ]

    check(assertions, CARDINALS['mo'])

def test_cardinal_mr():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    check(assertions, CARDINALS['mr'])

def test_cardinal_ms():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ms'])

def test_cardinal_mt():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('few', ['0','2','6','10','102','105','107','0.0','2.0','3.0']),
        ('many', ['11','15','19','111','114','117','1011','11.0','12.0','13.0']),
        ('other', ['20','28','35','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.1'])
    ]

    check(assertions, CARDINALS['mt'])

def test_cardinal_my():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['my'])

def test_cardinal_nah():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['nah'])

def test_cardinal_naq():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['naq'])

def test_cardinal_nb():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['nb'])

def test_cardinal_nd():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['nd'])

def test_cardinal_ne():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ne'])

def test_cardinal_nl():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['nl'])

def test_cardinal_nn():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['nn'])

def test_cardinal_nnh():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['nnh'])

def test_cardinal_no():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['no'])

def test_cardinal_nqo():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['nqo'])

def test_cardinal_nr():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['nr'])

def test_cardinal_nso():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    check(assertions, CARDINALS['nso'])

def test_cardinal_ny():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ny'])

def test_cardinal_nyn():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['nyn'])

def test_cardinal_om():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['om'])

def test_cardinal_or():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['or'])

def test_cardinal_os():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['os'])

def test_cardinal_pa():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    check(assertions, CARDINALS['pa'])

def test_cardinal_pap():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['pap'])

def test_cardinal_pl():
    assertions = [
        ('one', ['1']),
        ('few', ['2','3','4','22','23','24','32','33','34']),
        ('many', ['0','5','12','19','100']),
        ('other', ['0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['pl'])

def test_cardinal_prg():
    assertions = [
        ('zero', ['0','10','15','20','30','0.0','10.0','11.0']),
        ('one', ['1','21','31','0.1','1.0','1.1']),
        ('other', ['2','6','9','22','26','29','102','0.2','0.55','0.9','1.2','1.55','1.9','10.2'])
    ]

    check(assertions, CARDINALS['prg'])

def test_cardinal_ps():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ps'])

def test_cardinal_pt():
    assertions = [
        ('one', ['0','1','0.0','0.75','1.5']),
        ('other', ['2','10','17','100','1000','2.0','2.75','3.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['pt'])

def test_cardinal_pt_PT():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['pt-PT'])

def test_cardinal_rm():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['rm'])

def test_cardinal_ro():
    assertions = [
        ('one', ['1']),
        ('few', ['0','2','9','16','101','0.0','0.75','1.5','10.0','100.0']),
        ('other', ['20','28','35','100','1000'])
    ]

    check(assertions, CARDINALS['ro'])

def test_cardinal_rof():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['rof'])

def test_cardinal_root():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['root'])

def test_cardinal_ru():
    assertions = [
        ('one', ['1','21','31']),
        ('few', ['2','3','4','22','23','24','32','33','34']),
        ('many', ['0','5','12','19','100']),
        ('other', ['0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ru'])

def test_cardinal_rwk():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['rwk'])

def test_cardinal_sah():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['sah'])

def test_cardinal_saq():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['saq'])

def test_cardinal_sc():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['sc'])

def test_cardinal_scn():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['scn'])

def test_cardinal_sd():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['sd'])

def test_cardinal_sdh():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['sdh'])

def test_cardinal_se():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['se'])

def test_cardinal_seh():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['seh'])

def test_cardinal_ses():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ses'])

def test_cardinal_sg():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['sg'])

def test_cardinal_sh():
    assertions = [
        ('one', ['1','21','31','0.1','1.1','2.1']),
        ('few', ['2','3','4','22','23','24','32','33','34','0.2','0.3','0.4','1.2','1.3','1.4','2.2','2.3','2.4']),
        ('other', ['0','5','12','19','100','0.0','0.5','0.75','1.0','1.5','1.75','2.0'])
    ]

    check(assertions, CARDINALS['sh'])

def test_cardinal_shi():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('few', ['2','6','10','2.0','3.0','4.0']),
        ('other', ['11','19','26','100','1000','1.1','1.5','1.9','2.1','2.4','2.7','10.1'])
    ]

    check(assertions, CARDINALS['shi'])

def test_cardinal_si():
    assertions = [
        ('one', ['0','1','0.0','0.1','1.0']),
        ('other', ['2','10','17','100','1000','0.2','0.55','0.9','1.1','1.45','1.8','10.0'])
    ]

    check(assertions, CARDINALS['si'])

def test_cardinal_sk():
    assertions = [
        ('one', ['1']),
        ('few', ['2','3','4']),
        ('many', ['0.0','0.75','1.5','10.0','100.0']),
        ('other', ['0','5','12','19','100'])
    ]

    check(assertions, CARDINALS['sk'])

def test_cardinal_sl():
    assertions = [
        ('one', ['1','101','201']),
        ('two', ['2','102','202']),
        ('few', ['3','4','103','0.0','0.75','1.5','10.0','100.0']),
        ('other', ['0','5','12','19','100'])
    ]

    check(assertions, CARDINALS['sl'])

def test_cardinal_sma():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['sma'])

def test_cardinal_smi():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['smi'])

def test_cardinal_smj():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['smj'])

def test_cardinal_smn():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['smn'])

def test_cardinal_sms():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('two', ['2','2.0','2.00','2.000']),
        ('other', ['0','3','10','17','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['sms'])

def test_cardinal_sn():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['sn'])

def test_cardinal_so():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['so'])

def test_cardinal_sq():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['sq'])

def test_cardinal_sr():
    assertions = [
        ('one', ['1','21','31','0.1','1.1','2.1']),
        ('few', ['2','3','4','22','23','24','32','33','34','0.2','0.3','0.4','1.2','1.3','1.4','2.2','2.3','2.4']),
        ('other', ['0','5','12','19','100','0.0','0.5','0.75','1.0','1.5','1.75','2.0'])
    ]

    check(assertions, CARDINALS['sr'])

def test_cardinal_ss():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ss'])

def test_cardinal_ssy():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ssy'])

def test_cardinal_st():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['st'])

def test_cardinal_sv():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['sv'])

def test_cardinal_sw():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['sw'])

def test_cardinal_syr():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['syr'])

def test_cardinal_ta():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ta'])

def test_cardinal_te():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['te'])

def test_cardinal_teo():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['teo'])

def test_cardinal_th():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['th'])

def test_cardinal_ti():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    check(assertions, CARDINALS['ti'])

def test_cardinal_tig():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['tig'])

def test_cardinal_tk():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['tk'])

def test_cardinal_tl():
    assertions = [
        ('one', ['0','2','3','5','7','0.0','0.15','0.3','0.5','0.7']),
        ('other', ['4','6','9','0.4','0.6','0.9'])
    ]

    check(assertions, CARDINALS['tl'])

def test_cardinal_tn():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['tn'])

def test_cardinal_to():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['to'])

def test_cardinal_tr():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['tr'])

def test_cardinal_ts():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ts'])

def test_cardinal_tzm():
    assertions = [
        ('one', ['0','1','11','18','24','0.0','1.0','11.0']),
        ('other', ['2','6','10','100','103','106','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    check(assertions, CARDINALS['tzm'])

def test_cardinal_ug():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ug'])

def test_cardinal_uk():
    assertions = [
        ('one', ['1','21','31']),
        ('few', ['2','3','4','22','23','24','32','33','34']),
        ('many', ['0','5','12','19','100']),
        ('other', ['0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['uk'])

def test_cardinal_ur():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['ur'])

def test_cardinal_uz():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['uz'])

def test_cardinal_ve():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['ve'])

def test_cardinal_vi():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['vi'])

def test_cardinal_vo():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['vo'])

def test_cardinal_vun():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['vun'])

def test_cardinal_wa():
    assertions = [
        ('one', ['0','1','0.0','1.0','0.00']),
        ('other', ['2','10','17','100','1000','0.1','0.5','0.9','1.1','1.4','1.7','10.0'])
    ]

    check(assertions, CARDINALS['wa'])

def test_cardinal_wae():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['wae'])

def test_cardinal_wo():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['wo'])

def test_cardinal_xh():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['xh'])

def test_cardinal_xog():
    assertions = [
        ('one', ['1','1.0','1.00','1.000']),
        ('other', ['0','2','9','16','100','0.0','0.45','0.9','1.1','1.35','1.6','10.0'])
    ]

    check(assertions, CARDINALS['xog'])

def test_cardinal_yi():
    assertions = [
        ('one', ['1']),
        ('other', ['0','2','9','16','100','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['yi'])

def test_cardinal_yo():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['yo'])

def test_cardinal_yue():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['yue'])

def test_cardinal_zh():
    assertions = [
        ('other', ['0','8','15','100','1000','0.0','0.75','1.5','10.0','100.0'])
    ]

    check(assertions, CARDINALS['zh'])

def test_cardinal_zu():
    assertions = [
        ('one', ['0','1','0.0','0.5','1.0','0.00','0.02','0.04']),
        ('other', ['2','10','17','100','1000','1.1','1.85','2.6','10.0','100.0'])
    ]

    check(assertions, CARDINALS['zu'])


# ================================
# END AUTOMATICALLY GENERATED CODE
# ================================
