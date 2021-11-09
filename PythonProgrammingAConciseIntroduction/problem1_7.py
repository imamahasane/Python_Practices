# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 12:09:46 2019

@author: ASUS
"""

def problem1_7():
    b1 = input("Enter the length of one of the bases: ")
    b2 = input("Enter the length of the other base: ")
    h = input("Enter the height: ")
    A = (1/2) * (float(b1)+float(b2)) * float(h)

    print("The area of a trapezoid with bases", float(b1), "and", float(b2), "and height", float(h), "is",float(A))
