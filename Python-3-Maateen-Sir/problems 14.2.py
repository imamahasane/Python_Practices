# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:22:54 2020

@author: emama
"""

def gcd(a, b):
    if b > a:
        gcd(b, a)
        
    while b != 0:
        temp = a % b
        a = b
        b = temp
        
    return a

a, b = map(int, input("Please enter tho number: ").split())
print(gcd(a, b))