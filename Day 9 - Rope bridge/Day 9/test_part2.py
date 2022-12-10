import pytest
from part2 import follow_instruction_multiple_tails

def test_follow_instruction_multiple_tails_example_one():
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
        
    # Assert statements.
    assert actual_H_position_list == expected_H_position_list
    assert actual_T_positions_list == expected_T_positions_list
        