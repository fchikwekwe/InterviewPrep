"""
Given a matrix, return True if every zero is reachable from every other zero.
"""

# Input 1:
[
    [0, 0, 1],
    [1, 0, 0],
    [0, 0, 1]
] # Output: True
# Input 2:
[
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 1]
] # Output: False


[
[1, 0, 0, 1],
[1, 0, 0, 1],
[1, 1, 1, 1],
]

[
[0, 0, 1, 0],
[0, 0, 1, 1],
[1, 1, 0, 0]
]

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

print(
    find_path(
        [
            [0, 0, 0, 0],
            [0, 0, 1, 1],
            [1, 0, 0, 0]
        ]
    )
)
