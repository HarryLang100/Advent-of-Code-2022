#%% Read all the lines in the file into a list.
with open("example_input.txt") as f:
    lines = f.read().splitlines()
    
#%% Find the position of the stack numbers.
found_stack_numbers = False
current_line = 0
while not found_stack_numbers:
    if lines[current_line][1] == "1":
        stack_numbers_position = current_line
        found_stack_numbers = True
    current_line += 1
print(stack_numbers_position)

#%% Determine the number of stacks
number_of_stacks = lines[stack_numbers_position][-2:-1]

#%% Split the lines up into the stack lines and the instruction lines.
stack_lines = lines[:stack_numbers_position]
instruction_lines = lines[stack_numbers_position + 2:]

#%% Function to convert an instruction line into a list.
## E.g. "move 1 from 2 to 1" becomes [1, 2, 1]
def convert_instruction_line_to_list(line):
    line_split = line.split(" ")
    return line_split[1], line_split[3], line_split[4]

#%% 