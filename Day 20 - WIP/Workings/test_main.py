import pytest

from main import get_coordinate_sum
from main import move_number
from main import parse_input
from main import main

class TestMain(object):
    def test_example(self):
        filename = "../example_input.txt"
        expected_output = 3
        actual_output = main(filename)
        assert actual_output == expected_output

class TestGetCoordinateSum(object):
    def test_get_coordinate_sum_example_input(self):
        input_numbers = [1, 2, -3, 4, 0, 3, -2]
        expected_output = 3
        actual_output = get_coordinate_sum(input_numbers)
        assert actual_output == expected_output
        

class TestMoveNumber(object):
    def test_move_number_forward(self):
        number_to_move = 2
        current_index = 1
        input_numbers = [1, 2, 3, 4, 5]
        expected_output = [1, 3, 4, 2, 5]
        actual_output = move_number(number_to_move, current_index, input_numbers)
        assert actual_output == expected_output
    
    def test_move_number_forward_to_end(self):
        number_to_move = 3
        current_index = 1
        input_numbers = [1, 3, 3, 4, 5]
        expected_output = [1, 3, 4, 5, 3]
        actual_output = move_number(number_to_move, current_index, input_numbers)
        assert actual_output == expected_output
    
    def test_move_number_forward_same_place(self):
        number_to_move = 2
        current_index = 1
        input_numbers = [1, 2]
        expected_output = [1, 2]
        actual_output = move_number(number_to_move, current_index, input_numbers)
        assert actual_output == expected_output
    
    def test_move_number_backward(self):
        number_to_move = -3
        current_index = 1
        input_numbers = [1, -3, 2, 3, -2, 0, 4]
        expected_output = [1, 2, 3, -2, -3, 0, 4]
        actual_output = move_number(number_to_move, current_index, input_numbers)
        assert actual_output == expected_output
    
    def test_move_number_smaller_index(self):
        number_to_move = -3
        current_index= 5
        input_numbers = [1, 2, 3, 4, 5, -3, 6, 7]
        expected_output = [1, 2, -3, 3, 4, 5, 6, 7]
        actual_output = move_number(number_to_move, current_index, input_numbers)
        assert actual_output == expected_output
    
class TestParseInput(object):
    def test_on_example(self):
        filename = "../example_input.txt"
        expected_output = [1, 2, -3, 3, -2, 0, 4]
        actual_output = parse_input(filename)
        assert actual_output == expected_output