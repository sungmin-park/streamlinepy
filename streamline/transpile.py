from compiler import parseFile
import json

from jinja2 import Environment, PackageLoader

import re


env = Environment(loader=PackageLoader('streamline', 'templates'))


def render_template(_template_name, **kwargs):
    return env.get_template(_template_name).render(**kwargs)


def snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def visit(node):
    return globals()['visit_%s' % snake(node.__class__.__name__)](node)


def visit_call_func(call_func):
    args = [visit(i) for i in call_func.args]
    return '%s(%s, _)' % (visit(call_func.node), ', '.join(args))


def visit_const(const):
    return json.dumps(const.value)


def visit_discard(discard):
    return visit(discard.expr) + ';'


def visit_from(from_):
    js = []
    for name, as_ in from_.names:
        if as_ is None:
            as_ = name
        js.append(
            "var %s = streamlinepy.import_from('%s', '%s', __file__, _);" % (
                as_, name, from_.modname
            )
        )
    return '\n'.join(js)


def visit_printnl(printnl):
    return 'console.info(%s);' % ', '.join(visit(i) for i in printnl.nodes)


def visit_return(return_):
    return 'return %s;' % visit(return_.value)


def visit_function(func):
    return "var %s = function(){ %s };" % (func.name, visit(func.code))


def visit_name(name):
    return name.name


def visit_stmt(stmt):
    js = [visit(i) for i in stmt.nodes]
    return ''.join(i + '\n' for i in js)


def trans(module, filename):
    name = filename[:-3].replace('/', '.')
    stmts = visit(module.node)
    return render_template(
        'module.js', stmts=stmts, name=name, filename=filename
    )


def to_js(filename):
    module = parseFile(filename)
    return trans(module, filename)
