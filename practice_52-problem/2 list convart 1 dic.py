# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:53:26 2019

@author: ASUS
"""

a = [11, 22, 33]
b = ["Apple", "Banana", "Painapple"]

my_dic = {}

for i in range(len(a)):
    my_dic[b[i]] = a[i]
print(my_dic)

my_dic = {a[i] : b[i] for i in range(len(a))}
print(my_dic)