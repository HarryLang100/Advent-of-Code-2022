import pytest
import inspect

from part1 import parse_instructions
from part1 import update_T_based_on_H
from part1 import follow_instruction
from part1 import main

def test_parse_instructions_example():
    actual_output = parse_instructions("example_input.txt")
    expected_output = [["R", 4],
                       ["U", 4],
                       ["L", 3],
                       ["D", 1],
                       ["R", 4],
                       ["D", 1],
                       ["L", 5],
                       ["R", 2]]
    message = inspect.cleandoc("""
                The parse_instructions() function did not work correctly on
                the example input.""")
    assert actual_output == expected_output, message
    
def test_update_T_based_on_H_far_right():
    input_T_position = [0, 0]
    input_H_position = [2, 2]
    expected_output = [1, 1]
    actual_output = update_T_based_on_H(input_H_position, input_T_position)
    message = inspect.cleandoc(f"""
            The 'far right' test for update_T_based_on_H() failed. The
            returned position of T was {actual_output}, instead of 
            {expected_output}.""")
    assert actual_output == expected_output, message
    
def test_update_T_based_on_H_one_right():
    input_T_position = [2, 2]
    input_H_position = [2, 4]
    expected_output = [2, 3]
    actual_output = update_T_based_on_H(input_H_position, input_T_position)
    message = inspect.cleandoc(f"""
            The 'one right' test for update_T_based_on_H() failed. The
            returned position of T was {actual_output}, instead of 
            {expected_output}.""")
    assert actual_output == expected_output, message
    
def test_update_T_based_on_H_one_down():
    input_T_position = [2, 2]
    input_H_position = [0, 2]
    expected_output = [1, 2]
    actual_output = update_T_based_on_H(input_H_position, input_T_position)
    message = inspect.cleandoc(f"""
            The 'one down' test for update_T_based_on_H() failed. The
            returned position of T was {actual_output}, instead of 
            {expected_output}.""")
    assert actual_output == expected_output, message
    
def test_update_T_based_on_H_one_left():
    input_T_position = [2, 2]
    input_H_position = [2, 0]
    expected_output = [2, 1]
    actual_output = update_T_based_on_H(input_H_position, input_T_position)
    message = inspect.cleandoc(f"""
            The 'one left' test for update_T_based_on_H() failed. The
            returned position of T was {actual_output}, instead of 
            {expected_output}.""")
    assert actual_output == expected_output, message
    
def test_update_T_based_on_H_diagonal_up_above():
    input_T_position = [2, 2]
    input_H_position = [4, 3]
    expected_output = [3, 3]
    actual_output = update_T_based_on_H(input_H_position, input_T_position)
    message = inspect.cleandoc(f"""
            The 'diagonal_up_above' test for update_T_based_on_H() failed. The
            returned position of T was {actual_output}, instead of 
            {expected_output}.""")
    assert actual_output == expected_output, message
    
def test_update_T_based_on_H_diagonal_up_right():
    input_T_position = [2, 2]
    input_H_position = [3, 4]
    expected_output = [3, 3]
    actual_output = update_T_based_on_H(input_H_position, input_T_position)
    message = inspect.cleandoc(f"""
            The 'diagonal_up_right' test for update_T_based_on_H() failed. The
            returned position of T was {actual_output}, instead of 
            {expected_output}.""")
    assert actual_output == expected_output, message
    
def test_update_T_based_on_H_overlapping():
    input_T_position = [2, 2]
    input_H_position = [2, 2]
    expected_output = [2, 2]
    actual_output = update_T_based_on_H(input_H_position, input_T_position)
    message = inspect.cleandoc(f"""
            The 'overlapping' test for update_T_based_on_H() failed. The
            returned position of T was {actual_output}, instead of 
            {expected_output}.""")
    assert actual_output == expected_output, message

def test_update_T_based_on_H_touching():
    input_T_position = [2, 2]
    input_H_position = [2, 1]
    expected_output = [2, 2]
    actual_output = update_T_based_on_H(input_H_position, input_T_position)
    message = inspect.cleandoc(f"""
            The 'touching' test for update_T_based_on_H() failed. The
            returned position of T was {actual_output}, instead of 
            {expected_output}.""")
    assert actual_output == expected_output, message


def test_follow_instruction_up_four():
    instruction = ["U", 4]
    H_starting_position = [0, 5]
    T_starting_position = [0, 5]
    expected_H_position_list = [[1, 5], [2, 5], [3, 5], [4, 5]]
    expected_T_position_list = [[0, 5], [1, 5], [2, 5], [3, 5]]
    actual_H_position_list, actual_T_position_list = follow_instruction(
        instruction, 
        H_starting_position,
        T_starting_position)
    assert actual_H_position_list == expected_H_position_list
    assert actual_T_position_list == expected_T_position_list

def test_main():
    filename = "example_input.txt"
    expected_output = 13
    actual_output = main(filename)
    message = inspect.cleandoc(f"""
                    The main() function failed on the exaple input. It
                    returned {actual_output}, instead of {expected_output}.""")
    assert actual_output == expected_output, message