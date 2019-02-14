numbers = [4, 3, 2, 7, 8, 2, 3, 1]

def find_duplicates_no_negatives(nums):
    """
    Assuming that there can be no negatives or zeros.
    """
    output = []
    for num in nums:
        # Numbers should only be negative if you've flagged them
        # Use absolute value since it might have been marked negative already
        if nums[abs(num)-1] < 0:
            output.append(abs(num))
        # Flag the value so that you know its duplicated if you see it again
        else:
            nums[abs(num)-1] *= -1
    return output

print(find_duplicates_no_negatives(numbers))

def find_duplicates(nums):
    """
    Time complexity: O(n), iterates twice, but not nested
    Space complexity: O(1), only uses space for output
    """
    i = 0
    # iterate through the whole array
    for i in range(len(nums)):
        print(nums)
        if nums[i] != nums[nums[i] - 1]:
            # swap elements to their expected place in the list
            # expected place = index value offset by one
            # only duplicates wont be at their expected spots
            nums[nums[i] -1], nums[i] = nums[i], nums[nums[i] -1]

    duplicates = []
    for i in range(len(nums)):
        print(nums, duplicates)
        if nums[nums[i] - 1] == nums[i] and i != nums[i] - 1:
            duplicates.append(nums[i])

    return duplicates

input_list = [4, 3, 2, 7, 8, 10, 11, 3, 11]

print("other method", find_duplicates(input_list))

def hash_duplicates(nums):
    """
    Time complexity: O(n), iterates twice, but not nested
    Space complexity: O(m), the size of the dictionary
    """
    duplicates = []
    hash_table = {}

    for num in nums:
        try:
            hash_table[num] += 1
        except:
            hash_table[num] = 1
    for item in hash_table:
        print(hash_table)
        if hash_table[item] > 1:
            duplicates.append(item)
    return duplicates

print("hash method", hash_duplicates(input_list))
