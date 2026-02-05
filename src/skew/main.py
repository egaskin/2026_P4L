def main():
    print("Skew array code!")

# Insert your skew() function here, along with any subroutines that you need.
def skew(symbol: str) -> int:
    """
    skew returns 1 or -1 if the given single character string is either G or C respectively (case-       insensitive), otherwise returns zero. 
    Throws an error if the given string does not have a length of one.
    Parameters:
    - symbol (str): A given one character string.
    Returns:
    - int: The symbol's respective skew score.
    """
    if len(symbol) != 1:
        raise ValueError(f"Symbol must have length 1, got symbol = {symbol}")

    if symbol == "G":
        return 1
    elif symbol == "C":
        return -1
    else:
        return 0

# Insert your skew_array() function here, along with any subroutines that you need.
def skew_array(genome: str) -> list[int]:
    """
    skew_array returns the list that represents the skew at each position of the genome. That is,       the i-th position in the list is the skew at the i-th position of the genome.
    Parameters:
    - genome (str): A genome string.
    Returns:
    - list[int]: A list representing the skew of the genome string.
    """

    """
    SkewArray(genome)
        n ← len(genome)
        array ← array of length n + 1
        array[0] ← 0
        for every integer i between 1 and n
            array[i] = array[i-1] + Skew(genome[i-1])
        return array
    """
    # # attempt at recursive solution based on: https://www.w3reference.com/blog/recursive-list-comprehension-in-python/
    # # issue below is that skew(genome[i]) only calculates the skew at position i exactly, not recursively calling deeper skews
    # # to get previous skew values. skew(genome[i-1]) needs to be a function that accesses the cumumalitive skew at genome[i-1]
    # def get_ith_skew(i, genome):
    #     if i == 0:
    #         return skew(genome[i])
    #     else:
    #         return skew(genome[i]) + skew(genome[i-1])
    # return [get_ith_skew(i, genome) for i, _ in enumerate(genome)]

    n = len(genome)
    array = [0] * (n + 1)
    for i in range(1, n + 1):
        array[i] = array[i-1] + skew(genome[i-1])
    return array

# Insert your minimum_skew() function here, along with any subroutines that you need.
def minimum_skew(genome: str) -> list[int]:
    """
    minimum_skew finds the list of integers representing all integer indices that minimizes the skew     of the genome text.
    Parameters:
    - genome (str): A genome string.
    Returns:
    - list[int]: A list of indices that minimize the skew value of the genome text.
    """
    skew_array_list = skew_array(genome)

    min_val = min(skew_array_list)

    found_locations = []

    for i, val in enumerate(skew_array_list):
        if val == min_val:
            found_locations.append(i)

    return found_locations


if __name__ == "__main__":
    main()