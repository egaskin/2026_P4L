import csv

def read_electoral_votes(filename: str) -> dict[str, int]:
    """
    Processes the number of electoral votes for each state.

    Parameters:
        filename (str): A filename string.

    Returns:
        dict[str, int]: A dictionary that associates each state name (string)
        to an integer corresponding to its number of Electoral College votes.
    """
    if len(filename) == 0 or not isinstance(filename, str):
        raise ValueError("filename must be a non-empty string.")
    
    electoral_votes: dict[str,int] = {}

    # parse the file contents
    # get a file object from a "file" from filename
    with open(filename, "r") as file:
        lines = csv.reader(file) # returns a list, one line per element
        
        # each element in lines is a list of string
        # e.g. lines[0] = ["Alabama", "9"]

        # range over all lines and for eahc one, parse state name and number of votes
        for line in lines:
            state_name = line[0]
            num_votes = int(line[1])
            electoral_votes[state_name] = num_votes

    return electoral_votes

def read_polling_data(filename: str) -> dict[str, float]:
    """
    Parses polling percentages from a file.

    Parameters:
    - filename (str): A filename string.

    Returns:
    - dict[str, float]: A dictionary of state names (strings) to floats
      corresponding to the percentages for candidate 1.
    """
    if len(filename) == 0 or not isinstance(filename, str):
        raise ValueError("filename must be a non-empty string.")
    
    candidate_1_percentages: dict[str,float] = {}

    # parse the file contents
    # get a file object from a "file" from filename
    with open(filename, "r") as file:
        lines = csv.reader(file) # returns a list, one line per element
        for line in lines:
            state_name = line[0]
            num_votes = float(line[1])
            candidate_1_percentages[state_name] = num_votes/100.0

    return candidate_1_percentages