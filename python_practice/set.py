# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 03:40:49 2019

@author: Imam Ahasan
"""

arr = []
n = int(input())
for i in range(n):
    s = input().split()
    for i in range(1,len(s)):
        s[i] = int(s[i])
        
    if s[0] == "insert":                          
        arr.insert(s[1],s[2])

    elif s[0] == "print":
        print (arr)
        
    elif s[0] == "remove":
        arr.remove(s[1])
        
    elif s[0] == "append":
        arr.append(s[1])
        
    elif s[0] == "sort":
        arr.sort()
                
    elif s[0] == "pop":
        arr.pop()
        
    elif s[0] == "reverse":
        arr.reverse()
