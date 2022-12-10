import pdb

import inspect

from part1 import update_T_based_on_H
from part1 import follow_instruction
from part1 import update_H_one_step
from part1 import parse_instructions

def update_Ts_one_step(current_T_positions, new_H_position):
    print("About to update T positions.")
    print(f"Current T positions: {current_T_positions}.")
    """

    Args:
        current_T_positions (list): List of the current position for each
        tail. Each position is a list of length 2.
        new_H_position (list): List of the new position of H. This is a list
        of length 2.

    Returns:
        new_T_positions.
    """
    
    # Check that the inputs are reasonable.
    message = inspect.cleandoc(f"""
        current_T_positions must be a list, not of type 
        {type(current_T_positions)}""")
    assert isinstance(current_T_positions, list), message
    for position in current_T_positions:
        message = inspect.cleandoc(f"""
                        Each member of current_T_position must be 
                        a list. Found an object of type {type(position)})""")
        assert isinstance(position, list), message
        message = inspect.cleandoc(f"""
                        Each member of current_T_position must be 
                        a list of length 2. Found an object of 
                        length {len(position)})""")
        assert len(position) == 2, message
    
    # Instantiate variables.
    new_T_positions = []
    # Update position of first tail (based on head)
    print("Updating first tail.")
    new_T_positions.append(update_T_based_on_H(new_H_position,
                                               current_T_positions[0]))
    
    # Update the rest of the tails (based on previous tail).
    for tail_index in range(1, len(current_T_positions)):
        new_T_positions.append(update_T_based_on_H(
            #new_T_positions[tail_index - 1],
            current_T_positions[tail_index - 1],
            current_T_positions[tail_index]))
    
    return new_T_positions


def follow_instruction_multiple_tails(instruction,
                                      H_starting_position,
                                      T_starting_positions):
    """
    Returns:
        new_H_position
        new_T_positions
        list of final tail locations
    """
    final_tail_position_list = []
    H_previous_position = H_starting_position
    T_previous_positions = T_starting_positions
    direction = instruction[0]
    num_steps = instruction[1]
    print(f"num_steps: {num_steps}")
    
    for step in range(num_steps):
        # Get new H position.
        new_H_position = update_H_one_step(direction, 
                                           H_previous_position)
        
        # Update previous H position
        H_previous_position = new_H_position
        
        
        # Get new T positions.
        T_new_positions = update_Ts_one_step(
            T_previous_positions,
            new_H_position)
        
        # Update previous T positions
        T_previous_positions = T_new_positions
        final_tail_position_list.append(T_previous_positions[-1])

    return new_H_position, T_new_positions, final_tail_position_list

#%%
def main(filename):
    n_tails = 9 # This is true both in the example and actual input.
    H_position = [0, 0]
    T_positions = [[0, 0] for index in range(n_tails)]
    final_tail_position_history = []
    instructions = parse_instructions(filename)
    for instruction in instructions:
        print(f"Current instruction: {instruction}.")
        H_position, T_positions, final_tail_position_list = \
            follow_instruction_multiple_tails(
                instruction,
                H_position, 
                T_positions)
        print(f"New H position: {H_position}.")
        for item in final_tail_position_list:
            final_tail_position_history.append(item)
    print(f"Final tail position history: {final_tail_position_history}.")
                
    # Finally, count the number of unique tail positions.
    unique_position_counter = 0
    unique_positions_found = []
    for position in final_tail_position_history:
        if position not in unique_positions_found:
            unique_positions_found.append(position)
            unique_position_counter += 1
    
    #
    return unique_position_counter

#%%
if __name__ == "__main__":
    result = main("example_input_part_2.txt") # Expect 36.
    print(result)