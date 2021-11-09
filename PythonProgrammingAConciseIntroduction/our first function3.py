# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:20:26 2019

@author: ASUS
"""

def areatriangle(b, h):
    area = 0.5 * b * h
    print("The area of a triangle of base", b, "and hight", h, "is", area)
    
areatriangle(5, 8)


def areatriangle(b,h):
    return (0.5 * b * h)

print("The area of a triangle of ",areatriangle(5, 8))