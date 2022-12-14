import unittest
from unittest.mock import patch

class MyTest(unittest.TestCase):
     def setUp(self):
         patcher = patch('mymodule.foo')
         self.addCleanup(patcher.stop)
         self.mock_foo = patcher.start()

     def test_foo(self):
         self.assertIs(mymodule.foo, self.mock_foo)

MyTest('test_foo').run()