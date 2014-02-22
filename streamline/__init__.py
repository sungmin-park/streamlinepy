from compiler import parseFile
import json

import re


def snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def visit(node):
    return globals()['visit_%s' % snake(node.__class__.__name__)](node)


def visit_const(const):
    return json.dumps(const.value)


def visit_return(return_):
    return 'return %s;' % visit(return_.value)


def visit_function(func):
    return "var %s = function(){ %s };" % (func.name, visit(func.code))


def visit_stmt(stmt):
    js = [visit(i) for i in stmt.nodes]
    return ''.join(i + '\n' for i in js)


def trans(module):
    return visit(module.node)


def to_js(filename):
    module = parseFile(filename)
    return trans(module)
