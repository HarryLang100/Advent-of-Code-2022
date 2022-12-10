import pdb

from part1 import update_T_based_on_H
from part1 import follow_instruction
from part1 import update_H_one_step

#%%
def follow_instruction_multiple_tails(instruction,
                                      H_starting_position,
                                      T_starting_positions,
                                      n_tails):
    # Setup.
    H_position_list = []
    T_positions_list = [[] for index in range(n_tails)]
    H_previous_position = H_starting_position
    T_previous_positions = T_starting_positions
    direction = instruction[0]
    num_steps = instruction[1]
    
    # Repeat the instruction the required number of times.
    for step in range(num_steps):
        
        H_position_list.append(update_H_one_step(direction, 
                                                 H_previous_position))
        # Update the first tail.
        T_previous_positions[0].append(update_T_based_on_H(
            H_previous_position, 
            T_previous_positions[0]))
        
        # Update the rest of the tails.
        for index in range(1, n_tails):
            print(T_previous_positions)
            T_previous_positions[index] = update_T_based_on_H(
                    T_previous_positions[index - 1][-1],
                    T_previous_positions[index][-1])
        
        #
        for index in range(n_tails):
            T_positions_list[index].append(T_previous_positions[index][-1])
        
        #   
        return H_position_list, T_positions_list
            

#%%
# Inputs.
instruction = ["R", 4]
H_starting_position = [0, 0]
n_tails = 9
T_starting_positions = [[0, 0] for index in range(n_tails)]

# Expected outputs.
expected_H_position_list = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4]]
expected_T_positions_list = [
    [
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 3]
    ],
    [
        [0, 0],
        [0, 0],
        [0, 1],
        [0, 2]
    ],
    [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]
    ],
    [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]
    ],
    [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]
    ],
    [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]
    ],
    [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]
    ],
    [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]
    ]]

# Create actual output.
(actual_H_position_list, 
 actual_T_positions_list) = follow_instruction_multiple_tails(
     instruction,
     H_starting_position,
     T_starting_positions,
     n_tails
         )