from mod1.multiplication import Multiplication 

import unittest

class TestMultiplication(unittest.TestCase):

    def test_init(self):
        tester=Multiplication(2,3)
        self.assertEquals(tester.a,2,"test the a value")
        self.assertEquals(tester.b,3,"test the b value")

    def test_multiplication(self):
        tester=Multiplication(2,3)
        self.assertEquals(tester.multiplication(),6,"test the Multiplication value")


