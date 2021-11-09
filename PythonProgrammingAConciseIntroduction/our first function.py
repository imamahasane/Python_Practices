# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:07:33 2019

@author: ASUS
"""

def hello():
    print("Hello, Imam.")
hello()


def hello():
    res = "Hello, Imam."
    return res
print(hello())


def hello(a):
    return a
m = hello("Hello, Imam.")
print(m)