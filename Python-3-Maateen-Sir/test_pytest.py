# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:07:18 2020

@author: emama
"""

from jijiji import add, is_even

def test_add():
    assert add(2, 3) == 5
    
def test_is_even():
    assert is_even(2) == True
    
