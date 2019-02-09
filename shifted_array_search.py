def shifted_arr_search(shiftArr, num):
    counter = 0
    new_list = []
    for i in range(len(shiftArr)):
        counter += 1
        if shiftArr[i] > shiftArr[i+1]:
            greater = shiftArr[:i+1]
            less = shiftArr[i+1:]
            new_list.extend(less)
            new_list.extend(greater)
            print(new_list)
            break
    num_index = binary_search(new_list, num)
    num_index = num_index + counter
    return num_index

def binary_search(new_list, num):
    first = 0
    last = len(new_list) - 1

    while last >= first:
        midpoint = first + last // 2
        print("new_list {}, midpoint {}".format(new_list, midpoint))
        if new_list[midpoint] == num:
            print(midpoint)
            return midpoint
        if new_list[midpoint] > num:
            last = midpoint - 1
        else:
            first = midpoint + 1

print(shifted_arr_search([9, 12, 17, 19, 22, 2, 4, 5], 2))

# counter = 0 # keep track of how many spaces ive traveled
# list = [3, 4, 1, 2]
# new_list [1, 2, 3, 4]
# return value index

# iterate and find when the next calue is less than
# slice the array and concatenate the first half with the second half of the new slice
# binary search on the second array
# subtract the index to the counter
