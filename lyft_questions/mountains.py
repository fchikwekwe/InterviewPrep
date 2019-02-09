"""
find_peak is function that uses binary search to find the index of a
peak element in O(log n) time complexity
"""
def find_peak(nums):
    left = 0
    right = len(nums)-1
    peaks = []

    # What if the list is empty?
    if nums == []:
        return []
    # What if the list has only one item?
    if len(nums) == 1:
        return [0] # list with index of peak
    # Lets use an iterative approach with binary search
    while left < right - 1:
        mid = (left + right) // 2
        # when we've reached a peak greater than number
        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            peaks.append(mid)
        # climbing the peak
        if nums[mid] < nums[mid+1]:
            # we need to move the goal post
            left = mid + 1
            # descending the peak
        else:
            right = mid - 1
    return peaks
# test function
arr = [2] # output = index 2, 6
print(find_peak(arr))
