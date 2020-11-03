#Test are done for calculator functions only

import unittest
import project

class SimpleTest(unittest.TestCase):
    
    def test_addition(self):

        """testing the addition function""" 

        self.assertEqual(project.addition(10,5),15)
        self.assertEqual(project.addition(-7,-5),-12)
        self.assertEqual(project.addition(28,0),28)
        self.assertEqual(project.addition(28,-8),20)

    def test_substraction(self):
               
        """testing the substraction function""" 

        self.assertEqual(project.substraction(-1, -8),7)
        self.assertEqual(project.substraction(10,4),6)
        self.assertEqual(project.substraction(10, 0), 10)
        self.assertEqual(project.substraction(-5, 3), -8)
        self.assertEqual(project.substraction(5, -3), 8)

    def test_multiplication(self):
               
        """testing the multiplication function""" 

        self.assertEqual(project.multiplication(0,5),0)
        self.assertEqual(project.multiplication(-5,-3),15)
        self.assertEqual(project.multiplication(-1,8),-8)
        self.assertEqual(project.multiplication(11,3),33)

    def test_division(self):
               
        """testing the division function""" 

        try:
            r = project.division(10,0)
            self.assertEqual(project.division(36,6),6)
            self.assertEqual(project.division(-36,6),-6)
            self.assertEqual(project.division(-36,-3),12)
            self.assertEqual(project.division(35,-5),-7)
            self.assertEqual(project.division(10,4),2.5)
        except ZeroDivisionError as e:
            self.assertEqual(type(e), ZeroDivisionError)

    def test_power(self):
               
        """testing the power function""" 

        self.assertEqual(project.power(2,2),4)
        self.assertEqual(project.power(2,0),1)
        self.assertEqual(project.power(2,-1),0.5)

    def test_root(self):
               
        """testing the root function""" 

        try:
            r = project.root(-10,-5)
            self.assertEqual(project.root(9,16),"3.0 and 4.0.")
            self.assertEqual(project.root(-5,9),"The first number is bellow 0, the second square root is 3.0.")
            self.assertEqual(project.root(1,-9),"The first square root is 1.0, number is bellow 0.")
        except ValueError as e:
            self.assertEqual(type(e), ValueError)

if __name__=="__main__":
    unittest.main()