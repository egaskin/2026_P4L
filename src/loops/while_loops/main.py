

# Insert your factorial() function here.
def factorial(n: int) -> int:
    """
    Compute n! (factorial) using a while loop.
    Args:
        n: A non-negative integer.
    Returns:
        The factorial of n.

    Raises an error if n is negative.
    """

    if n < 0:
        raise ValueError(f"Input n must be non-negative, got {n}.")
    
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1

    return factorial

# Insert your sum_first_n_integers() function here.
def sum_first_n_integers(n: int) -> int:
    """
    Takes as input an integer n and returns the sum of the first n positive integers.
    Parameters:
    - n (int): an integer
    Returns:
    int: sum of the first n positive integers

    Raises an error if n is negative.
    """

    if n < 0:
        raise ValueError(f"Input n must be non-negative, got {n}.")

    cumu_sum = 0
    
    while n > 0:
        cumu_sum += n
        n -= 1
        
    return cumu_sum

def main():
    print("While loops module begins here!")
    n = 5
    print(f"\nTesting factorial(n) = factorial({n}) = {factorial(n)}")
    # print(factorial(n))

    print(f"\nTesting sum_first_n_integers(n) = sum_first_n_integers({n}) = {sum_first_n_integers(n)}")
    # print(sum_first_n_integers(n))

    print(f"\nTesting factorial(n) with negative input = factorial({n})")
    try:
        n = -3

        # this line should never execute (an error will raise when factorial(n) is called)
        print(f"Function didn't raise an error for negative input: factorial({n}) = {factorial(n)}")
    except ValueError as e:
        print(f"Caught an error as expected: {e}")

    

if __name__ == "__main__":
    main()
    