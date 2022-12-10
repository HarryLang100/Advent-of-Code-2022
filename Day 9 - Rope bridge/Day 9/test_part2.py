import pytest
import inspect
from part2 import follow_instruction_multiple_tails
from part2 import main

# def test_follow_instruction_multiple_tails_example_one():
#     # Inputs.
#     instruction = ["R", 4]
#     H_starting_position = [0, 0]
#     n_tails = 9 # Test purposes only.
#     T_starting_positions = [[0, 0] for index in range(n_tails)]
    
#     # Expected outputs.
#     expected_H_position_list = [
#         [0, 1],
#         [0, 2],
#         [0, 3],
#         [0, 4]]
#     expected_T_positions_list = [
#         [
#             [0, 0],
#             [0, 1],
#             [0, 2],
#             [0, 3]
#         ],
#         [
#             [0, 0],
#             [0, 0],
#             [0, 1],
#             [0, 2]
#         ],
#         [
#             [0, 0],
#             [0, 0],
#             [0, 0],
#             [0, 1]
#         ],
#         [
#             [0, 0],
#             [0, 0],
#             [0, 0],
#             [0, 0]
#         ],
#         [
#             [0, 0],
#             [0, 0],
#             [0, 0],
#             [0, 0]
#         ],
#         [
#             [0, 0],
#             [0, 0],
#             [0, 0],
#             [0, 0]
#         ],
#         [
#             [0, 0],
#             [0, 0],
#             [0, 0],
#             [0, 0]
#         ],
#         [
#             [0, 0],
#             [0, 0],
#             [0, 0],
#             [0, 0]
#         ],
#         [
#             [0, 0],
#             [0, 0],
#             [0, 0],
#             [0, 0]
#         ]]
    
#     # Create actual output.
#     (actual_H_position_list, 
#      actual_T_positions_list) = follow_instruction_multiple_tails(
#          instruction,
#          H_starting_position,
#          T_starting_positions)
        
#     # Assert statements.
#     assert actual_H_position_list == expected_H_position_list
#     assert actual_T_positions_list == expected_T_positions_list
        
def test_main():
    filename = "example_input_part_2.txt"
    expected_output = 36
    actual_output = main(filename)
    message = inspect.cleandoc(f"""
                        The main() function did not work on the example: 
                        returned {actual_output} instead of 
                        {expected_output}.""")
    assert actual_output == expected_output, message