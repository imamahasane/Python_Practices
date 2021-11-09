# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:23:04 2020

@author: emama
"""

import requests

img_url = "html://goo.gl/JxKtPw"

r = requests.get(img_url)

with open("pybook1.png", "w") as f:
    f.write(r.content)