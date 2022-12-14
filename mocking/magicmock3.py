import unittest
from unittest.mock import patch

class MyTest(unittest.TestCase):

    def create_patch(self, name):
        patcher = patch(name)
        thing = patcher.start()
        self.addCleanup(patcher.stop)
        return thing

    def test_foo(self):
        mock_foo = self.create_patch('mymodule.Foo')
        mock_bar = self.create_patch('mymodule.Bar')
        mock_spam = self.create_patch('mymodule.Spam')

        assert mymodule.Foo is mock_foo
        assert mymodule.Bar is mock_bar
        assert mymodule.Spam is mock_spam

original = mymodule.Foo
MyTest('test_foo').run()
assert mymodule.Foo is original