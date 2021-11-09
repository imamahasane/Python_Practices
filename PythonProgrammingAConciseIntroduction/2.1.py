# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 06:58:31 2019

@author: ASUS
"""

nlis = [2,4,8,105,210,-3,47,8,33,1]
rlis = [3.14, 7.26, -4.76, 0, 8.24, 9.1, -100.7, 4]

def average(numlis):
    for i in numlis:
        print(i)
    print("average should by", sum(numlis) / len(numlis))
        
average(nlis)
average(rlis)