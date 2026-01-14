# Insert your another_factorial() function here.
def another_factorial(n: int) -> int:
    """
    Compute n! (factorial) using a for loop.
    Args:
        n: A non-negative integer.
    Returns:
        The factorial of n.
    Raises:
        ValueError: If n is negative.
    """
    factorial = 1
    for n in range(1, n+1):
        # print(n)
        factorial *= n
    return factorial

# Insert your sum_even() function here.
def sum_even(k: int) -> int:
    """
    Takes as input an integer k and returns the sum of all even positive integers up to and             (possibly) including k.
    Parameters:
    - k (int): an integer
    Returns:
    int: sum of all even positive integers up to and (possibly) including k
    """

    cum_sum_even = 0
    for k in range(0, k + 1, 1):
        if k % 2 == 0:
            cum_sum_even += k
    
    return cum_sum_even

if __name__ == "__main__":
    main()
    