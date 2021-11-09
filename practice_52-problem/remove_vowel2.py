# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:41:13 2019

@author: ASUS
"""

vowels = "aeiouAEIOU"
sentence = input("Please enter the sentence: ")

filter_letter = []

for i in sentence:
    if i not in vowels:
        filter_letter.append(i)
        
print("".join(filter_letter))

fi = "".join([i for i in sentence if i not in vowels])