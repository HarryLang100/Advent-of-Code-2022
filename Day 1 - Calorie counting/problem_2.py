# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:48:38 2022

@author: Harry Lang
"""

with open("input.txt") as input_file:
    lines = input_file.readlines()

current_sum = 0
results_list = []
for current_line in lines:
    if current_line.strip() == "":
        results_list.append(current_sum)
        current_sum = 0
    else:
        current_sum += int(current_line.strip())

results_list.sort(reverse=True)
top_three_sum = results_list[0] + results_list[1] + results_list[2]
print(f"Sum: {top_three_sum}")