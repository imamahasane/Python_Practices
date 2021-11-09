# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:15:19 2020

@author: emama
"""

def square(x):
    temp = x ** 2
    print(temp)
    return

def main():
    for i in range(1, 11):
        square(i)
        
if __name__ == "__main__":
    main()
    