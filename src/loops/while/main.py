# Insert your factorial() function here.
def factorial(n: int) -> int:
    """
    Compute n! (factorial) using a while loop.
    Args:
        n: A non-negative integer.
    Returns:
        The factorial of n.
    """
    
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
    """
    cum_sum = 0
    
    while n > 0:
        cum_sum += n
        n -= 1
        
    return cum_sum


if __name__ == "__main__":
    main()
    