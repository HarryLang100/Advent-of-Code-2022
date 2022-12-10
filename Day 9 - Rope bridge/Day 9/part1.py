import inspect

def parse_instructions(filename):
    """Take an instruction input file and output the instructions as a 2D
    list.

    Args:
        filename (string): Name of the file.

    Returns:
        List of instructions, e.g. [['R', 4], ['U', 4], ...].
    """
    instructions_list = []
    with open(filename) as file:
        lines = file.read().splitlines()
    for line in lines:
        line = line.split(" ")
        instructions_list.append([line[0], int(line[1])])
    return instructions_list

 
#%%
def sign(input):
    if input > 0:
        return_value = 1
    elif input < 0:
        return_value = -1
    else:
        return 0
    return return_value

def update_T_based_on_H(H_position, T_position):
    # Make sure inputs are valid.
    message = inspect.cleandoc(f"""
                               H_position is of type {type(H_position)},
                               when it should be a list.""")
    assert isinstance(H_position, list), message
    message = inspect.cleandoc(f"""
                               H_position is of length {len(H_position)},
                               when it should be of length 2 (vertical_
                               position, horizontal_position.""")
    assert len(H_position) == 2, message
    message = inspect.cleandoc(f"""
                               T_position is of type {type(T_position)},
                               when it should be a list.""")
    assert isinstance(T_position, list), message
    message = inspect.cleandoc(f"""
                               T_position is of length {len(T_position)},
                               when it should be of length 2 (vertical_
                               position, horizontal_position.""")
    assert len(T_position) == 2, message
    
    # 
    vertical_distance = H_position[0] - T_position[0]
    horizontal_distance = H_position[1] - T_position[1] 
    if abs(vertical_distance) > 1 and horizontal_distance == 0:
        # Vertical move.
        new_T_position = [T_position[0] + sign(vertical_distance), T_position[1]]
    elif abs(horizontal_distance) > 1 and vertical_distance == 0:
        # Horizontal move.
        new_T_position = [T_position[0], T_position[1] + sign(horizontal_distance)]
    elif (abs(horizontal_distance) > 1 and abs(vertical_distance) == 1 or
          abs(horizontal_distance) == 1 and abs(vertical_distance) > 1):
       new_T_position = [T_position[0] + sign(vertical_distance), T_position[1] + sign(horizontal_distance)]
    elif abs(horizontal_distance) > 2 or abs(vertical_distance) > 2:
       raise Exception("H position and T position not close enough for move.")
    else:
       new_T_position = T_position
    return new_T_position
 
#%%
def follow_instruction(instruction, H_starting_position, T_starting_position):
    H_position_list = []
    T_position_list = []
    H_previous_position = H_starting_position
    T_previous_position = T_starting_position
    direction = instruction[0]
    num_steps = instruction[1]
    for step in range(num_steps):
        H_position_list.append(update_H_one_step(direction, 
                                                 H_previous_position))
        T_position_list.append(update_T_based_on_H(H_position_list[-1], T_previous_position))
        H_previous_position = H_position_list[-1]
        T_previous_position = T_position_list[-1]

    return H_position_list, T_position_list


def update_H_one_step(direction, H_previous_position):
    if direction == "U":
        to_append = [H_previous_position[0] + 1, H_previous_position[1]]
    elif direction == "D":
        to_append = [H_previous_position[0] - 1, H_previous_position[1]]
    elif direction == "R":
        to_append = [H_previous_position[0], H_previous_position[1] + 1]
    elif direction == "L":
        to_append = [H_previous_position[0], H_previous_position[1] - 1]
    else:
        raise Exception(f"Invalid instruction direction: {direction}.")
    return to_append

#%%
def main(filename):
    H_position_history = [[0, 0]]
    T_position_history = [[0, 0]]
    instructions = parse_instructions(filename)
    for instruction in instructions:
            H_to_append, T_to_append = follow_instruction(
                instruction,
                H_position_history[-1],
                T_position_history[-1])
            for item in H_to_append:
                H_position_history.append(item)
            for item in T_to_append:
                T_position_history.append(item)
    T_position_history_unique = []
    for entry in T_position_history:
        if entry not in T_position_history_unique:
            T_position_history_unique.append(entry)
    return len(T_position_history_unique)

#%%
if __name__ == "__main__":
    result = main("input.txt")
    print(f"Number of positions: {result}.")