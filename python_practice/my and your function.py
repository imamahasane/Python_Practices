# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 05:40:31 2019

@author: Imam Ahasan
"""

def my_function(n):
    i = 1
    while i <= n:
        print(i)
        i += 1
        
def your_function(m):
    l = []
    for i in m:
        if i % 2 == 0:
            l.append(i)
    print(l)
            
def main_function():
    my_function(20)
    your_function(44)
    
if __name__ == "__main__":
    main_function