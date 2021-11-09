#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:18:01 2020

@author: imam
"""

a = ['aaaaa', 'sssssss', 'asgd', 'gb', 'a', 'r', 'qw']
b = [36, 64, 100, 144, 196, 256, 324]

m = {i : j for i, j in zip(a, b)}
print(m)