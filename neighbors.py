
def check_neighbors(this_list, super_index, sub_index):
    # neighbors = []
    if this_list[super_index][sub_index - 1]:
        if this_list[super_index][sub_index - 1] == 0:
            return True
    if this_list[super_index][sub_index + 1]:
        if this_list[super_index][sub_index + 1] == 0:
            return True
    if this_list[super_index - 1][sub_index]:
        if this_list[super_index - 1][sub_index] == 0:
            return True
    if this_list[super_index + 1][sub_index]:
        if this_list[super_index + 1][sub_index] == 0:
            return True
    return False

def width_height(this_list, super_index, sub_index):
    width = 1
    height = 1
    # Base case when the are no new adjacent zeros
    # List variables that will be passed to recursive call
    # Recursively call function



    # if this_list[super_index][sub_index - 1]:
    #     if this_list[super_index][sub_index - 1] == 0:
    #         width += 1
    # if this_list[super_index][sub_index + 1]:
    #     if this_list[super_index][sub_index + 1] == 0:
    #         width += 1


def find_islands(this_list):
    for inner_list in this_list:
        for num in inner_list:
            if num == 0:
                if check_neighbors(this_list, this_list.index(inner_list), inner_list.index(num)):
                    print("Its true")
                    return list(this_list.index(island_list), island_list.index(num))
