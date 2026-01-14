

# Insert your min_2() function here.
def min_2(a: int, b: int) -> int:
    """
    Takes two integers as input and returns their minimum.
    Parameters:
    - a (int): first integer
    - b (int): second integer
    Returns:
    int: minimum of a and b
    """
    if a < b:
        return a
    else:
        return b

# Insert your which_is_greater() function here.
def which_is_greater(x: int, y: int) -> int:
    """
    Takes two integers as inputs and returns 1 if the first input is larger, -1 if the second input is larger, and 0 if they are equal.
    Parameters:
    - x (int): first integer
    - y (int): second integer
    Returns:
    int: 1 if x is greater than y, -1 if y is greater than x, and 0 if x and y are equal
    """
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0

# Insert your same_sign() function here.
def same_sign(x: int, y: int) -> bool:
    """
    Takes two integers as input and returns True if they have the same sign, and False if they have different signs. Note: we assume that
    zero has a POSITIVE sign (rather than being unsigned)
    Parameters:
    - x (int): first integer
    - y (int): second integer
    Returns:
    bool: True if x and y have the same sign, False otherwise
    """
    if (x * y) > 0:
        return True
    return False

    # Insert your positive_difference() function here.
def positive_difference(a: int, b: int) -> int:
    """
    Takes two integers as input and returns the absolute value of their difference.
    Parameters:
    - a (int): first integer
    - b (int): second integer
    Returns:
    int: positive difference of a and b
    """
    return abs(a - b)

if __name__ == "__main__":
    main()
    