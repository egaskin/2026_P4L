def main():
    print("2D tuples and lists in Python (arrays)")

    # how to think about multidimensional arrays?
    # 
    kernel = (
        (0.05, 0.20, 0.05),
        (0.20, 0.00, 0.20),
        (0.05, 0.20, 0.02)
    )

    kernel_3d = (kernel, kernel, kernel)

    kernel_4d = (kernel_3d, kernel_3d, kernel_3d)

    print(kernel)

    # we can access individual elements too (everything is zero-indexed)
    print(f"kernel[0][2] = {kernel[0][2]}") # row 0, col 2. the indexing has order like so kernel[row][col][height]
    print(f"kernel[1][1] = {kernel[1][1]}")

    print(f"kernel_3d[1][1][1] = {kernel_3d[1][1][1]}") # the "center" element in the cube, enclosed by all the faces i.e. 0
    print(f"kernel_3d[2][1][1] = {kernel_3d[2][1][1]}") # should be the bottom center value, i.e. 0
    print(f"kernel_3d[2][2][1] = {kernel_3d[2][2][1]}")

    # let's declare a list that is 7 rows by 4 cols
    print("GENERALLY, BAD PYTHON ARRAY INITIALIZATION")
    [0] * 4 # type: ignore # we know how to make a single row with 4 columns like this
    a = [[0] * 4] * 7 # this creates 7 copies of a reference to a 1D list
    print(f"a original: {a}")
    a[1][2] = 19
    print(f"a[1][2] is changed, AND SO IS EVERY INDEX 2 col value: {a}") 

    # proper multidimensional list declaration, v1 (for loop)
    a = []
    for _ in range(7):
        new_row = [0] * 4
        a.append(new_row)
    print(f"a before changing: {a}")
    a[0][0] = 42
    a[1][2] = 19
    a[6][3] = 100
    print(f"a after changing: {a}")

    # proper multidimensional list declaration, v2 (list comprehension)
    a = [[0] * 4 for _ in range(7)]
    print("Number of rows is", len(a))
    print("Number of cols is", len(a[0]))

    # we can have non rectangular lists too. here's a "triangular 2d list"
    num_rows = 4
    board = []
    for i in range(num_rows):
        board.append([False] * i)

    print(f"board = {board}")
    print(f"board[0] = {board[0]}")

    # let's add a false to every row
    for row in range(len(board)):
        board[row].append(False)
    print(f"after editing, board = {board}")
    print(f"after editing, board[0] = {board[0]}")

    print_board_v1(board)
    print_board_v2(board)

    # declare the R Pentamino with everything starting as False
    num_cols = 5
    num_rows = 5
    r_pentomino = [[False] * num_cols for _ in range(num_rows)]
    r_pentomino[1][2] = True
    r_pentomino[1][3] = True
    r_pentomino[2][2] = True
    r_pentomino[2][1] = True
    r_pentomino[3][2] = True
    print(f"\nr_pentomino:")
    print_board_v2(r_pentomino)


def print_board_v1(board: list[list[bool]]) -> None:
    """
    Prints a 2-D list of boolean values in a prettty fashion
    
    :param board: board to print
    :type board: list[list[bool]]
    """

    for r in range(len(board)):
        for c in range(len(board[r])):
            # print the row without the space
            print(board[r][c], end = " ")

        # print a new line at the end of row
        print("")

def print_board_v2(board: list[list[bool]]) -> None:
    for row in board:
        print_row(row)

def print_row(row: list[bool]):
    for cell in row:
        print_cell(cell)
    print() # print new line

def print_cell(cell: bool):
    if cell:
        print("❤️", end = " ")
    else:
        print("☠️", end = " ")

if __name__ == "__main__":
    main()