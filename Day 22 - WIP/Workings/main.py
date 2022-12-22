import inspect

def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    map_lines = lines[:-2]
    path_line = lines[-1]
    return map_lines, path_line


def calculate_password(final_row, final_column, final_facing):
    result = 1000 * final_row + 4 * final_column + final_facing
    return result


def get_initial_coordinates(map_lines):
    first_period_position = map_lines[0].index(".")
    return 0, first_period_position

def get_new_direction(current_direction, turn_letter):
    """ Letter can be R for 90 degrees clockwise or L for
    90 degrees counterclockwise."""
    R_turn_dictionary = {"N":"E", "E":"S", "S":"W", "W":"N"}
    L_turn_dictionary = {"N":"W", "W":"S", "S":"E", "E":"N"}
    if turn_letter == "L":
        new_direction = L_turn_dictionary.get(current_direction)
    elif turn_letter == "R":
        new_direction = R_turn_dictionary.get(current_direction)
    else:
        message = inspect.cleandoc(f"""
                Invalid turn_letter: {turn_letter}. Expecting
                either "L" or "R""")
        raise Exception(message)
    return new_direction

def get_next_tile_coordinates(current_position, 
                              current_direction, 
                              map_lines):
    
    # What would be the coordinates of the next position?
    if current_direction == "N":
        new_vertical_position = current_position[0] # This will be updated.
        new_horizontal_position = current_position[1]
        next_position_found = False
        while not next_position_found:
            new_vertical_position -= 1 # North one place.
            print(f"Current vertical position: {new_vertical_position}")
            if new_vertical_position == -1: # Wrap around top edge.
                new_vertical_position = len(map_lines) - 1
            try:
                if map_lines[new_vertical_position][new_horizontal_position] != " ":
                    next_position_found = True
            except:
                pass
    return (new_vertical_position, new_horizontal_position)
    
def test_move_north():
    map_lines, path_line = parse_input("../example_input.txt")
    start_position = (7, 0)
    expected_end_position = (6, 0)
    actual_end_position = get_next_tile_coordinates(start_position,
                                                    "N",
                                                    map_lines)
            
# def main(filename):
#     map_lines, path_line = parse_input(filename)
#     current_position = get_initial_coordinates(map_lines)
#     current_direction = "E"
    
#     for instruction in path_line:
        
        