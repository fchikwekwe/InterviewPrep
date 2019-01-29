""" Interview prep questions given by Github@RinniSwift """

def return_product(number_list):
    """question 1) given an array of Int, return the largest product of 3 integers"""

    largest = 0
    second = 0
    third = 0
    # iterate over the list
    for num in number_list:
        # store the largest, second and third values
        if num > largest:
            # reassign all values
            third = second
            second = largest
            largest = num
        elif largest > num > second:
            third = second
            second = num
        elif second > num > third:
            third = num
    print("""Largest: {},
    second: {},
    third: {},
    product {}""".format(largest, second, third, largest*second*third))
    # multiply those numbers; return product
    return largest * second * third


"""question 2) calculate the indexes of the ocean view apartments
             E.g: Input [4, 4, 2, 3, 1] Output [1, 3, 4]
              ___   ___
              |  |  |  |        ___
              |  |  |  |  ___   |  |
              |  |  |  |  |  |  |  |  ___
              |  |  |  |  |  |  |  |  |  |
                                         ~~~~~~"""
def apartment_index():
    """question 2) calculate the indexes of the ocean view apartments"""
    pass


def return_bool(item_list, item):
    """question 3) create a binary search on a sorted array and returns a bool"""
    # initilize first and last value
    first = 0
    last = len(item_list)-1
    # initalize found condition
    found = False
    # make sure that first remains less than last
    while first <= last and not found:
        # search for value at midpoint
        midpoint = (first + last)//2
        print("current midpoint: ", item_list[midpoint])
        # if midpoint value is item, we are done
        if item_list[midpoint] == item:
            found = True
        # if midpoint value is greater than item, search first half
        else:
            if item_list[midpoint] > item:
                last = midpoint - 1
                print("last: ", last)
            # if midpoint value is less than item, search second half
            else:
                if item_list[midpoint] < item:
                    first = midpoint + 1
                    print("first: ", first)

    print("found", found)
    return found

def return_output(number_list):
    """question 4) given an array, numbers, of N integers, return an array output
    such that output[i] is equal to the product  of all integers except numbers[i]"""
    # for each index in range, return
    pass

def factorial_recursive():
    """question 5) create a factorial recurssive function
    that returns an Int (e.g. factorialRecurssive(num: 5) returns 120 (5*4*3*2*1)"""
    pass

def unique_char():
    """question 6) check if a word has all unique characters. returns Boolean of the unique word."""
    pass


if __name__ in "__main__":
    NUMBERS = [1, 50, 4, 31, 108, 15, 7]
    return_product(NUMBERS)
    SORTED_NUMBERS = [1, 4, 6, 10, 18, 22, 35, 49, 51, 72, 80, 101, 203]
    return_bool(SORTED_NUMBERS, 18)
    PRODUCT_NUMBERS = [2, 4, 5, 10]
