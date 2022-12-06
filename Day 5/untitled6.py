# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:35:23 2022

@author: Harry Lang
"""

stack_lines = ['    [D]    ', '[N] [C]    ', '[Z] [M] [P]']
intended_output =  [
    ["Z", "N"],
    ["M", "C", "D"],
    ["P"]
     ]

num_stacks = 3

stack = [[]*num_stacks]

for current_line_index in range(len(stack_lines), 0, -1):
    for current_stack_index in range(num_stacks):
        print(f"Current stack index: {current_stack_index}")
        try:
            stack[current_stack_index].append(stack_lines[current_line_index][4*current_stack_index + 1])
            print("Appended something! Now this is the stack")
            print(stack)
        except:
            pass

print(stack == intended_output)s