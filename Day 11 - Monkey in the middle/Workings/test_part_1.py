import pytest

import inspect

from part_1 import parse_input
from part_1 import update_worry_level
from part_1 import monkey_turn
from part_1 import get_monkey_business_level
from part_1 import main

def test_parse_input_mini_example():
    filename = "../mini_example_input.txt"
    expected_output = [
        [[79, 98], 
         ['old', '*', '19'],
         23,
         2,
         3],
        [[54, 65, 75, 74],
         ['old', '+', '6'],
         19,
         2,
         0]
        ]
    actual_output = parse_input(filename)
    message = "The parse_input() function did not work on the mini example."
    assert actual_output == expected_output, message
    return actual_output, expected_output

def test_update_worry_level_multiply():
    start_worry_level = 79
    instruction = ['old', '*', '19']
    expected_output_worry_level = 500
    actual_output_worry_level = update_worry_level(start_worry_level, instruction)
    assert actual_output_worry_level == expected_output_worry_level

def test_update_worry_level_add():
    start_worry_level = 54
    instruction = ['old', '+', '6']
    expected_output_worry_level = 20
    actual_output_worry_level = update_worry_level(start_worry_level, instruction)
    assert actual_output_worry_level == expected_output_worry_level

def test_monkey_turn():
    monkey_information = parse_input("../example_input.txt")
    expected_n_items_inspected = 2
    expected_new_monkey_information = [
     [[], ['old', '*', '19'], 23, 2, 3],
     [[54, 65, 75, 74], ['old', '+', '6'], 19, 2, 0],
     [[79, 60, 97], ['old', '*', 'old'], 13, 1, 3],
     [[74, 500, 620], ['old', '+', '3'], 17, 0, 1]]
    
    new_monkey_information, n_items_inspected = monkey_turn(
        0, monkey_information)
    
    assert new_monkey_information == expected_new_monkey_information
    assert n_items_inspected == expected_n_items_inspected
    

def test_get_monkey_business_level():
    inspection_count = [101, 95, 7, 105]
    expected_monkey_business_level= 10605
    actual_monkey_business_level = get_monkey_business_level(inspection_count)
    assert actual_monkey_business_level == expected_monkey_business_level
    
def test_main_example():
    filename = "../example_input.txt"
    n_rounds = 20
    expected_result = 10605
    actual_result = main(filename, n_rounds)
    message = inspect.cleandoc("""
                   The main() function failed on the example input: it returned
                   {actual_result} instead of {expected_result}.""")
    assert actual_result == expected_result, message
    
test