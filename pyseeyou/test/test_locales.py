import pytest

from pyseeyou.locales import one_or_other, other


def test_other():
    assert other(0) == 'other'
    assert other(1) == 'other'
    assert other(2) == 'other'
    assert other(4) == 'other'
    assert other(9) == 'other'
    assert other(13) == 'other'


def test_one_or_other():
    assert one_or_other(0) == 'other'
    assert one_or_other(1) == 'one'
    assert one_or_other(2) == 'other'
    assert one_or_other(4) == 'other'
    assert one_or_other(9) == 'other'
    assert one_or_other(13) == 'other'
