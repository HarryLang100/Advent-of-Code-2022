# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:54:29 2022

@author: Harry Lang
"""

def make_choice(opponent_choice_letter, requirement_letter):
    if opponent_choice_letter == 'A' and requirement_letter == 'X':
        my_choice = 'Z'
    if opponent_choice_letter == 'A' and requirement_letter == 'Y': 
        my_choice = 'X'
    if opponent_choice_letter == 'A' and requirement_letter == 'Z': 
        my_choice = 'Y'
    if opponent_choice_letter == 'B' and requirement_letter == 'X': 
        my_choice = 'X'
    if opponent_choice_letter == 'B'and requirement_letter == 'Y': 
        my_choice = 'Y'
    if opponent_choice_letter == 'B' and requirement_letter == 'Z': 
        my_choice = 'Z'
    if opponent_choice_letter == 'C' and requirement_letter == 'X': 
        my_choice = 'Y'
    if opponent_choice_letter == 'C' and requirement_letter == 'Y': 
        my_choice = 'Z'
    if opponent_choice_letter == 'C' and requirement_letter == 'Z': 
        my_choice = 'X'
    return my_choice

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
        
running_total = 0 
with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        my_choice = make_choice(line[0], line[2])
        running_total += determine_round_score(line[0], my_choice)
print(running_total)