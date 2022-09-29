import unittest
from unittest.mock import patch
import mymodule

class MyTest(unittest.TestCase):
    def setUp(self):
        # self.patcher = patch('mymodule.foo')
        # self.mock_foo = self.patcher.start()
        self.mock_foo=patch('mymodule.foo').start()

    def test_foo(self):
        self.assertIs(mymodule.foo, self.mock_foo)

    def tearDown(self):
        # self.patcher.stop()
        self.mock_foo.stop()

MyTest('test_foo').run()