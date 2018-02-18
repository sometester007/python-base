from mod1.add import Add 

import unittest

class TestAdd(unittest.TestCase):
    def test_init(self):
        tester=Add(2,3)
        self.assertEquals(tester.a,2,"test the a value")
        self.assertEquals(tester.b,3,"test the b value")

    def test_add(self):
        tester=Add(2,3)
        self.assertEquals(tester.add(),5,"test the add value")


