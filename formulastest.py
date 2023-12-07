#Sterling Arnold

import unittest
from formulas import *

class TestFormulas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add([1,2,3,4,5]),15)
        self.assertEqual(add([1,2,3,4,5,0]),15)
        self.assertEqual(add([1,2,3,4,5,-1]),15)
        self.assertEqual(add([1,2,3,4,5,-1,-2]),15)
        self.assertEqual(add([-1,-2,-3,-4,-5]),0)
        self.assertEqual(add([0,0,0,0,0]),0)

    def test_subtract(self):
        self.assertEqual(subtract([1,2,3,4,5]),0)
        self.assertEqual(subtract([1,2,3,4,5,0]),0)
        self.assertEqual(subtract([1,2,3,4,5,-1]),-1)
        self.assertEqual(subtract([1,2,3,4,5,-1,-2]),-3)
        self.assertEqual(subtract([-1,-2,-3,-4,-5]),-15)
        self.assertEqual(subtract([0,0,0,0,0]),0)
    
    def test_multiply(self):
        self.assertEqual(multiply([1,2,3,4,5]),120)
        self.assertEqual(multiply([1,2,3,4,5,0]),120)
        self.assertEqual(multiply([1,2,3,4,5,-1]),-120)
        self.assertEqual(multiply([1,2,3,4,5,-1,-2]),240)
        self.assertEqual(multiply([-1,-2,-3,-4,-5]),-120)
        self.assertEqual(multiply([0,0,0,0,0]),0)
    
    def test_divide(self):
        self.assertEqual(divide([1,2,3,4,5]),0.008333333333333333)
        self.assertEqual(divide([1,2,3,4,5,0]),"Cannot divide by 0")
        self.assertEqual(divide([1,2,3,4,5,-1]),-0.008333333333333333)
        self.assertEqual(divide([1,2,3,4,5,-1,-2]),0.004166666666666667)

if __name__ == '__main__':
    unittest.main()