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

def check_next_tile(current_position, 
                    current_direction, 
                    map_lines):
    
    # What would be the coordinates of the next position?
    if current_direction == "N":
        next_position = (current_position[0] - 1,
                         current_position[1])
    elif current_direction == "S":
        next_position = (current_position[0] + 1,
                         current_position[1])
    elif current_direction == "E":
        next_position = (current_position[0],
                         current_position[1] + 1)
    elif current_direction == "E":
        next_position = (current_position[0],
                         current_position[1] - 1)
    
    # Does it wrap around the map?
    if 
    
# def main(filename):
#     map_lines, path_line = parse_input(filename)
#     current_position = get_initial_coordinates(map_lines)
#     current_direction = "E"
    
#     for instruction in path_line:
        
        