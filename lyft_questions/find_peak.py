"""
find_peak is function that uses binary search to find the index of a
peak element in O(log n) time complexity
"""
def find_peak(nums):
    first = 0
    last = len(nums)-1

    if nums == []:
        return None
    if len(nums) == 1:
        return 0 # list with index of peak
    # Lets use an iterative approach with binary search
    while first < last:
        mid = (first + last) // 2
        # when we've reached a peak greater than number
        if nums[mid] > nums[mid + 1]:
            last = mid
        # climbing the peak
        if nums[mid] < nums[mid+1]:
            # we need to move the goal post
            first = mid + 1
    return last

print(find_peak([1, 2, 4, 5, 4, 2, 5, 2, 1]))
