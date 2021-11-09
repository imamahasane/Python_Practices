#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:52:04 2020

@author: imam
"""

a = ['aaaaa', 'sssssss', 'asgd', 'gb', 'a', 'r', 'qw']

m = {i for i in a if len(i) > 2}
print(m)