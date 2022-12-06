#%%

import pdb

#%% Cheating instead of parsing
from create_stacks_manual import stacks, stacks_example

use_test_input = False
if use_test_input:
    filename = "example_input.txt"
    stacks = stacks_example
else:
    filename = "input.txt"
    stacks = stacks
#%% Helper functions.

def move(stacks, instruction):
    num_to_move = instruction[0]
    from_stack_index = instruction[1] - 1
    to_stack_index = instruction[2] - 1
    for index in range(num_to_move):
        stacks[to_stack_index] += stacks[from_stack_index][-1:]
        del stacks[from_stack_index][-1:]
        
def move_keep_order(stacks, instruction):
    num_to_move = instruction[0]
    from_stack_index = instruction[1] - 1
    to_stack_index = instruction[2] - 1
    stacks[to_stack_index] += stacks[from_stack_index][-1*num_to_move:]
    del stacks[from_stack_index][-1*num_to_move:]
    
def get_tops(stacks):
    output = ""
    for stack in stacks:
        output += stack[-1]
    return output

def convert_instruction_line_to_list(line):
## E.g. "move 1 from 2 to 1" becomes [1, 2, 1]
    line_split = line.split(" ")
    return int(line_split[1]), int(line_split[3]), int(line_split[5])

# %% Reading and parsing

with open(filename) as f:
    lines = f.read().splitlines()
    
found_stack_numbers = False
current_line = 0
while not found_stack_numbers:
    if lines[current_line][1] == "1":
        stack_numbers_position = current_line
        found_stack_numbers = True
    current_line += 1

number_of_stacks = int(lines[stack_numbers_position][-2])

stack_lines = lines[:stack_numbers_position]
instruction_lines = lines[stack_numbers_position + 2:]

    

    
# %% Convert instructions from text to lists.
instructions_lists = []
for line in instruction_lines:
    instructions_lists.append(convert_instruction_line_to_list(line))

#%% Actual work.

print(*stacks, sep="\n")
print()
for num, instruction in enumerate(instructions_lists):
    print(instruction)
    move_keep_order(stacks, instruction)
    print(*stacks, sep="\n")
    print()

print(get_tops(stacks))