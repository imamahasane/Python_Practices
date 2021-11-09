# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:24:22 2020

@author: emama
"""

from time import time

def timer(any_fun):
    def count_time():
        start = time()
        any_fun()
        stop = time()
        print(stop - start, "second")
        
def hello():
    print("Hello World!")
    return

def another_fun():
    for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(item)
    return

hello()
another_fun()
        