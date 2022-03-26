import unittest

def Add(x,y):
    return x+y
def Sub(x,y):
    return x-y
def Mul(x,y):
    return x*y
def Div(x,y):
    return x/y

class Mathsoperations(unittest.TestCase):

    def setUp(self):
        self.a=10
        self.b=10

    def tearDown(self):
        self.a=0
        self.b=0

    def test_add(self):

        c= Add(self.a,self.b)
        self.assertEqual(c,self.a+self.b)

    def test_sub(self):
        c=Sub(self.a,self.b)
        self.assertEqual(c,self.a-self.b)

    def test_mul(self):
        c=Mul(self.a,self.b)
        self.assertEqual(c,self.a*self.b)

    def test_div(self):
        c=Div(self.a,self.b)
        self.assertEqual(c,self.a/self.b)

if __name__ == "__main__":
    unittest.main()