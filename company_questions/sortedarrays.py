"""
Return the common elements between the two lists without using any additinal data structures.
"""
input1 = [-1, 0, 1, 5, 7, 9]
input2 = [1, 2, 2, 5, 7, 7, 8, 11]

# check to see if either list is empty
## if it is, then return an empty array
# take the first two values in both arrays and compare them to one another
# if the values are equal to one another, then return that value
# whichever value is higher, increment the lower one and then compare again
# edge case of if the next value is also a duplicate

def return_duplicates(list1, list2):
    # store the duplicate values
    duplicates = []
    # check edge case of either list being empty
    if list1 == [] or list2 == []:
        return []
    # keep track of the indices that you will increment
    index1 = 0
    index2 = 0
    # keep iterating until the end of either array
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            index1 += 1
        elif list1[index1] > list2[index2]:
            index2 += 1
        else:
            # if the values are equal, you've found a duplicate
            duplicates.append(list1[index1])
            index1 += 1
            index2 += 1
    return duplicates

print(return_duplicates(input1, input2))
