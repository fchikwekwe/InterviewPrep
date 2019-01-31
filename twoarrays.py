"""
Find common elements within 2 integer arrays in O(N) time  and O(1) space.
"""

def intersection(nums1, nums2):
    """
    This solution is O(n) space and O(n) time complexities.
    """
    print("nums1 set {}, nums2 set {}".format(set(nums1), set(nums2)))
    return list(set(nums1) & set(nums2))

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1, nums2))
