import pytest

from main import parse_input
from main import calculate_password
from main import get_new_direction

class TestParseInput(object):
    def test_on_example(self):
        filename = "../example_input.txt"
        expected_map = [
            "        ...#",
            "        .#..",
            "        #...",
            "        ....",
            "...#.......#",
            "........#...",
            "..#....#....",
            "..........#.",
            "        ...#....",
            "        .....#..",
            "        .#......",
            "        ......#."]         
        expected_path = "10R5L5R10L4R5L5"
        actual_map, actual_path = parse_input(filename)
        assert actual_map == expected_map
        assert actual_path == expected_path

class TestCalculatePassword(object):
    def test_on_example(self):
        expected_output = 6032
        actual_output = calculate_password(6, 8, 0)
        assert actual_output == expected_output

class TestGetNewDirection(object):
    def test_North_turn_clockwise(self):
        expected_output = "E"
        actual_output = get_new_direction("N", "R")
        assert actual_output == expected_output
        
    def test_North_turn_counterclockwise(self):
        expected_output = "W"
        actual_output = get_new_direction("N", "L")
        assert actual_output == expected_output