# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:16:37 2022

@author: Harry Lang
"""

running_total_score = 0

def determine_round_score(opponent_choice, my_choice):
    if opponent_choice=='A' and my_choice == 'X':
        round_score = 4
    if opponent_choice=='A' and my_choice == 'Y':
        round_score = 8
    if opponent_choice=='A' and my_choice == 'Z':
        round_score = 3
    if opponent_choice=='B' and my_choice == 'X':
        round_score = 1
    if opponent_choice=='B' and my_choice == 'Y':
        round_score = 5
    if opponent_choice=='B' and my_choice == 'Z':
        round_score = 9
    if opponent_choice=='C' and my_choice == 'X':
        round_score = 7
    if opponent_choice=='C' and my_choice == 'Y':
        round_score = 2
    if opponent_choice=='C' and my_choice == 'Z':
        round_score = 6


    return round_score

with open("input.txt") as file:
    lines = file.readlines()
    breakpoint()
    for line in lines:
        running_total_score += determine_round_score(line[0], line[2])
    breakpoint()
print(running_total_score)
        
        
        
        
        
        
        
        