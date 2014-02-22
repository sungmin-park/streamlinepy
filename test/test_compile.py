from contextlib import contextmanager
from os import path, getcwd, chdir
from unittest import TestCase

import execjs
from streamline import to_js


@contextmanager
def pushd(dir):
    current = getcwd()
    chdir(dir)
    yield
    chdir(current)


class CompileTest(TestCase):
    def test_hello_world(self):
        with pushd(path.dirname(__file__)):
            js = to_js('hello_world.py')
            ctx = execjs.compile(js)
            self.assertEqual('Hello, world!', ctx.call('hello_world'))
