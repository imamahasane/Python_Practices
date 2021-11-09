# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 07:22:25 2019

@author: Imam Ahasan
"""

a = int(input())
a_input = set(map(int, input().split()))
    
b = int(input())
b_input = set(map(int, input().split()))
    
print(len(a_input.difference(b_input)))