import pdb

def compare_two_flat_lists(left_list, right_list):
    #left_len = len(left_list)
    right_len = len(right_list)
    result = False
    for index, left_integer in enumerate(left_list):
        if index >= right_len - 1: # Right list runs out of items first.
            break
        if left_integer < right_list[index]: # Left integer smaller than
        # corresponding right.
            result = True
            break
    return result

