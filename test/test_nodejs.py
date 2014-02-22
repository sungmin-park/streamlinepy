from unittest import TestCase
import execjs


class NodeJsTest(TestCase):
    def test_eval(self):
        self.assertEqual(2, execjs.eval("1 + 1"))
