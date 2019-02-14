| Solved? | Mastered? | Question |
|--------------------------------|
| [X] | [] | asteroid collision|
| [] | [] | find all peaks|
| [X] | [X] | implement a stack|
| [X] | [X] | islands|
| [X] | [] | find the path|
| [X] | [X] | return dups from two sorted arrays|
| [X] | [] | return dups from one unsorted array|
| [X] | [X] | return products all except self |

- asteroid collision

def asteroidCollision(asteroids):
    res = []
    for asteroid in asteroids:
        if len(res) == 0 or asteroid > 0:
            res.append(asteroid)
        elif asteroid < 0:
            # While top of the stack is positive.
            while len(res) and res[-1] > 0:
                # Both asteroids are equal, destroy both.
                if res[-1] == -asteroid:
                    res.pop()
                    break
                # Stack top is smaller, remove the +ve asteroid
                # from the stack and continue the comparison.
                elif res[-1] < -asteroid:
                    res.pop()
                    continue
                # Stack top is larger, -ve asteroid is destroyed.
                elif res[-1] > -asteroid:
                    break
            else:
                # -ve asteroid made it all the way to the
                # bottom of the stack and destroyed all asteroids.
                res.append(asteroid)
    return res

- Find A Peak

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

- Find All Peaks
# iterate through the list
# compare the left and right values


- Implement a Stack

class Stack:
    def __init__(self):
        self.items = []
        self.max = []

    def is_empty(self):
        if self.items == []:
            return True
        return False

    def pop(self):
        if self.is_empty:
            raise IndexError
        else:
            if self.items[-1] == self.max[-1]:
                self.max.pop()
                return self.items.pop()
            else:
                return self.items.pop()

    def push(self, new_item):
        if self.max == []: # check if max list is empty
            self.max.append(new_item)
            self.items.append(new_item)
        else:
            if new_item >= self.max[-1]: # checks if new item is greater or equal to top item in max
                self.max.append(new_item)
                self.items.append(new_item)
            else:
                self.items.append(new_item)

    def max(self):
        if self.max == []:
            return None
        return self.max[-1]

- Find all the islands

def find_islands(matrix):
    """
    Main function that keeps track of our have times we find a new island
    in the matrix.
    """
    new_one = 0 # keep track of every new zero we see

    # iterate over the 2D array
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # check to see if we have found a one
            if matrix[i][j] == 1:
                # adjust the new one counter
                new_one += 1
                check_neighbors(matrix, i, j) # helper function to check for adjacent zero
    return new_one

def check_neighbors(matrix, i, j):
    """
    Recursive function that check all adjacent cells everytime it finds a
    neighbor.
    """
    if i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[0]):
        if matrix[i][j] == 1:
            print("matrix", matrix)
            # change it to a different number so that it doesnt keep getting rechecked
            matrix[i][j] = 2
            check_neighbors(matrix, i + 1, j)
            check_neighbors(matrix, i - 1, j)
            check_neighbors(matrix, i, j + 1)
            check_neighbors(matrix, i, j - 1)

- Find the path

def find_path(matrix):
    """
    Input: 2d array.
    Output: boolean
    """
    new_zero = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                check_neighbors(matrix, i, j)
                print("main", matrix)
                new_zero += 1

    if new_zero == 1:
        return True
    return False

def check_neighbors(matrix, i, j):
    """ Check to see if any adjacent neighbors are zeros """
    if i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[0]):
        if matrix[i][j] == 0:
            print("helper", matrix)
            matrix[i][j] = 2
            check_neighbors(matrix, i - 1, j)
            check_neighbors(matrix, i + 1, j)
            check_neighbors(matrix, i, j - 1)
            check_neighbors(matrix, i, j + 1)

- Return duplicates from sorted arrays (no other data structures)
def find_duplicate(nums1, nums2):
    duplicates = [] # store the duplicates and return them at the end

    index1 = 0
    index2 = 0

    if nums1 == [] or nums2 == []:
        return []

    while index1 < len(nums1) and index2 < len(num2):
        if nums1[index1] == nums2[index2]:
            duplicates.append(nums1[index1])
            index1 += 1
            index2 += 1
        elif nums1[index1] > nums2[index2]:
            index2 += 1
        else: num2[index2] < nums1[index1]:
            index1 += 1
    return duplicates

- Return duplicates from unsorted array
input = [1, 5, 3, 0, 1, 4, 8, 10, 2]

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
            nums[abs(num)-1] * = -1
    return output

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
