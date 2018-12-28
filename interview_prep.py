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


def return_bool():
    """question 3) create a binary search on a sorted array and returns a bool"""
    pass

if __name__ in "__main__":
    NUMBERS = [1, 50, 4, 31, 108, 15, 7]
    return_product(NUMBERS)
