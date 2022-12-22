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

def test_one():
    number_to_move = -3
    current_index = 1
    input_numbers = [1, -3, 2, 3, -2, 0, 4]
    expected_output = [1, 2, 3, -2, -3, 0, 4]
    #expected_new_index = 4
    actual_output = move_number(number_to_move, current_index, input_numbers)
    assert actual_output == expected_output

def test_two():
    number_to_move = -4
    current_index = 1
    input_numbers = [12, -4, 3]
    expected_output = [-4, 12, 3]
    actual_output = move_number(number_to_move, current_index, input_numbers)
    assert actual_output == expected_output