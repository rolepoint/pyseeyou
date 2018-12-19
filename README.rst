--------
pyseeyou
--------

A Python ICU MessageFormat parsing tool,
using `parsimonious <https://github.com/erikrose/parsimonious>`_ to parse a
PEG, which has been taken from
`messageformat.js <https://github.com/SlexAxton/messageformat.js>`_.

Compatible with Python 2.7, 3.5, 3.6 and 3.7

Usage
=====

.. code-block:: python

    from pyseeyou import format

    result = format('''{GENDER, select,
                           male {He}
                         female {She}
                          other {They}
                       } found {NUM_RESULTS, plural,
                           one {1 result}
                         other {# results}
                       } in {NUM_CATEGORIES, plural,
                             one {1 category}
                           other {# categories}
                       }.''',
            {'GENDER': 'male', 'NUM_RESULTS': 1, 'NUM_CATEGORIES': '2'}, 'en')

    => u'He found 1 result in 2 categories.'
