from __future__ import unicode_literals

from pyseeyou import format, format_tree
from pyseeyou.grammar import ICUMessageFormat


def test_format():
    select = format(
        '{WHO, select, male {He} female {She} other {They}}.',
        {'WHO': 'male'}, 'en')

    assert select == 'He.'

    plural = format(
        '{NUM_TICKETS, plural, one {1 ticket} other {# tickets} =42 {42 ticketerinos}}.',
        {'NUM_TICKETS': 1}, 'en')

    assert plural == '1 ticket.'

    select_plural = format(
        '{GENDER, select, male {He wants} female {She wants} other {They want}} {NUM_TICKETS, plural, one {1 ticket} other {# tickets} =42 {42 ticketerinos}}.',
        {'GENDER': 'male', 'NUM_TICKETS': 5}, 'en')

    assert select_plural == 'He wants 5 tickets.'

    select_plural_offset = format(
        '{GENDER, select, male {He wants} female {She wants} other {They want}} {NUM_TICKETS, plural, offset:2 one {1 ticket} other {# tickets} =42 {42 ticketerinos}}.',
        {'GENDER': 'female', 'NUM_TICKETS': '44'}, 'en')

    assert select_plural_offset == 'She wants 42 ticketerinos.'


def test_format_tree():
    ast = ICUMessageFormat.parse(
        '{WHO, select, male {He} female {She} other {They}}.')

    select = format_tree(ast, {'WHO': 'male'}, 'en')
    assert select == 'He.'

    select = format_tree(ast, {'WHO': 'female'}, 'en')
    assert select == 'She.'

    select = format_tree(ast, {'WHO': 'other'}, 'en')
    assert select == 'They.'

    select = format_tree(ast, {}, 'en')
    assert select == 'They.'

    ast = ICUMessageFormat.parse(
        '{NUM_TICKETS, plural, offset:1 one {1 ticket} other {# tickets} =42 {42 ticketerinos}}.')

    plural = format_tree(ast, {'NUM_TICKETS': 1}, 'en')
    assert plural == '0 tickets.'

    plural = format_tree(ast, {'NUM_TICKETS': '1'}, 'en')
    assert plural == '0 tickets.'

    plural = format_tree(ast, {'NUM_TICKETS': '2'}, 'en')
    assert plural == '1 ticket.'

    plural = format_tree(ast, {'NUM_TICKETS': 2.0}, 'en')
    assert plural == '1.0 tickets.'

    plural = format_tree(ast, {'NUM_TICKETS': 5}, 'en')
    assert plural == '4 tickets.'

    plural = format_tree(ast, {'NUM_TICKETS': 43}, 'en')
    assert plural == '42 ticketerinos.'


def test_format_empty_string():
    template = '{number, plural, =1 {} other {#}}'

    result = format(template, {'number': 1}, 'en')

    assert result == ''
