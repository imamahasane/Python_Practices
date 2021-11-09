# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 06:56:15 2019

@author: Imam Ahasan
"""

def mutate_string(string, position, character):
    re = string[:position] + character + string[position + 1:]
    return re

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)