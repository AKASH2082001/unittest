import unittest

def Mylist():
    list=[1,2,3,4,5]
    return list

class mylistcheck(unittest.TestCase):

    def test_list(self):
        element= 2
        self.assertIn(element, Mylist())

    def test_list2(self):
        element= 10
        self.assertNotIn(element, Mylist())

if __name__ == "__main__":
    unittest.main()