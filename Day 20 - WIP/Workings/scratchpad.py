from main import move_number
from main import parse_input

original_numbers = parse_input("../example_input.txt")

length = len(original_numbers)
numbers = [number for number in original_numbers]
indexes = range(length)

for original_index in range(length):
    current_number = original_numbers[original_index]
    current_index = indexes.index(original_index)
    print(f"Current numbers: {numbers}")
    print(f"Number to move: {current_number}")
    print(f"Index of current number: {current_index}")
    print()
    numbers = move_number(current_number,
                          current_index,
                          numbers)
    
    indexes = move_number(current_number,
                          current_index,
                          indexes)
