# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 03:49:31 2019

@author: Imam Ahasan
"""

n = int(input())
s = set(map(int, input().split()))
my_list = []

N = int(input())
for j in range(N):
#    for i in range(1,len(s)):
#        s[i] = int(s[i])
        
    if s[0] == "pop":
        my_list.pop()
        
    elif s[0] == "remove":
        my_list.remove(s[-1])
        
    elif s[0] == "discard":
        my_list.discard(s[-1])
        
    elif s[0] == "discard":
        my_list.discard(s[-1])
        
    elif s[0] == "remove":
        my_list.remove(s[-1])
        
    elif s[0] == "pop":
        my_list.pop()
        
    elif s[0] == "discard":
        my_list.discard(s[-1])
        
    elif s[0] == "remove":
        my_list.remove(s[-1])
        
    elif s[0] == "pop":
        my_list.pop()
        
    elif s[0] == "discard":
        my_list.discard(s[-1])
        
    
        


