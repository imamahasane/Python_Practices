# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:32:38 2019

@author: ASUS
"""

vowels = "aeiou"

sentence = input("Please enter a 'sentence': ")
filtered_letters = []

for letter in sentence:
    if letter not in vowels:
        filtered_letters.append(letter)

print("".join(filtered_letters))

filtered_letters = "".join([letter for letter in sentence if letter not in vowels])
print(filtered_letters)