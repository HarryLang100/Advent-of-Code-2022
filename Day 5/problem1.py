# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:58:02 2022

@author: Harry Lang
"""

#%%
with open("example_input.txt") as f:
    lines = f.read().splitlines()
    
found_stack_numbers = False
current_line = 0
while not found_stack_numbers:
    if lines[current_line][1] == "1":
        stack_numbers_position = current_line
        found_stack_numbers = True
    current_line += 1
print(stack_numbers_position)

number_of_stacks = lines[stack_numbers_position][-2:-1]

stack_lines = lines[:stack_numbers_position]
instruction_lines = lines[stack_numbers_position + 2:]

def convert_instruction_line_to_list(line):
    line_split = line.split(" ")
    return line_split[1], line_split[3], line_split[4]

#%%

#stack_lines = [ [] for i in range(number_of_stacks)]
stack = []
for current_stack_num in range(number_of_stacks):
    reached_top = False
    while not reached_top:
        stack[current_stack_num]
    
#%%
lines_upside_down = [stack_lines[-index] for index in range(len(stack_lines))]
print(lines_upside_down)

