import pytest

from pyseeyou.locales import get_parts_of_num

def test_get_parts_of_num():
    assert get_parts_of_num('1') == (1, 1, 0, 0, 0, 0)
    assert get_parts_of_num('1.0') == (1.0, 1, 1, 0, 0, 0)
    assert get_parts_of_num('1.00') == (1.00, 1, 2, 0, 0, 0)
    assert get_parts_of_num('1.3') == (1.3, 1, 1, 1, 3, 3)
    assert get_parts_of_num('1.30') == (1.30, 1, 2, 1, 30, 3)
    assert get_parts_of_num('1.03') == (1.03, 1, 2, 2, 3, 3)
    assert get_parts_of_num('1.230') == (1.230, 1, 3, 2, 230, 23)