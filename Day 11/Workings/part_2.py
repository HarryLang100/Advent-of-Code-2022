from part_1 import parse_input
from part_1 import get_monkey_business_level

def update_worry_level_2(worry_level, instruction, prod_divisibility_numbers):

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

    # Now decrease the worry level by doing
    # worry level MOD prod_divisibility_numbers
    new_worry_level = new_worry_level % prod_divisibility_numbers
    
    # 
    return new_worry_level

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

def monkey_turn(monkey_index, monkey_information):
    items_to_inspect = list(monkey_information[monkey_index][0])
    n_items_to_inspect = len(monkey_information[monkey_index][0])
    divisibility_numbers = [monkey[2] for monkey in monkey_information]
    divisibility_numbers_prod = 1
    for num in divisibility_numbers:
        divisibility_numbers_prod = divisibility_numbers_prod * num
    for item in items_to_inspect:
        current_worry_level = item
        instruction = monkey_information[monkey_index][1]
        new_worry_level = update_worry_level_2(current_worry_level,
                                             instruction,
                                             divisibility_numbers_prod)
        test_division_num = monkey_information[monkey_index][2]
        if new_worry_level % test_division_num == 0:
            to_monkey = monkey_information[monkey_index][3]
            monkey_information[to_monkey][0].append(new_worry_level)
        else:
            to_monkey = monkey_information[monkey_index][4]
            monkey_information[to_monkey][0].append(new_worry_level)
    monkey_information[monkey_index][0] = []
    return monkey_information, n_items_to_inspect

#%%
result = main("input.txt", 10000) 
print(f"Result: {result}.")
