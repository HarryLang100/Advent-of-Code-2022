import pytest
import inspect
from part2 import follow_instruction_multiple_tails
from part2 import main
from part2 import update_Ts_one_step

def test_update_Ts_one_step():
    new_H_position = [0, 2]
    current_T_positions = [[0, 0] for index in range(9)]
    
    expected_new_T_positions = [[0, 1], [0, 0], [0, 0], [0, 0], [0, 0], 
                                [0, 0], [0, 0], [0, 0], [0, 0]]
    
    actual_new_T_positions = update_Ts_one_step(
        current_T_positions, new_H_position)
    
    assert actual_new_T_positions == expected_new_T_positions
    
def test_update_Ts_one_step_b():
    new_H_position = [0, 3]
    current_T_positions = [[0, 1], [0, 0], [0, 0], [0, 0], 
                            [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    expected_T_new_positions = [[0, 2], [0, 1], [0, 0], [0, 0], 
                                [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    actual_T_new_positions = update_Ts_one_step(
        current_T_positions, new_H_position)
    assert actual_T_new_positions == expected_T_new_positions
    
# def test_update_Ts_one_step_c():
#     new_H_position = [4, 6]
#     current_T_positions = [[4, 5], [3, 5], [2, 4], [2, 3], [2, 2], 
#                            [0, 0], [0, 0], [0, 0], [0, 0]]
#     expected_T_new_positions = [[4, 5], [3, 5], [2, 4], [2, 3], 
#                                 [2, 2], [0, 0], [0, 0], [0, 0], [0, 0]]
#     actual_T_new_positions = update_Ts_one_step(
#         current_T_positions, new_H_position)
    
#     assert actual_T_new_positions == expected_T_new_positions
    
#%%

# def test_follow_instruction_multiple_tails_example_one():
#     instruction = ["R", 4]
#     n_tails = 9 # Test purposes only.
#     H_starting_position = [0, 0]
#     T_starting_positions = [[0, 0] for index in range(n_tails)]
    
#     expected_new_H_position = [0, 4]
#     expected_new_T_positions = [
#         [0, 3],
#         [0, 2],
#         [0, 1],
#         [0, 0],
#         [0, 0],
#         [0, 0],
#         [0, 0],
#         [0, 0],
#         [0, 0]]
#     expected_final_tail_position_list = [[0, 0] for index in range(4)]
    
    
#     # Create actual output.
#     (actual_H_new_position, 
#      actual_new_T_positions,
#      actual_final_tail_position_list) = follow_instruction_multiple_tails(
#           instruction,
#           H_starting_position,
#           T_starting_positions)
        
#     # Assert statements.
#     assert actual_H_new_position == expected_new_H_position
#     assert actual_new_T_positions == expected_new_T_positions
#     assert actual_final_tail_position_list == expected_final_tail_position_list
    
def test_follow_instruction_multiple_tails_example_a():
    instruction = ["R", 1]
    n_tails = 9 # Test purposes only.
    H_starting_position = [0, 0]
    T_starting_positions = [[0, 0] for index in range(n_tails)]
    
    expected_new_H_position = [0, 1]
    expected_new_T_positions = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]]
    expected_final_tail_position_list = [[0, 0] for index in range(1)]
    
    # Create actual output.
    (actual_H_new_position, 
      actual_new_T_positions,
      actual_final_tail_position_list) = follow_instruction_multiple_tails(
          instruction,
          H_starting_position,
          T_starting_positions)

    # Assert statements.
    assert actual_H_new_position == expected_new_H_position
    assert actual_new_T_positions == expected_new_T_positions
    assert actual_final_tail_position_list == expected_final_tail_position_list
    
def test_follow_instruction_multiple_tails_example_b():
    instruction = ["R", 2]
    n_tails = 9 # Test purposes only.
    H_starting_position = [0, 0]
    T_starting_positions = [[0, 0] for index in range(n_tails)]
    
    expected_new_H_position = [0, 2]
    expected_new_T_positions = [
        [0, 1],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]]
    expected_final_tail_position_list = [[0, 0] for index in range(2)]
    
    # Create actual output.
    (actual_H_new_position, 
      actual_new_T_positions,
      actual_final_tail_position_list) = follow_instruction_multiple_tails(
          instruction,
          H_starting_position,
          T_starting_positions)

    # Assert statements.
    assert actual_H_new_position == expected_new_H_position
    assert actual_new_T_positions == expected_new_T_positions
    assert actual_final_tail_position_list == expected_final_tail_position_list
    
    # Create actual output.
    (actual_H_new_position, 
      actual_new_T_positions,
      actual_final_tail_position_list) = follow_instruction_multiple_tails(
          instruction,
          H_starting_position,
          T_starting_positions)
          
def test_follow_instruction_multiple_tails_example_c():
    instruction = ["R", 3]
    n_tails = 9 # Test purposes only.
    H_starting_position = [0, 0]
    T_starting_positions = [[0, 0] for index in range(n_tails)]
    
    expected_new_H_position = [0, 3]
    expected_new_T_positions = [
        [0, 2],
        [0, 1],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0]]
    expected_final_tail_position_list = [[0, 0] for index in range(3)]
    
    # Create actual output.
    (actual_H_new_position, 
      actual_new_T_positions,
      actual_final_tail_position_list) = follow_instruction_multiple_tails(
          instruction,
          H_starting_position,
          T_starting_positions)

    # Assert statements.
    assert actual_H_new_position == expected_new_H_position
    assert actual_new_T_positions == expected_new_T_positions
    assert actual_final_tail_position_list == expected_final_tail_position_list
    
    # Create actual output.
    (actual_H_new_position, 
      actual_new_T_positions,
      actual_final_tail_position_list) = follow_instruction_multiple_tails(
          instruction,
          H_starting_position,
          T_starting_positions)
        
#     # Assert statements.
#     assert actual_H_new_position == expected_new_H_position
#     assert actual_new_T_positions == expected_new_T_positions
#     assert actual_final_tail_position_list == expected_final_tail_position_list


        
def test_main():
    filename = "example_input_part_2.txt"
    expected_output = 36
    actual_output = main(filename)
    message = inspect.cleandoc(f"""
                        The main() function did not work on the example: 
                        returned {actual_output} instead of 
                        {expected_output}.""")
    assert actual_output == expected_output, message