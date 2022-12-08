

#%%
test_forest = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0]]

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

if (find_viewing_distance_west([0, 0], test_forest) == 0 and
    find_viewing_distance_west([1, 1], test_forest) == 1):
        print("West tests passed")
else:
    print("West tests failed")

#%%
def find_viewing_distance_east(tree_coordinates, forest):
    current_looking_distance = 1
    view_obstructed = False
    tree_height = forest[tree_coordinates[0]][tree_coordinates[1]]
    
    while not view_obstructed:
        if tree_coordinates[1] + current_looking_distance >= len(forest[0]):
            break
        current_tree_height = forest[tree_coordinates[0]][tree_coordinates[1] + current_looking_distance]
        if current_tree_height >= tree_height: # Obstructs view
             view_obstructed = True
             current_looking_distance += 1
        else:
          current_looking_distance += 1
    return current_looking_distance - 1   
 
if (find_viewing_distance_east([0, 0], test_forest) == 1 and
    find_viewing_distance_east([1, 1], test_forest) == 0):
        print("East tests passed")
else:
    print("East tests failed")
    
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

if (find_viewing_distance_north([0, 0], test_forest) == 0 and
    find_viewing_distance_north([1, 1], test_forest) == 1):
        print("North tests passed")
else:
    print("East tests failed")
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

if (find_viewing_distance_south([4, 4], test_forest) == 0 and
    find_viewing_distance_south([3, 4], test_forest) == 1):
        print("South tests passed")
else:
    print("South tests failed")

#%%
tree_of_interest = [3, 2]
north_vd = find_viewing_distance_north(tree_of_interest, test_forest)
south_vd = find_viewing_distance_south(tree_of_interest, test_forest)
east_vd = find_viewing_distance_east(tree_of_interest, test_forest)
west_vd = find_viewing_distance_west(tree_of_interest, test_forest)
scenic_score = north_vd * south_vd * east_vd * west_vd

print(f"North distance: {north_vd}")
print(f"South distance: {south_vd}")
print(f"East distance: {east_vd}")
print(f"West distance: {west_vd}")
print()
print(f"Scenic score: {scenic_score}")

#%%
def get_scenic_score(tree_coordinates, forest):
    north_vd = find_viewing_distance_north(tree_of_interest, test_forest)
    south_vd = find_viewing_distance_south(tree_of_interest, test_forest)
    east_vd = find_viewing_distance_east(tree_of_interest, test_forest)
    west_vd = find_viewing_distance_west(tree_of_interest, test_forest)
    scenic_score = north_vd * south_vd * east_vd * west_vd
    return scenic_score

#%%
max_scenic_score = 0
for row_index in range(forest_height):
    for col_index in range(forest_width):
        if get_scenic_score([row_index, col_index], forest) > max_scenic_score:
            max_scenic_score = get_scenic_score([row_index, col_index], forest)
print(f"Max scenic score: {max_scenic_score}")