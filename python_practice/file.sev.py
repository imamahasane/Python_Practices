# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 01:39:59 2020

@author: emama
"""

import requests

url = "http://www.subeen.com/allposts/"

response = requests.get(url)

with open("dimik.html", "w") as f:
    f.write(response.text)