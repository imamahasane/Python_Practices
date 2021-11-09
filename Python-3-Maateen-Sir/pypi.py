#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 03:06:28 2020

@author: imam
"""

import requests

r = requests.get('https://api.github.com/events')
m = r.status_code
print(m)
