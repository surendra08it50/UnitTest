##If you use this technique you must ensure that the patching is 'undone' by calling stop. This can be fiddlier than you might think, because if an exception is raised in the setUp then tearDown is not called. unittest.TestCase.addCleanup() makes this easier:

import unittest
from unittest.mock import patch

class MyTest(unittest.TestCase):
    def setUp(self):
        patcher = patch('package.module.Class')
        self.MockClass = patcher.start()
        self.addCleanup(patcher.stop)

    def test_something(self, package=None):
        assert package.module.Class is self.MockClass


"""As an added bonus you no longer need to keep a reference to the patcher object. It is also possible to stop all patches which have been started by using patch.stopall().


patch.stopall()

Stop all active patches. Only stops patches started with start.        

"""