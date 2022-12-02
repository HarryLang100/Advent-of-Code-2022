# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:48:38 2022

@author: Harry Lang
"""

import pandas as pd

file = pd.read_table("calories_input.txt", header=None)

current_sum = 0
results_list = []
for current_row in range(file.shape[0]):
    if file.iloc[current_row][0] == -1:
        results_list.append(current_sum)
        current_sum = 0
    else:
        current_sum += file.iloc[current_row][0]

results_list.sort(reverse=True)
print(results_list)
top_three_sum = results_list[0] + results_list[1] + results_list[2]
print(f"Sum: {top_three_sum}")