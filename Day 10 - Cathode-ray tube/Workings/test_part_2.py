import pytest

from part_1 import parse_input
from part_1 import create_X_list
from part_2 import get_image

def test_get_image():
    expected_image = "##..##..##..##..##..##..##..##..##..##..\n" +\
                     "###...###...###...###...###...###...###.\n" +\
                     "####....####....####....####....####....\n" +\
                     "#####.....#####.....#####.....#####.....\n" +\
                     "######......######......######......####\n" +\
                     "#######.......#######.......#######.....\n"
    print(expected_image)
    X_list = create_X_list(parse_input("../example.txt"))
    actual_image = get_image(X_list)
    message = "The get_image() function did not work correctly on the example."
    assert actual_image == expected_image, message
    
