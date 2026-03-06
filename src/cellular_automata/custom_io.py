from datatypes import GameBoard

def read_rules_from_file(filename: str) -> dict[str, str]:
    """
    read_rules_from_file takes a filename as a string and reads the rule strings provided in this file.
    It stores the result in a dictionary mapping neighborhood strings to integers.

    Args:
        filename (str): The name of the file containing the rule strings.

    Returns:
        dict[str, int]: A dictionary where keys are neighborhood strings and values are the resulting state integers.
    """
    # TODO: implement
    pass

def read_color_map_from_file(filename: str) -> dict:
    """
    Reads a color map configuration from a txt file and return it as a map.

    Args:
        filename (str): The path to the color map.

    Returns:
        dict: A map with keys as integers representing states and values of string representing colors.
        values must be of type dark_gray, white, red, gree, yellow, orange, purple, blue, or black
    """
    with open(filename, 'r') as f:
        giant_string = f.read()

    trimmed_giant_string = giant_string.strip()
    lines = trimmed_giant_string.splitlines()

    color_map: dict[str, str] = {}

    for line in lines:
        # each line should look like "0:black"
        parts = line.split(':')
        state = parts[0].strip()
        color = parts[1].strip()

        color_map[state] = color

    return color_map

def read_board_from_file(filename: str) -> GameBoard:
    """
    Reads a board configuration from a CSV file and returns it as a GameBoard.

    Args:
        filename (str): The path to the CSV file.

    Returns:
        GameBoard: A 2D list of integers representing the board.
    """
    # open(filename, 'r') opens the file in read mode ('r'), returning a file object (f).
    # with ensures the file is automatically closed when the block ends — even if there’s an error.
    with open(filename, 'r') as f: 
        # first, convert the whole file to a string
        giant_string = f.read()
        
    # trim any space at the start or end of file
    trimmed_giant_string = giant_string.strip()
    
    # split the long string into multiple strings, one for each line
    lines = trimmed_giant_string.splitlines()
    
    # lines is a list of strings, each element is each line of the file
    board: GameBoard = []
    
    # we will iterate over each line, parse the data in each line, and build the board
    for line in lines:
        line_elements = line.split(',')
        # line_elements contains a list of strings, one for each element in the row, i.e., a bunch of "0" and "1" strings
        board.append(set_row_values(line_elements))
        
    return board


def set_row_values(line_elements: list[str]) -> list[str]:
    """
    Convert a list of numeric strings into a list of integers.

    Args:
        line_elements (list[str]): A list of strings, where each element
                                   represents a nonnegative integer.

    Returns:
        list[int]: A list of integers parsed from the input strings.
    """
    current_row = []
    
    # parse the line and convert each element to an integer
    for element in line_elements:
        val = str(element)
        current_row.append(val)
        
    return current_row


