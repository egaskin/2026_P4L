from datatypes import GameBoard
from functions import assert_rectangular


def read_board_from_file(filename: str) -> GameBoard:
    """
    Reads a CSV file representing a Game of Life board.
    "1" = alive (True), "0" = dead (False).
    Args:
        filename (str): The name of the CSV file.
    Returns:
        GameBoard: Parsed board.
    """
    if not isinstance(filename, str) or len(filename) == 0:
        raise ValueError("filename must be a non-empty string.")

    # with means close the file at the end of the code block, even if an error occurs
    with open(filename, 'r') as f:
        giant_string = f.read()

    # first trim any whitespace from the start and end of the file
    giant_string = giant_string.strip()

    # split the file into lines
    lines = giant_string.split('\n')

    # raise errorr if there are no lines
    if len(lines) == 0:
        raise ValueError("The file must contain at least one line.")
    
    # range over lines and trim whitespace from each line, and check if any line is empty after trimming
    for i, _ in enumerate(lines):
        lines[i] = lines[i].strip()  # trim whitespace from the line
        if len(lines[i]) == 0:
            raise ValueError("Lines cannot be empty.")

    # range over lines and parse each one into a list of booleans
    board: GameBoard = []
    for line in lines:
        line_elements = line.split(',')  # split the line into elements by comma
        
        row_values = set_row_values(line_elements)  # convert "0"/"1" to booleans
        board.append(row_values)

    assert_rectangular(board)  # Check if the board is rectangular

    return board  # Return the parsed board


def set_row_values(line_elements: list[str]) -> list[bool]:
    """
    Convert a list of "0"/"1" strings into booleans.
    Args:
        line_elements (list[str]): Strings "0"/"1".
    Returns:
        list[bool]: Row with True/False.
    """
    if not isinstance(line_elements, list) or len(line_elements) == 0:
        raise ValueError("line_elements must be a non-empty list.")
    
    row_values: list[bool] = []

    for val in line_elements:
        val = val.strip()  # trim whitespace from the value
        if val == "1":
            row_values.append(True)
        elif val == "0":
            row_values.append(False)
        else:
            raise ValueError("Invalid: Each element must be '0' or '1'.")
        
    return row_values  # Return the parsed row values