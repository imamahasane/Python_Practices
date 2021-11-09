# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 12:47:34 2019

@author: emama
"""

user_input = int(input())

ascending_list = []
for i in range(user_input):
    vari = input()
    v = sorted(vari)
    

cou = v.count('t')
print('t = ',cou)
