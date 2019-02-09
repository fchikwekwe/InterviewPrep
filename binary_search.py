"""
Implementing binary search function to look for an integer in a sorted list.
"""

int_list = [171]
current_int = 170

def binary_search(input_list, num):
    """
    Arguments:
    input_list == sorted list of ints
    num == target integer
    """
    if len(input_list) == 0:
        return False
    if len(input_list) == 1:
        if num == input_list[0]:
            return True
        return False

    midpoint = len(input_list) // 2

    if input_list[midpoint] == num:
        return True
    elif input_list[midpoint] > num:
        return binary_search(input_list[:midpoint], num)
    else:
        return binary_search(input_list[midpoint:], num)

print(binary_search(int_list, current_int))
