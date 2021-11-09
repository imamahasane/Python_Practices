# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:18:12 2020

@author: emama
"""

import unittest
from unit_test import add, is_even

class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_is_even(self):
        self.assertTrue(is_even(2))
        
   
if __name__ == '__main__':
    unittest.main()