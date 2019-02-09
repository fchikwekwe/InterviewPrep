input_list = [1, 5, 3, 0, 1, 4, 8, 10, 2]

def find_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for num in nums:
        if nums[abs(num)-1] < 0:
            res.append(abs(num))
        else:
            nums[abs(num)-1] *= -1
    return res

find_duplicates(input_list)
