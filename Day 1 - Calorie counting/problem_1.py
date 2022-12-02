# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:51:50 2022

@author: Harry Lang
"""

current_sum = 0
max_sum = 0

with open("original_input.txt") as input_file:
    lines = input_file.readlines()
    
for current_row in lines:
    if current_row.strip() == "": # If the line is empty.
        current_sum = 0 # Reset the counter.
    else:
        current_sum += int(current_row.strip()) # Add the current number to
        # the count. 
    if current_sum > max_sum:
        max_sum = current_sum

print(f"Result: {max_sum}")