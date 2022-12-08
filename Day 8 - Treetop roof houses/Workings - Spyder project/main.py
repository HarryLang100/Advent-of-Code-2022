# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:13:14 2022

@author: Harry Lang
"""

# tree_coordinates[row, column]

#%%
def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    forest = [[] for i in range(len(lines))]
    for line_index, line in enumerate(lines):
        forest[line_index] = [int(letter) for letter in line]
    return forest

#%%
def check_tree_visible(tree_coordinates, forest):
    forest_height = len(forest)
    forest_width = len(forest[0])
    
    
    tree_height = forest[tree_coordinates[0]][tree_coordinates[1]]
    
    tree_visible_from_west = True
    for col_index in range(tree_coordinates[1]):
        current_tree_height = forest[tree_coordinates[0]][col_index]
        # print("Checking from West")
        # print(f"Current tree coordinates: {tree_coordinates[0], col_index}")
        # print(f"Current tree height: {current_tree_height}")
        if current_tree_height >= tree_height:
            tree_visible_from_west = False
    # print(f"Visible from West? {tree_visible_from_west}")
    
    tree_visible_from_east = True
    for col_index in range(tree_coordinates[1] + 1, forest_width):
        current_tree_height = forest[tree_coordinates[0]][col_index]
        if current_tree_height >= tree_height:
            tree_visible_from_east = False
    
    tree_visible_from_north = True
    for row_index in range(tree_coordinates[0]):
        current_tree_height = forest[row_index][tree_coordinates[1]]
        if current_tree_height >= tree_height:
            tree_visible_from_north = False
    
    tree_visible_from_south = True
    for row_index in range(tree_coordinates[0] + 1, forest_height):
        current_tree_height = forest[row_index][tree_coordinates[1]]
        if current_tree_height >= tree_height:
            tree_visible_from_south = False
    
    tree_visible = (tree_visible_from_west or
                    tree_visible_from_east or
                    tree_visible_from_north or
                    tree_visible_from_south)                    
        
    print(f"Tree at {tree_coordinates} is visible? {tree_visible}")
        
    return (tree_visible_from_west or
            tree_visible_from_east or
            tree_visible_from_north or
            tree_visible_from_south)


def count_visible_trees(forest):
    visible_count = 0
    forest_height = len(forest)
    forest_width = len(forest[0])
    
    for row_index in range(forest_height):
        for col_index in range(forest_width):
            if check_tree_visible([row_index, col_index], forest):
                visible_count += 1
            else: # Tree not visible.
                pass
    return visible_count
#%%
filename = "input.txt"
forest = parse_input(filename)
number_visible_trees = count_visible_trees(forest)
print(f"The number of visible trees is {number_visible_trees}")