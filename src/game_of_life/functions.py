from datatypes import GameBoard

def count_rows(board: GameBoard) -> int:
    """
    Count the number of rows in a GameBoard.
    Args:
        board (GameBoard): A 2D list of booleans representing the game state.
    Returns:
        int: Number of rows in the board.
    """
    if not isinstance(board, list):
        raise ValueError("board must be a list.")
    assert_rectangular(board)  # Ensure the board is rectangular before counting columns

    return len(board)  # Return the number of rows in the board


def count_cols(board: GameBoard) -> int:
    """
    Count the number of columns in a GameBoard.
    Args:
        board (GameBoard): A 2D list of booleans representing the game state.
    Returns:
        int: Number of columns in the board.
    Raises:
        ValueError: If the board is not rectangular.
    """
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty 2D list.")
    
    assert_rectangular(board)  # Ensure the board is rectangular before counting columns

    return len(board[0])  # Return the number of columns in the first row


def assert_rectangular(board: GameBoard) -> None:
    """
    Ensure that a GameBoard is rectangular.
    Args:
        board (GameBoard): A 2D list of booleans representing the game state.
    Raises:
        ValueError: If the board has no rows or if its rows are not of equal length.
    """
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty 2D list.")
    
    row_length = len(board[0])  # Get the length of the first row to compare against
    for i, row in enumerate(board, start=1):
        if len(row) != row_length:
            raise ValueError(f"Row {i} has length {len(row)}, expected {row_length}.")

def play_game_of_life(initial_board: GameBoard, num_gens: int) -> list[GameBoard]:
    """
    Simulate Game of Life for a given number of generations.
    Args:
        initial_board (GameBoard): The starting game board.
        num_gens (int): The number of generations to simulate.
    Returns:
        list[GameBoard]: Boards from initial through num_gens generations.
    """
    if not isinstance(initial_board, list) or len(initial_board) == 0:
        raise ValueError("initial_board must be a non-empty GameBoard.")
    if not isinstance(num_gens, int) or num_gens < 0:
        raise ValueError("num_gens must be a non-negative integer.")
    
    if len(initial_board[0]) == 0:
        raise ValueError("No elements in first row.")
    
    assert_rectangular(initial_board)

    boards: list[GameBoard] = [initial_board]  # Start with the initial board
    for i in range(num_gens):
        # update the current board to get the next board, and add it to the list of boards
        # NOTE: we dont do the drawing here, we just compute the boards, and then we will draw them all at the end.
        # this modularity makes our program cleaner and easier to debug, because we can test the board updating logic separately from the drawing logic.
        # sometimes we may want to both simultaneously, but for now we will keep them separate.
        boards.append(update_board(boards[i]))
    
    return boards


def update_board(current_board: GameBoard) -> GameBoard:
    """
    Apply Game of Life rules for one generation.
    Args:
        current_board (GameBoard): The current game board.
    Returns:
        GameBoard: A new board representing the next generation.
    """
    if not isinstance(current_board, list) or len(current_board) == 0:
        raise ValueError("current_board must be a non-empty GameBoard.")
    
    num_rows = count_rows(current_board)
    num_cols = count_cols(current_board)
    next_board = initialize_board(num_rows, num_cols)  # Create a new board for the next generation

    # range over all the cells of the current board and get the updated values
    for r in range(num_rows):
        for c in range(num_cols):
            next_board[r][c] = update_cell(current_board, r, c)  # Update the cell and set it in the next board

    return next_board

def initialize_board(num_rows: int, num_cols: int) -> GameBoard:
    """
    Initialize a GameBoard with the given number of rows and columns.
    Args:
        num_rows (int): Number of rows.
        num_cols (int): Number of columns.
    Returns:
        GameBoard: A num_rows x num_cols board filled with False values.
    """
    if not isinstance(num_rows, int) or num_rows <= 0:
        raise ValueError("num_rows must be a positive integer.")
    if not isinstance(num_cols, int) or num_cols <= 0:
        raise ValueError("num_cols must be a positive integer.")
    
    board: GameBoard = []

    for _ in range(num_rows):
        row = [False] * num_cols
        board.append(row)

    return board


def update_cell(board: GameBoard, r: int, c: int) -> bool:
    """
    Determine the next state of the cell at (r, c).
    Args:
        board (GameBoard): The current game board.
        r (int): Row index.
        c (int): Column index.
    Returns:
        bool: True if alive next generation, False otherwise.
    """
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty GameBoard.")
    if not isinstance(r, int) or not isinstance(c, int):
        raise ValueError("r and c must be integers.")
    
    num_live_neighbors = count_live_neighbors(board, r, c)

    # branch into two cases: curent cell alive or dead
    if board[r][c]:
        # live case
        if num_live_neighbors == 2 or num_live_neighbors == 3:
            return True # remain alive
        else:
            return False # lack of maters or overpopulation
    else:
        # dead case
        if num_live_neighbors == 3:
            return True # zombie ritual!
        else:
            return False # stay dead

def count_live_neighbors(board: GameBoard, r: int, c: int) -> int:
    """
    Count live neighbors of board[r][c].
    Args:
        board (GameBoard): The current game board.
        r (int): Row index.
        c (int): Column index.
    Returns:
        int: Number of live neighbors.
    """
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty GameBoard.")

    count = 0
    for neighbor_r in range(r-1, r+2):
        for neighbor_c in range(c-1, c+2):

            # establish that the neighbor cell is in the board
            if in_field(board, neighbor_r, neighbor_c):
                # check if the neighbor is alive and that we arent lookin at the current cell we want  the neighbor count for
                if board[neighbor_r][neighbor_c] and ((r, c) != (neighbor_r, neighbor_c)):
                    count += 1

    # # we could let it overcount and then subtract one
    # if board[r][c]:
    #     count -= 1
    return count


def in_field(board: GameBoard, i: int, j: int) -> bool:
    """
    Check if the given (i, j) indices are within the board.
    Args:
        board (GameBoard): The current game board.
        i (int): Row index.
        j (int): Column index.
    Returns:
        bool: True if inside the board, False otherwise.
    """
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("board must be a non-empty GameBoard.")
    if not isinstance(i, int) or not isinstance(j, int):
        raise ValueError("i and j must be integers.")

    if i < 0 or i >= count_rows(board):
        return False
    
    if j < 0 or j >= count_cols(board):
        return False

    return True # we must have a valid index
