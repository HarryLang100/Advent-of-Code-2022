import inspect

from part_1 import parse_input
from part_1 import create_X_list

def get_image(X_list):
    to_print = ""
    for pixel_column in range(6): # CRT is 6 high.
        for pixel_row in range(40): # CTR is 40 wide.
            pixel_index = 40 * pixel_column + pixel_row
            sprite_position = get_sprite_position(X_list[pixel_index])
            if pixel_row in sprite_position:
                to_print += "#"
            else:
                    to_print += "."
        if pixel_column != 6:
            to_print += "\n"
    return to_print
                
                    
                    
def get_sprite_position(middle):
    message = inspect.cleandoc(f"""
                               middle must be of type {type(0)}, not of type
                               {type(middle)}""")
    assert isinstance(middle, int), message
    return [middle - 1, middle, middle + 1]
    
message = "The get_image() function did not work correctly on the example."

if __name__ == "__main__":
    X_list = create_X_list(parse_input("../input.txt"))
    print(get_image(X_list))