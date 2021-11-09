# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 06:50:11 2019

@author: Imam Ahasan
"""

a = int(input())
#a_sat = set()
a_input = set(map(int, input().split()))
#a_sat.add(a_input)
    

b = int(input())
#b_sat = set()
b_input = set(map(int, input().split()))
#b_sat.add(b_input)
    
print(len(a_input.union(b_input)))
