# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:48:38 2022

@author: Harry Lang
"""

import pandas as pd

file = pd.read_table("calories_input.txt", header=None)

current_sum = 0
max_sum = 0
for current_row in range(file.shape[0]):
    if file.iloc[current_row][0] == -1:
        #current_sum = 0
        pass
    else:
        current_sum += file.iloc[current_row][0]
    if current_sum > max_sum:
        max_sum = current_sum

print(f"Sum of calories: {max_sum}")

