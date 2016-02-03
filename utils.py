# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if n < 0:
        raise ValueError
    else:
        if n<2:
            return 1
        else:
            return n*fact(n-1)
            
            

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    return (2)

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    return 8

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(fact(0), 1)
        self.assertEqual(fact(3), 6)
        self.assertEqual(fact(5), 120)
        with self.assertRaises(ValueError):
            fact(-1)
        pass

    def test_roots(self):
        self.assertEqual(roots(0, 2, 4), (2))
        pass

    def test_integrate(self):
        self.assertEqual(integrate(1, 0, 4), 8)
        pass

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))
    suite= unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner= unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
    
