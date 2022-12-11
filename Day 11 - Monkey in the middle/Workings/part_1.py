def parse_input(filename):
    # For each monkey, make a list of format
    # starting_items, operation, test_division_num, if_false, if_true
    with open(filename) as file:
        lines = file.read().splitlines()
    n_monkeys = int((len(lines) + 1)/7)
    monkey_information = [None for index in range(n_monkeys)]
    
    # Add monkey info for each monkey.
    for line_index in range(0, len(lines), 7):
        
        # Get starting items as list of integers.
        starting_items = lines[line_index + 1].lstrip().replace(",", "").split(" ")[2:]
        starting_items = [int(item) for item in starting_items]
        
        # Get operation as list of strings.
        operation = lines[line_index + 2].split(" ")[-3:]
        
        
        # Get test_division_num as integer.
        test_division_num = int(lines[line_index + 3].split(" ")[-1])
        
        # Get if_true as integer.
        if_true = int(lines[line_index + 4].split(" ")[-1])
        
        # Get if_false as integer.
        if_false = int(lines[line_index + 5].split(" ")[-1])

        # Add information to list.
        monkey_information[int(line_index/7)] = [
            starting_items, operation, test_division_num, if_true, if_false]
    #
    return monkey_information

def update_worry_level(worry_level, instruction):

    # Understand what operation to perform.
    operation = instruction[1]
    message = f"Invalid operation: {operation}. (Should be either '+' or '*'.)"
    assert operation in ["+", "*"], message
    
    # Determine numbers to operate on.
    numbers_to_operate_on = [None, None]
    if instruction[0] == "old":
        numbers_to_operate_on[0] = int(worry_level)
    elif instruction[0].isnumeric():
        numbers_to_operate_on = int(instruction[0])
    if instruction[2] == "old":
        numbers_to_operate_on[1] = int(worry_level)
    elif instruction[2].isnumeric():
        numbers_to_operate_on[1] = int(instruction[2])
    
    # Perform the operation
    if operation == "+":
        new_worry_level = numbers_to_operate_on[0] + numbers_to_operate_on[1]
    elif operation == "*":
        new_worry_level = numbers_to_operate_on[0] * numbers_to_operate_on[1]

    # Now decrease the worry level (divide by 3 and round down).
    new_worry_level = int(new_worry_level//3)
    
    # 
    return new_worry_level

    
def monkey_turn(monkey_index, monkey_information):
    items_to_inspect = list(monkey_information[monkey_index][0])
    n_items_to_inspect = len(monkey_information[monkey_index][0])
    for item in items_to_inspect:
        current_worry_level = item
        instruction = monkey_information[monkey_index][1]
        new_worry_level = update_worry_level(current_worry_level,
                                             instruction)
        test_division_num = monkey_information[monkey_index][2]
        if new_worry_level % test_division_num == 0:
            to_monkey = monkey_information[monkey_index][3]
            monkey_information[to_monkey][0].append(new_worry_level)
        else:
            to_monkey = monkey_information[monkey_index][4]
            monkey_information[to_monkey][0].append(new_worry_level)
    monkey_information[monkey_index][0] = []
    return monkey_information, n_items_to_inspect
    
def get_monkey_business_level(inspection_count):
    inspection_count.sort(reverse=True)
    return inspection_count[0] * inspection_count[1]
    
def main(filename, n_rounds):
    monkey_information = parse_input(filename)
    n_monkeys = len(monkey_information)
    inspection_count = [0 for index in monkey_information]
    for round_index in range(n_rounds):
        for monkey_index in range(n_monkeys):
            monkey_information, n_items_inspected = monkey_turn(
                monkey_index,
                monkey_information)
            inspection_count[monkey_index] += n_items_inspected
    return get_monkey_business_level(inspection_count)

#%%
result = main("input.txt", 20)
print(f"Result: {result}.")
