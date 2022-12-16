#from main import check_pair
from main import compare_two_flat_lists
# class TestCheckPair(object):
#     def test_check_pair_one(self):
#         left_side = [1, 1, 3, 1, 1]
#         right_side = [1, 1, 5, 1, 1]
#         expected_output = True
#         actual_output = check_pair(left_side, right_side)
#         assert actual_output == expected_output
    
#     def test_check_pair_two(self):
#         left_side = [[1],[2,3,4]]
#         right_side = [[1],4]
#         expected_output = True
#         actual_output = check_pair(left_side, right_side)
#         assert actual_output == expected_output

#     def test_check_pair_three(self):
#         left_side = [[8,7,6]]
#         right_side = [8,7,6]
#         expected_output = False
#         actual_output = check_pair(left_side, right_side)
#         assert actual_output == expected_output

#     def test_check_pair_four(self):
#         left_side = [[4,4],4,4]
#         right_side = [[4,4],4,4,4]
#         expected_output = True
#         actual_output = check_pair(left_side, right_side)
#         assert actual_output == expected_output

#     def test_check_pair_five(self):
#         left_side = [7,7,7,7]
#         right_side = [7,7,7]
#         expected_output = True
#         actual_output = check_pair(left_side, right_side)
#         assert actual_output == expected_output

#     def test_check_pair_six(self):
#         left_side = []
#         right_side = [3]
#         expected_output = False
#         actual_output = check_pair(left_side, right_side)
#         assert actual_output == expected_output
    
#     def test_check_pair_seven(self):
#         left_side = [[[]]]
#         right_side = [[]]
#         expected_output = False
#         actual_output = check_pair(left_side, right_side)
#         assert actual_output == expected_output

class TestCompareTwoFlatLists(object):
    def test_compare_two_lists_left_side_smaller(self):
        left_side = [1, 1, 3, 1, 1]
        right_side = [1, 1, 5, 1, 1]
        expected_output = True
        actual_output = compare_two_flat_lists(left_side, right_side)
        assert actual_output == expected_output
    
    def test_compare_two_lists_right_runs_out_first(self):
        left_side = [1, 2, 3, 4]
        right_side = [1, 2]
        expected_output = False
        actual_output = compare_two_flat_lists(left_side, right_side)
        assert actual_output == expected_output
        
    def test_compare_two_flat_lists_left_empty(self):
        left_side = []
        right_side = [3]
        expected_output = False
        actual_output = compare_two_flat_lists(left_side, right_side)
        assert actual_output == expected_output