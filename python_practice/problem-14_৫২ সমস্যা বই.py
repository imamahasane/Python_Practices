# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 07:20:33 2019

@author: Imam Ahasan
"""

li = []
T = int(input())

for i in range(T):
    first_input = input()
    second_input = input()
    
    c = first_input.count(second_input)

    p = "Occurrence of \'{}\' in \'{}\' = {}".format(second_input, first_input, c)
    
    p2 = "\'{}\' is not present".format(second_input)
    
    if c != 0:
        li.append(p)
    else:
        li.append(p2)
    
    for j in li:
        print(j)
         