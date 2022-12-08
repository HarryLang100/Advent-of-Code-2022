
def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    forest = [[] for i in range(len(lines))]
    for line_index, line in enumerate(lines):
        forest[line_index] = [int(letter) for letter in line]
    return forest


#%%
def find_viewing_distance_west(tree_coordinates, forest):
     current_looking_distance = 1
     view_obstructed = False
     tree_height = forest[tree_coordinates[0]][tree_coordinates[1]]
    
     while not view_obstructed:
         if tree_coordinates[1] - current_looking_distance < 0:
             break 
         current_tree_height = forest[tree_coordinates[0]][tree_coordinates[1] - current_looking_distance]
         if current_tree_height >= tree_height: # Obstructs view
             view_obstructed = True
             current_looking_distance += 1
         else:
          current_looking_distance += 1
     return current_looking_distance - 1   


#%%
def find_viewing_distance_east(tree_coordinates, forest):
    current_looking_distance = 1
    view_obstructed = False
    tree_height = forest[tree_coordinates[0]][tree_coordinates[1]]
    
    while not view_obstructed:
        print(f"Current looking distance: {current_looking_distance}")
        if tree_coordinates[1] + current_looking_distance >= len(forest[0]):
            current_looking_distance += 1
            print("Reached edge")
            break
        current_tree_height = forest[tree_coordinates[0]][tree_coordinates[1] + current_looking_distance]
        if current_tree_height >= tree_height: # Obstructs view
             view_obstructed = True
             current_looking_distance += 1
        else:
          current_looking_distance += 1
          
    return current_looking_distance - 1
 
    
#%% 
def find_viewing_distance_north(tree_coordinates, forest):
    current_looking_distance = 1
    view_obstructed = False
    tree_height = forest[tree_coordinates[0]][tree_coordinates[1]]
    
    while not view_obstructed:
        if tree_coordinates[0] - current_looking_distance < 0:
            break 
        current_tree_height = forest[tree_coordinates[0] - current_looking_distance][tree_coordinates[1]]
        if current_tree_height >= tree_height: # Obstructs view
            current_looking_distance += 1
            view_obstructed = True
        else:
            current_looking_distance += 1
    return current_looking_distance - 1
#%%
def find_viewing_distance_south(tree_coordinates, forest):
    current_looking_distance = 1
    view_obstructed = False
    tree_height = forest[tree_coordinates[0]][tree_coordinates[1]]
    
    while not view_obstructed:
        if tree_coordinates[0] + current_looking_distance >= len(forest):
            break 
        current_tree_height = forest[tree_coordinates[0] + current_looking_distance][tree_coordinates[1]]
        if current_tree_height >= tree_height: # Obstructs view
            current_looking_distance += 1
            view_obstructed = True
        else:
            current_looking_distance += 1
    return current_looking_distance - 1   


#%%
def get_scenic_score(tree_coordinates, forest):
    north_vd = find_viewing_distance_north(tree_coordinates, forest)
    south_vd = find_viewing_distance_south(tree_coordinates, forest)
    east_vd = find_viewing_distance_east(tree_coordinates, forest)
    west_vd = find_viewing_distance_west(tree_coordinates, forest)
    scenic_score = north_vd * south_vd * east_vd * west_vd
    return scenic_score

#%%
filename = "input.txt"
forest = parse_input(filename)

#%%
forest_height = len(forest)
forest_width = len(forest[0])

#%%
max_scenic_score = 0

for row_index in range(forest_height):
    for col_index in range(forest_width):
        print(f"Row index: {row_index} | Col index: {col_index}")
        if get_scenic_score([row_index, col_index], forest) > max_scenic_score:
            max_scenic_score = get_scenic_score([row_index, col_index], forest)
print(f"Max scenic score: {max_scenic_score}")