from pyseeyou.grammar import ICUMessageFormat
from pyseeyou.node_visitor import ICUNodeVisitor


def format(msg, values, lang):
    '''
    :param msg: String, The message to parse
    :param values: Dict, The values to use in forming the final message
    :param lang: String, The language code for the language to use to decide on
                 pluralisation rules
    '''

    ast = ICUMessageFormat.parse(msg)

    return format_tree(ast, values, lang)


def format_tree(ast, values, lang):
    '''
    :param ast: parsimonious.nodes.Node, Formed tree of the message to parse
    :param values: Dict, The values to use in forming the final message
    :param lang: String, The language code for the language to use to decide on
                 pluralisation rules
    '''
    i = ICUNodeVisitor(values, lang)

    return i.visit(ast)
