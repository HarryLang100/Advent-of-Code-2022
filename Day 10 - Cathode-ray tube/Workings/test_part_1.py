import pytest
import inspect

from part_1 import parse_input
from part_1 import execute_instruction
from part_1 import create_X_list
from part_1 import main

def test_parse_input_mini_example():
    filename = "../mini_example.txt"
    expected_output = [
        "noop",
        ["addx", 3],
        ["addx", -5]]
    actual_output = parse_input(filename)
    assert actual_output == expected_output
    
    
def test_execute_instruction_mini_example_noop():
    current_X_value = 1
    expected_X_list = [1]
    instruction = "noop"
    actual_X_list = execute_instruction(current_X_value, instruction)
    message = inspect.cleandoc("""
                               The execute_instruction() function did not 
                               work on the 'noop' instruction.""")
    assert actual_X_list == expected_X_list, message
    
def test_execute_instruction_mini_example_addx_positive():
    current_X_value = 1
    expected_X_list = [1, 4]
    instruction = ["addx", 3]
    actual_X_list = execute_instruction(current_X_value, instruction)
    message = inspect.cleandoc("""
                               The execute_instruction() function did not 
                               work on the ['addx', 3] instruction.""")
    assert actual_X_list == expected_X_list, message

def test_execute_instruction_small_mini_addx_negative():
    current_X_value = 4
    expected_X_list = [4, -1]
    instruction = ["addx", -5]
    actual_X_list = execute_instruction(current_X_value, instruction)
    message = inspect.cleandoc("""
                               The execute_instruction() function did not 
                               work on the ['addx', -5] instruction.""")
    assert actual_X_list == expected_X_list, message
    
def test_create_X_list_mini_example():
    instructions = ["noop",
                    ["addx", 3],
                    ["addx", -5]]
    # During cycle     1, 2, 3, 4, 5, 6.
    expected_X_list = [1, 1, 1, 4, 4, -1 ]
    actual_X_list = create_X_list(instructions)
    assert actual_X_list == expected_X_list
    
def test_main_example():
    filename = "../example.txt"
    expected_output = 13140
    actual_output = main(filename)
    message = inspect.cleandoc("""
                               The main() function has failed on the example
                               input.""")
    assert actual_output == expected_output, message
         