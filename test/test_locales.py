import pytest

from pyseeyou.locales import (
    get_parts_of_num, brazilian_pt, czech, french, one_or_other, other, spanish)


def test_get_parts_of_num():
    assert get_parts_of_num('1') == ('1', 1, 0, 0, 0, 0)
    assert get_parts_of_num('1.0') == ('1.0', 1, 1, 0, 0, 0)
    assert get_parts_of_num('1.00') == ('1.00', 1, 2, 0, 0, 0)
    assert get_parts_of_num('1.3') == ('1.3', 1, 1, 1, 3, 3)
    assert get_parts_of_num('1.30') == ('1.30', 1, 2, 1, 30, 3)
    assert get_parts_of_num('1.03') == ('1.03', 1, 2, 2, 3, 3)
    assert get_parts_of_num('1.230') == ('1.230', 1, 3, 2, 230, 23)


def test_brazilian_pt():
    assert brazilian_pt(*get_parts_of_num('0')) == 'one'
    assert brazilian_pt(*get_parts_of_num('1')) == 'one'
    assert brazilian_pt(*get_parts_of_num('1.0')) == 'one'
    assert brazilian_pt(*get_parts_of_num('1.3')) == 'other'
    assert brazilian_pt(*get_parts_of_num('2')) == 'other'
    assert brazilian_pt(*get_parts_of_num('4')) == 'other'
    assert brazilian_pt(*get_parts_of_num('9')) == 'other'
    assert brazilian_pt(*get_parts_of_num('13')) == 'other'


def test_czech():
    assert czech(*get_parts_of_num('0')) == 'other'
    assert czech(*get_parts_of_num('1')) == 'one'
    assert czech(*get_parts_of_num('1.0')) == 'many'
    assert czech(*get_parts_of_num('1.3')) == 'many'
    assert czech(*get_parts_of_num('2')) == 'few'
    assert czech(*get_parts_of_num('2.5')) == 'many'
    assert czech(*get_parts_of_num('4')) == 'few'
    assert czech(*get_parts_of_num('13')) == 'other'
    assert czech(*get_parts_of_num('13.5')) == 'many'


def test_french():
    assert french(*get_parts_of_num('0')) == 'one'
    assert french(*get_parts_of_num('1')) == 'one'
    assert french(*get_parts_of_num('1.0')) == 'one'
    assert french(*get_parts_of_num('1.3')) == 'one'
    assert french(*get_parts_of_num('2')) == 'other'
    assert french(*get_parts_of_num('4')) == 'other'
    assert french(*get_parts_of_num('9')) == 'other'
    assert french(*get_parts_of_num('13')) == 'other'


def test_other():
    assert other(*get_parts_of_num('0')) == 'other'
    assert other(*get_parts_of_num('1')) == 'other'
    assert other(*get_parts_of_num('1.0')) == 'other'
    assert other(*get_parts_of_num('1.3')) == 'other'
    assert other(*get_parts_of_num('2')) == 'other'
    assert other(*get_parts_of_num('4')) == 'other'
    assert other(*get_parts_of_num('9')) == 'other'
    assert other(*get_parts_of_num('13')) == 'other'


def test_one_or_other():
    assert one_or_other(*get_parts_of_num('0')) == 'other'
    assert one_or_other(*get_parts_of_num('1')) == 'one'
    assert one_or_other(*get_parts_of_num('1.0')) == 'other'
    assert one_or_other(*get_parts_of_num('1.3')) == 'other'
    assert one_or_other(*get_parts_of_num('2')) == 'other'
    assert one_or_other(*get_parts_of_num('4')) == 'other'
    assert one_or_other(*get_parts_of_num('9')) == 'other'
    assert one_or_other(*get_parts_of_num('13')) == 'other'


def test_spanish():
    assert spanish(*get_parts_of_num('0')) == 'other'
    assert spanish(*get_parts_of_num('2')) == 'other'
    assert spanish(*get_parts_of_num('1.1')) == 'other'
    assert spanish(*get_parts_of_num('0.9')) == 'other'
    assert spanish(*get_parts_of_num('10.0')) == 'other'
    assert spanish(*get_parts_of_num('1000.000')) == 'other'
    assert spanish(*get_parts_of_num('1')) == 'one'
    assert spanish(*get_parts_of_num('1.0')) == 'one'
    assert spanish(*get_parts_of_num('1.00')) == 'one'
    assert spanish(*get_parts_of_num('1.000000')) == 'one'
