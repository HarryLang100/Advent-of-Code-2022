# =============================================================================
# def get_next_tile_coordinates(current_position, 
#                               current_direction, 
#                               map_lines):
#     
#     # What would be the coordinates of the next position?
#     if current_direction == "N":
#         new_vertical_position = current_position[0] # This will be updated.
#         new_horizontal_position = current_position[1]
#         next_position_found = False
#         while not next_position_found:
#             new_vertical_position -= 1 # North one place.
#             print(f"Current vertical position: {new_vertical_position}")
#             if new_vertical_position == -1: # Wrap around top edge.
#                 new_vertical_position = len(map_lines) - 1
#             try:
#                 if map_lines[new_vertical_position][new_horizontal_position] != " ":
#                     next_position_found = True
#             except:
#                 pass
#     return (new_vertical_position, new_horizontal_position)
#     
# def test_move_north():
#     map_lines, path_line = parse_input("../example_input.txt")
#     start_position = (7, 0)
#     expected_end_position = (6, 0)
#     actual_end_position = get_next_tile_coordinates(start_position,
#                                                     "N",
#                                                     map_lines)
# =============================================================================

def get_next_potential_position(current_position, 
                                current_direction,
                                map_lines):
    
    assert current_direction in ("N", "S", "E", "W")
    
    if current_direction == "N":
        potential_new_position = (current_position[0] - 1, 
                                  current_position[1])
    elif current_direction 
    

def execute_instruction(current_position,
                        current_direction,
                        map_lines,
                        number_to_move):

    