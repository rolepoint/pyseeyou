from __future__ import unicode_literals

from parsimonious.grammar import Grammar

g = Grammar('''
            message_format_pattern =
                (message_format_element/octothorpe/string)*

            message_format_element = "{" _ id ("," element_format)? _ "}"

            element_format =
                (_ replace_type _ "," _ select_format_pattern _) /
                (_ replace_type _ "," _ plural_format_pattern _) /
                (_ id arg_style_pattern*)

            plural_format_pattern = offset? (plural_form)+
            plural_form = _ plural_key _ "{" _ message_format_pattern _ "}"
            plural_key = id / ("=" digits)

            select_format_pattern = select_form+
            select_form = _ id _ "{" _ message_format_pattern _ "}"

            arg_style_pattern = _ "," _ id _

            offset = _ "offset" _ ":" _ digits _

            octothorpe   = ~"#"
            string       = (~"\w+"/~"[^{}]+"/_)+
            id           = ~"\w+"i
            replace_type = ~"\w+"i
            digits       = ~"[0-9]+"
            _            = ~"\s*"
            ''')
