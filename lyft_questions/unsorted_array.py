def find_duplicates(nums):
    index = 0
    # iterate through the whole array
    while index < len(nums):
        print(nums)
        num = nums[index]
        if nums[num-1] != num:
            while nums[num - 1] != num:
                # swap
                cur = nums[num - 1]
                nums[num - 1] = num
                nums[index] = cur
                num = cur
            continue
        index += 1

    output = []
    for index in range(len(nums)):
        print(nums, output)
        num = nums[index]
        if nums[num - 1] == num and index != num - 1:
            output.append(num)

    return output

input_list = [4, 3, 2, 7, 8, 2, 3, 1]

find_duplicates(input_list)
