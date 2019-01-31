"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal
to the product of all the elements of nums except nums[i].
Please solve it in O(n) and without division.
"""

## Pseudocode ##
# make an array to hold our answers
# iterate over the indices
# store values that are not the current index
# multiply those values together
# return that multiplied value

ints = [2, 4, 6, 8]

def all_else_product(array_of_ints):
    products = []
    for curr_index in range(len(array_of_ints)):
        will_multiply = []
        for index in range(len(array_of_ints)):
            # print("array of ints", array_of_ints)
            if index is not curr_index:
                will_multiply.append(array_of_ints[index])
                # print("will multiply", will_multiply)
        new_value = 1
        for value in will_multiply:
            # print("value", value)
            new_value *= value
            # print("new value", new_value)
        products.append(new_value)
    return products
print("v0", all_else_product(ints))

def all_else_product_opt(int_list):
    # keep track of the multiplied value
    product = 1
    # use this for range
    list_length = len(int_list)
    output = []
    for i in range(list_length):
        # product = 1 is fine to append because it doesn't change value
        output.append(product)
        product = product * int_list[i]
    # use a neutral number to multiply with
    product = 1
    # move backwards through the array in stepwise fashion
    for i in range(list_length -1, -1, -1):
        # the output list value at the current index is multiplied by the product
        output[i] = output[i] * product
        # the product is multiplied by the input list value at the current index
        product = product * int_list[i]
    return output

print("v1", all_else_product_opt(ints))
