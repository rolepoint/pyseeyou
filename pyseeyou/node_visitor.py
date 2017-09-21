from __future__ import unicode_literals

from builtins import str
from decimal import Decimal
from parsimonious.nodes import NodeVisitor
from toolz import merge

from pyseeyou.locales import get_cardinal_category


class ICUNodeVisitor(NodeVisitor):
    def __init__(self, options, lang='en'):
        '''
        ICUNodeVisitor is a walker for the generated parse tree from
        pyseeyou.grammar.ICUMessageFormat.

        Calling visit() on an instance of the ICUNodeVisitor will traverse the
        tree, returning a fully formed string, using the self.options dict as
        the values to replace any IDs that were parsed using the grammar.

        :param options: Values used to replace parsed IDs with.
        :param lang: Language used to derive pluralisation phrase of number
        '''
        self.options = options
        self.lang = lang

    def generic_visit(self, node, visited_children):
        '''
        Each of the methods below beginning with visit_ are called when
        visiting a node of that type. These methods deal with how to parse and
        process the data that has reached that node.

        This generic_visit method deals with visiting nodes that have no
        specific type.
        '''
        if visited_children:
            visited_children = self._filter_none(visited_children)

        if len(visited_children) > 1:
            return merge(visited_children)

        elif len(visited_children) == 1:
            return visited_children[0]

    def visit_message_format_pattern(self, node, visited_children):
        text = ''

        for item in visited_children:
            if not item:
                continue

            if isinstance(item, str):
                text += item

            else:
                for key in item:
                    text += self._get_formed_string(item, key)

        return text

    def visit_message_format_element(self, node, visited_children):
        visited_children = self._filter_none(visited_children)
        key = visited_children[0].get('key')

        if len(visited_children) == 1:
            return {key: None}
        else:
            values = visited_children[1]
            return {key: values}

    def visit_element_format(self, node, visited_children):
        return visited_children[0]

    def visit_select_format_pattern(self, node, visited_children):
        return merge(visited_children)

    def visit_select_form(self, node, visited_children):
        return self._get_key_value(visited_children)

    def visit_plural_format_pattern(self, node, visited_children):
        visited_children = self._filter_none(visited_children)
        return merge(visited_children)

    def visit_plural_form(self, node, visited_children):
        return self._get_key_value(visited_children)

    def visit_plural_key(self, node, visited_children):
        if isinstance(visited_children[0], str):
            return {'key': visited_children[0]}

        return visited_children[0]

    def visit_arg_style_pattern(self, node, visited_children):
        pass

    def visit_offset(self, node, visited_children):
        for child in visited_children:
            if isinstance(child, int):
                return {'offset': child}

    def visit_octothorpe(self, node, visited_children):
        return str(node.text)

    def visit_string(self, node, visited_children):
        return str(node.text)

    def visit_id(self, node, visited_children):
        return {'key': str(node.text)}

    def visit_replace_type(self, node, visited_children):
        return {'replace_type': str(node.text)}

    def visit_decimal(self, node, visited_children):
        return str(node.text)

    def visit_digits(self, node, visited_children):
        return int(node.text)

    def visit__(self, node, visited_children):
        pass

    def _get_formed_string(self, item, key):
        # Direct replacement, {} style
        if not item[key]:
            return self.options[key]

        replace_type = item[key]['replace_type']
        if replace_type.lower() == 'select':
            return self._select_replace(item[key], key)

        elif replace_type.lower() == 'plural':
            return self._plural_replace(item[key], key)

    def _select_replace(self, item, key):
        if key in self.options:
            return item[self.options[key]]

        else:
            return item['other']

    def _plural_replace(self, item, key):
        str_key = str(self.options[key])

        if 'offset' in item:
            dec_str_key = Decimal(str_key)
            dec_str_key -= item['offset']

            if dec_str_key < 0:
                str_key = '0'
            else:
                str_key = str(dec_str_key)

        if str_key in item:
            return item[str_key]

        else:
            plural_key = get_cardinal_category(str_key, self.lang)

            if '#' in item[plural_key]:
                return item[plural_key].replace(
                    '#', str(str_key))

            else:
                return item[plural_key]

    def _get_key_value(self, items):
        key, value = None, None
        for item in items:
            if not item:
                continue

            elif isinstance(item, str):
                value = item

            elif isinstance(item, dict):
                key = item['key']

        return {key: value}

    def _filter_none(self, items):
        return [item for item in items if item is not None]
