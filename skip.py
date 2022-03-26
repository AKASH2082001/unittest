import sys

import Calculator

import unittest

class Mathsoperations(unittest.TestCase):

    @unittest.skipIf(sys.platform.startswith("win"),"Requires not windows OS")
    def test_add(self):
        a=10
        b=2
        c= Calculator.Add(a,b)
        self.assertEqual(c,a+b)
    @unittest.skipUnless(sys.platform.startswith("Linux"),"Requires not windows OS")
    def test_sub(self):
        a=10
        b=5
        c=Calculator.Sub(a,b)
        self.assertEqual(c,a-b)
    @unittest.skip("Skip the test")
    def test_mul(self):
        a=10
        b=2
        c=Calculator.Mul(a,b)
        self.assertEqual(c,a*b)

    def test_div(self):
        a=10
        b=2
        c=Calculator.Div(a,b)
        self.assertEqual(c,a/b)

if __name__ == "__main__":
    unittest.main()