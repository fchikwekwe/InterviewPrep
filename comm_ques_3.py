def three_product(nums):
    """
    nums: type list
    """

    three = []

    for num in nums:
        if len(three) == 0:
            three.append(num)
            continue # next number
        if len(three) < 3:
            for i, val in enumerate(three):
                if num >= val:
                    three.insert(i+1, num)
                    break
            continue # next number

        for i, val in enumerate(three):
            if num >= val:
                three[i] = num # replace val
                break

    product = 1
    for val in three:
        product *= val

    return product

if __name__ == "__main__":
    list_1 = [1, 5, 3, 2, 7, 0]
    print(three_product(list_1))
