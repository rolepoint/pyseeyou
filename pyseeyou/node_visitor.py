from __future__ import unicode_literals

from parsimonious.nodes import NodeVisitor
from toolz import merge


class ICUNodeVisitor(NodeVisitor):
    def __init__(self, options):
        self.options = options

    def generic_visit(self, node, visited_children):
        if visited_children:
            not_none = self._filter_none(visited_children)

            if not_none:
                return not_none[0]

    def visit_message_format_pattern(self, node, visited_children):
        text = u''

        for item in visited_children:
            if not item:
                continue

            for key in item:
                if key in self.options:
                    text += item[key][self.options[key]]
                else:
                    text += item[key]

        return text

    def visit_message_format_element(self, node, visited_children):
        key, values = self._filter_none(visited_children)
        key = key.get('key')

        return {key: values}

    def visit_element_format(self, node, visited_children):
        return visited_children[0]

    def visit_select_format_pattern(self, node, visited_children):
        return merge(visited_children)

    def visit_select_form(self, node, visited_children):
        key, value = None, None
        for child in visited_children:
            if not child:
                continue

            elif isinstance(child, unicode):
                value = child

            elif isinstance(child, dict):
                if child.get('key'):
                    key = child['key']

        return {key: value}

    def visit_plural_format_pattern(self, node, visited_children):
        pass

    def visit_plural_form(self, node, visited_children):
        pass

    def visit_plural_key(self, node, visited_children):
        pass

    def visit_arg_style_pattern(self, node, visited_children):
        pass

    def visit_offset(self, node, visited_children):
        pass

    def visit_octothorpe(self, node, visited_children):
        pass

    def visit_string(self, node, visited_children):
        return {'value': node.text}

    def visit_id(self, node, visited_children):
        return {'key': node.text}

    def visit_digits(self, node, visited_children):
        pass

    def visit__(self, node, visited_children):
        pass

    def _filter_none(self, items):
        return [item for item in items if item is not None]
