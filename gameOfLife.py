
# working!

def gameOfLife(board):
    original = [[board[row][col] for col in range(len(board[0]))] for row in range(len(board))]

    for r, row in enumerate(board):
        for c in range(len(row)):
            # print("CURRENT CELL", board[r][c])
            num_neighbors = numAliveNeighbors(r, c, original)

            if original[r][c] == 1 and num_neighbors < 2:
                print("original", original, "new", board)
                board[r][c] = 0
            elif original[r][c] == 1 and num_neighbors == 2:
                print("original", original, "new", board)
                board[r][c] = 1
            elif original[r][c] == 1 and num_neighbors == 3:
                print("original", original, "new", board)
                board[r][c] = 1
            elif original[r][c] == 1 and num_neighbors > 2:
                print("original", original, "new", board)
                board[r][c] = 0
            elif original[r][c] == 0 and num_neighbors == 3:
                print("original", original, "new", board)
                board[r][c] = 1
    return board

def numAliveNeighbors(r, c, board):
    # make sure to exclude current cell
    neighbors = [[-1, -1], [0, -1], [1, -1],
                [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
    alive = 0

    for neighbor in neighbors:
        row_pos = neighbor[0] + r
        col_pos = neighbor[1] + c
        print(r, c, row_pos, col_pos)
        if row_pos >= 0 and row_pos < len(board) and col_pos >= 0 and col_pos < len(board[0]):
            if board[row_pos][col_pos] == 1:
                alive += 1

    # print("Num alive neighbors", alive)
    return alive


if __name__ in "__main__":
    print(gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
    # expected output
    # [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
