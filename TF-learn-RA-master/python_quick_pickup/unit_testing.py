import unittest

from test import toUpperCase4testing

class UpperTestingCase(unittest.TestCase):
    """testing for the to upper case in module 'test'"""
    def test_case_1(self):
        result = toUpperCase4testing("sss")
        self.assertEqual(result,"SSS")
        
unittest.main()
