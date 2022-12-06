stacks = [ [] for i in range(3)] # Makes an empty 2D list of length 3.
stacks[0] = ["Z", "N"]
stacks[1] = ["M", "C", "D"]
stacks[2] = ["P"]

instructions = [
        [1, 2, 1],
        [3, 1, 3],
        [2, 2, 1],
        [1, 1, 2]
    ]

def move(stacks, instruction):
    num_to_move = instruction[0]
    from_stack_index = instruction[1] - 1
    to_stack_index = instruction[2] - 1
    for index in range(num_to_move):
        stacks[to_stack_index] += stacks[from_stack_index][-1:]
        del stacks[from_stack_index][-1:]

def get_tops(stacks):
    output = ""
    for stack in stacks:
        output += stack[-1]
    return output

#%%

stacks = [ [] for i in range(3)] # Makes an empty 2D list of length 3.
stacks[0] = ["Z", "N"]
stacks[1] = ["M", "C", "D"]
stacks[2] = ["P"]


print("Original state: ")
print(stacks)
for num, instruction in enumerate(instructions):
    print(stacks)
    move(stacks, instruction)
    print(f"After {num} instructions, the state is:")

print(get_tops(stacks))
    