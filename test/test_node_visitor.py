# coding=utf-8
from __future__ import unicode_literals
import pytest

from pyseeyou.grammar import ICUMessageFormat
from pyseeyou.node_visitor import ICUNodeVisitor


def test_process_select_statement():
    msg = ICUMessageFormat.parse(
        '''{WHO, select, male {He} female {She} other {They}}.''')

    i = ICUNodeVisitor({'WHO': 'male'})
    assert i.visit(msg) == 'He.'

    i = ICUNodeVisitor({'WHO': 'female'})
    assert i.visit(msg) == 'She.'

    i = ICUNodeVisitor({'WHO:': 'other'})
    assert i.visit(msg) == 'They.'


def test_use_other_statement_if_no_select_arg():
    msg = ICUMessageFormat.parse(
        '''{WHO, select, male {He} female {She} other {They}}.''')

    i = ICUNodeVisitor({})
    assert i.visit(msg) == 'They.'


def test_process_plural_statement():
    msg = ICUMessageFormat.parse(
        '''{NUM_TICKETS, plural, one {1 ticket} other {# tickets} =42 {42 ticketerinos}}.''')

    i = ICUNodeVisitor({'NUM_TICKETS': 1})
    assert i.visit(msg) == '1 ticket.'

    i = ICUNodeVisitor({'NUM_TICKETS': 2})
    assert i.visit(msg) == '2 tickets.'

    i = ICUNodeVisitor({'NUM_TICKETS': 42})
    assert i.visit(msg) == '42 ticketerinos.'


def test_plural_statement_with_offset():
    msg = ICUMessageFormat.parse(
        '''{NUM_TICKETS, plural, offset:3 one {1 ticket} other {# tickets} =42 {42 ticketerinos}}.''')

    i = ICUNodeVisitor({'NUM_TICKETS': 2})
    assert i.visit(msg) == '0 tickets.'

    i = ICUNodeVisitor({'NUM_TICKETS': 4})
    assert i.visit(msg) == '1 ticket.'

    i = ICUNodeVisitor({'NUM_TICKETS': 45})
    assert i.visit(msg) == '42 ticketerinos.'


def test_plural_dict_uses_string():
    msg = ICUMessageFormat.parse(
        '''{NUM_TICKETS, plural, one {1 ticket} other {# tickets} =42 {42 ticketerinos}}.''')

    i = ICUNodeVisitor({'NUM_TICKETS': '1'})
    assert i.visit(msg) == '1 ticket.'

    i = ICUNodeVisitor({'NUM_TICKETS': '2'})
    assert i.visit(msg) == '2 tickets.'

    i = ICUNodeVisitor({'NUM_TICKETS': '42'})
    assert i.visit(msg) == '42 ticketerinos.'


def test_plural_dict_with_decimals():
    msg = ICUMessageFormat.parse(
        '''{NUM_TICKETS, plural, one {1 ticket} other {# tickets} =42.5 {42 ticketerinos}}.''')

    i = ICUNodeVisitor({'NUM_TICKETS': '1'})
    assert i.visit(msg) == '1 ticket.'

    i = ICUNodeVisitor({'NUM_TICKETS': '1.0'})
    assert i.visit(msg) == '1.0 tickets.'

    i = ICUNodeVisitor({'NUM_TICKETS': '42'})
    assert i.visit(msg) == '42 tickets.'

    i = ICUNodeVisitor({'NUM_TICKETS': '42.5'})
    assert i.visit(msg) == '42 ticketerinos.'


def test_msg_with_basic_replace():
    msg = ICUMessageFormat.parse(
        '''I {GREETING} this finds you well.''')

    i = ICUNodeVisitor({'GREETING': 'hope'})
    assert i.visit(msg) == 'I hope this finds you well.'

    i = ICUNodeVisitor({'GREETING': 'wish'})
    assert i.visit(msg) == 'I wish this finds you well.'

    i = ICUNodeVisitor({'GREETING': ''})
    assert i.visit(msg) == 'I  this finds you well.'


def test_msg_with_unicode_chars():
    msg = ICUMessageFormat.parse(
        '''{SYMBOL, select, snowman {☃} sun {☉} other {☹}}''')

    i = ICUNodeVisitor({'SYMBOL': 'snowman'})
    assert i.visit(msg) == '☃'

    i = ICUNodeVisitor({'SYMBOL': 'sun'})
    assert i.visit(msg) == '☉'

    i = ICUNodeVisitor({})
    assert i.visit(msg) == '☹'
