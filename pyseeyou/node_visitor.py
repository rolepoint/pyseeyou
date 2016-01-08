from __future__ import unicode_literals

from parsimonious.nodes import NodeVisitor
from toolz import merge

from pyseeyou.locales import get_cardinal_category


class ICUNodeVisitor(NodeVisitor):
    def __init__(self, options, lang='en'):
        self.options = options
        self.lang = lang

    def generic_visit(self, node, visited_children):
        if visited_children:
            visited_children = self._filter_none(visited_children)

        if len(visited_children) > 1:
            return merge(visited_children)

        elif len(visited_children) == 1:
            return visited_children[0]

    def visit_message_format_pattern(self, node, visited_children):
        text = u''

        for item in visited_children:
            if not item:
                continue

            if isinstance(item, unicode):
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
        return visited_children[1]

    def visit_plural_form(self, node, visited_children):
        return self._get_key_value(visited_children)

    def visit_plural_key(self, node, visited_children):
        if isinstance(visited_children[0], int):
            return {'key': visited_children[0]}

        return visited_children[0]

    def visit_arg_style_pattern(self, node, visited_children):
        pass

    def visit_offset(self, node, visited_children):
        pass

    def visit_octothorpe(self, node, visited_children):
        return unicode(node.text)

    def visit_string(self, node, visited_children):
        return unicode(node.text)

    def visit_id(self, node, visited_children):
        return {'key': unicode(node.text)}

    def visit_digits(self, node, visited_children):
        return int(node.text)

    def visit__(self, node, visited_children):
        pass

    def _get_formed_string(self, item, key):
        # Direct replacement, {} style
        if not item[key]:
            return self.options[key]

        # self.option has this key as an int -> change plurality
        if isinstance(self.options.get(key), int):
            if self.options[key] in item[key]:
                return item[key][self.options[key]]

            else:
                plural_key = get_cardinal_category(
                    self.options[key], self.lang)

                if '#' in item[key][plural_key]:
                    return item[key][plural_key].replace(
                        '#', unicode(self.options[key]))

                else:
                    return item[key][plural_key]

        # self.option has this key as a string -> change selection
        else:
            if key in self.options:
                return item[key][self.options[key]]

            else:
                return item[key]['other']

    def _get_key_value(self, items):
        key, value = None, None
        for item in items:
            if not item:
                continue

            elif isinstance(item, unicode):
                value = item

            elif isinstance(item, dict):
                key = item['key']

        return {key: value}

    def _filter_none(self, items):
        return [item for item in items if item is not None]
