def get_coordinate_sum(numbers):
    # Calculate the sum of the 1000th, 2000th and 3000th numbers.
    coordinates = list(range(3))
    index_of_0 = numbers.index(0)
    coordinates[0] = numbers[(index_of_0 + 1000) % len(numbers)]
    coordinates[1] = numbers[(index_of_0 + 2000) % len(numbers)]
    coordinates[2] = numbers[(index_of_0 + 3000) % len(numbers)]
    return sum(coordinates)
    
def move_number(number_to_move, current_index, numbers):
    new_numbers = ['_' for _ in range(len(numbers))]
    new_index = (current_index + number_to_move)
    if new_index >= 0:
        new_index = new_index % len(numbers)
    elif new_index < 0:
        new_index = (len(numbers) - 1 + new_index) % len(numbers)
        if new_index == len(numbers) - 1:
            new_index = 0
    if new_index == current_index: # Easy!
        new_numbers = numbers
    elif new_index > current_index:
        new_numbers[:current_index] = numbers[:current_index]
        new_numbers[current_index:new_index] = \
            numbers[current_index + 1: new_index + 1]
        new_numbers[new_index] = numbers[current_index]
        new_numbers[new_index + 1:] = numbers[new_index + 1:]
    elif new_index < current_index:
        new_numbers[:new_index] = numbers[:new_index]
        new_numbers[new_index] = numbers[current_index]
        new_numbers[new_index + 1:current_index + 1] = \
            numbers[new_index:current_index]
        new_numbers[current_index + 1:] = numbers[current_index + 1:]
    return new_numbers
    
def parse_input(filename):
    with open(filename) as file:
        lines = file.readlines()
    numbers = [int(line) for line in lines]
    return numbers
        
def main(filename):
    original_numbers = parse_input(filename)
    
    length = len(original_numbers)
    numbers = [number for number in original_numbers]
    indexes = range(length)
    
    for original_index in range(length):
        current_number = original_numbers[original_index]
        current_index = indexes.index(original_index)
        numbers = move_number(current_number,
                              current_index,
                              numbers)
        
        indexes = move_number(current_number,
                              current_index,
                              indexes)
    
    coordinate_sum = get_coordinate_sum(numbers)
    return coordinate_sum

if __name__ == "__main__":
    result = main("../input.txt")
    print(f"Result: {result}")
        
    