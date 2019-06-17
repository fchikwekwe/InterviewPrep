""" Leetcode answers """

# Jewels and Stones
def common_jewels():
    """ For every jewel, find out if it is also a stone """
    J = "abc"
    S = "aaAbb"
    output = 0
    for jewel in J:
        for stone in S:
            if jewel == stone:
                output += 1
    print("Output:", output)
    return output

common_jewels()

# Squares of a Sorted Array
nums = [-4, -1, 0, 3, 10]
def square_values(nums):
    """For an array of ints in non decreasing order, return an array of their
    squares, also in non-decreasing order"""
    squares = []
    for num in nums:
        squares.append(num*num)
    return squares
