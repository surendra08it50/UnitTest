"""
All the patchers have start() and stop() methods. These make it simpler to do patching in setUp methods or where you want to do multiple patches without nesting decorators or with statements.

To use them call patch(), patch.object() or patch.dict() as normal and keep a reference to the returned patcher object. You can then call start() to put the patch in place and stop() to undo it.

If you are using patch() to create a mock for you then it will be returned by the call to patcher.start.
"""


import unittest
from unittest.mock import patch
class MyTest(unittest.TestCase):
    def setUp(self):
        self.patcher1 = patch('package.module.Class1')
        self.patcher2 = patch('package.module.Class2')
        self.MockClass1 = self.patcher1.start()
        self.MockClass2 = self.patcher2.start()

    def tearDown(self):
        self.patcher1.stop()
        self.patcher2.stop()

    def test_something(self, package=None):
        assert package.module.Class1 is self.MockClass1
        assert package.module.Class2 is self.MockClass2

MyTest('test_something').run()