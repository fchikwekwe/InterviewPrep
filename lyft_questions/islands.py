"""				Lyft Interview Question : Islands

Given a Multidimensional array, return the number of island clusters where land
is represented by 1 and water by 0. A cluster of islands is defined by a 1 or
pack of one enclosed by 0’s left and right, NOT diagonally.

Example:

0110
0100   => 3 because we have 3 packs of 1’s
1000
0011

Note from interviewer: You don’t have to optimize for time and space now,
but after one working solution, try to be as optimal as possible.

Input => 2d array/list
Output => number
"""

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

print(
    find_islands(
        [
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 1]
        ]
    )
)
