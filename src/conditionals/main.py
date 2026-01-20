# index of conditional (boolean) functions
# < : less than
# > : greater than
# <= : less than or equal to
# >= : greater than or equal to
# == : equal to
# != : not equal to
# in : membership test
# not in : negated membership test
# and: logical AND, short circuits so if first operand is False, second is not evaluated
# or: logical OR, short circuits so if first operand is True, second is not evaluated
# xor: logical XOR, True if exactly one operand is True, False otherwise
    # truth table:
    # A     B      A and B   A or B   A xor B
    # True  True   True      True     False
    # True  False  False     True     True
    # False True   False     True     True
    # False False  False     False    False

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
    zero is both positively and negatively sign (rather than being unsigned)
    Parameters:
    - x (int): first integer
    - y (int): second integer
    Returns:
    bool: True if x and y have the same sign, False otherwise
    """
    # # version 1, naive
    # if (x >= 0 and y >= 0) or (x < 0 and y < 0):
    #     return True
    # else:
    #     return False

    # # version 2, using multiplication
    # if (x * y) >= 0:
    #     return True
    # else:
    #   return False

    # # version 3, using multiplication and no else
    # if (x * y) >= 0:
    #     return True
    # return False # if we make it here, then the function didnt return True

    # version 4, using multiplication and returning the boolean expression directly
    return (x * y) >= 0

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

def main():
    print("Conditionals module begins here!")
    x = 5
    y = 10  
    print(f"Testing min_2(x,y) = min_2({x},{y}) = {min_2(x,y)}")
    # print(min_2(x, y))

    print(f"Testing which_is_greater(x,y) = which_is_greater({x},{y}) = {which_is_greater(x,y)}")
    # print(which_is_greater(x, y))

    print(f"Testing same_sign(x,y) = same_sign({x},{y}) = {same_sign(x,y)}")
    # print(same_sign(x, y))

    print(f"Testing positive_difference(x,y) = positive_difference({x},{y}) = {positive_difference(x,y)}")
    # print(positive_difference(x, y))

if __name__ == "__main__":
    main()
    