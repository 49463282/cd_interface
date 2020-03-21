import unittest
from case.TestLogin import TestLogin
from case.TestCd import TestCd
suite = unittest.TestSuite()


suite.addTest(TestLogin('test_login'))
suite.addTest(TestCd('test_order'))
unittest.TextTestRunner().run(suite)

