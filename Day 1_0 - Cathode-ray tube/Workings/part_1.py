import inspect

def parse_input(filename):
    instructions = []
    with open(filename) as file:
        lines = file.read().splitlines()
    for line in lines:
        line_split = line.split(" ")
        if line_split[0] == "noop":
            instructions.append("noop")
        elif line_split[0] == "addx":
            instructions.append(["addx", int(line_split[1])])
        else:
            message = inspect.cleandoc(f"""
                                Invalid instruction: {line_split}""")
            raise Exception(message)
    return instructions


def execute_instruction(current_X_value, instruction):
    X_list_to_return = []
    if instruction == "noop":
        X_list_to_return.append(current_X_value)
    elif instruction[0] == "addx":
        X_list_to_return.append(current_X_value)
        X_list_to_return.append(current_X_value + instruction[1])
    return X_list_to_return


def create_X_list(instructions):
    X_history = [1]
    for instruction in instructions:
        new_X_list = execute_instruction(X_history[-1], instruction)
        for X in new_X_list:
            X_history.append(X)
    return X_history

def main(filename):
    instructions = parse_input(filename)
    X_list = create_X_list(instructions)
    running_sum = 0
    for index_position in range(19, len(X_list) + 1, 40):
        signal_strength = X_list[index_position] * (index_position + 1)
        running_sum += signal_strength
    return running_sum
        

#%%
if __name__ == "__main__":
    result = main("../input.txt")
    print(f"Sum of signal strengths: {result}.")