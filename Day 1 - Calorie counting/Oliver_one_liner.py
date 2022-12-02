# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:53:27 2022

@author: Harry Lang
"""

from itertools import groupby
with open("calories_input.txt") as f:
     print(max(sum(map(lambda x: int(x.strip()), elf)) for elf in (g for k,g in groupby(f.readlines(), key=lambda x: bool(x.strip()) ) if k)))