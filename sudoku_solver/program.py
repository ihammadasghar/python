from math import sqrt

BOARD = [[1, 6, 4, 0, 0, 0, 0, 0, 2],
                    [2, 0, 0, 4, 0, 3, 9, 1, 0],
                    [0, 0, 5, 0, 8, 0, 4, 0, 7],
                    [0, 9, 0, 0, 0, 6, 5, 0, 0],
                    [5, 0, 0, 1, 0, 2, 0, 0, 8],
                    [0, 0, 8, 9, 0, 0, 0, 3, 0],
                    [8, 0, 9, 0, 4, 0, 2, 0, 0],
                    [0, 7, 3, 5, 0, 9, 0, 0, 1],
                    [4, 0, 0, 0, 0, 0, 6, 7, 9]]


def solve(board):
    solved = True

    #  Go through each cell
    for row in range(len(board)):
        for col in range(len(board[row])):
            #  If the cell is not calculated
            if board[row][col] == 0 or type(board[row][col]) is list:
                #  Narrow possible values for the cell
                possibilities = narrow_possibilites(board, row, col)

                #  If there is only one possibilty assign it to the cell
                if len(possibilities) == 1:
                    board[row][col] = possibilities[0]
                else:
                    solved=False
                    board[row][col] = possibilities
    #  Check if all cells are solved
    if not solved:
        solve(board)
    return board

def narrow_possibilites(board, row, col):
    possibilities = [n+1 for n in range(9)]
    #  Row search
    #  Check the row
    for i in range(len(board[row])):
        cell = board[row][i]
        if cell in possibilities:
            possibilities.remove(cell)

    #  Column Search
    #  Check ahead of cell in the column
    for i in range(len(board)):
        cell = board[i][col]
        if cell in possibilities:
            possibilities.remove(cell)
   
    #  3x3 Block search
    DIM = int(sqrt(len(board)))
    cords = (((row) - ((row) % DIM)) , ( (col) - ((col)%DIM)) )  #  Cords of the first cell of the block that the cell belongs to

    for i in range(DIM):
        for j in range(DIM):
            cell = board[cords[0]+i][cords[1]+j]
            if cell in possibilities:
                possibilities.remove(cell)

    return possibilities

for e in solve(BOARD):
    print(e)



                


