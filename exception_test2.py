import unittest

class DeviceException(Exception):
    def __init__(self, msg, code):
        self.msg = msg
        self.code = code
    def __str__(self):
        return repr("Error {}: {}".format(self.code, self.msg))

class MyDevice(object):
    def __init__(self):
        self.name = 'DefaultName'

    def setParameter(self, param, value):
        if isinstance(value, str):
            setattr(self, param , value)
        else:
            raise DeviceException('Incorrect type of argument passed. Name expects a string', 100001)

    def getParameter(self, param):
        return getattr(self, param)

class TestMyDevice(unittest.TestCase):

    def setUp(self):
        self.dev1 = MyDevice()

    def tearDown(self):
        del self.dev1

    def test_name(self):
        """ Test for valid input for name parameter """

        self.dev1.setParameter('name', 'MyDevice')
        name = self.dev1.getParameter('name')
        self.assertEqual(name, 'MyDevice')

    def test_invalid_name(self):
        """ Test to check if error is raised if invalid type of input is provided """

        self.assertRaises(DeviceException, self.dev1.setParameter, 'name', 1234)

    def test_exception_message(self):
        """ Test to check if correct exception message and code is raised when incorrect value is passed """

        with self.assertRaises(DeviceException) as cm:
            self.dev1.setParameter('name', 1234)
        self.assertEqual(cm.exception.msg, 'Incorrect type of argument passed. Name expects a string', 'mismatch in expected error message')
        self.assertEqual(cm.exception.code, 100001, 'mismatch in expected error code')


if __name__ == '__main__':
    unittest.main()