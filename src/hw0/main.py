def main():
    n = 1000
    k = 998
    print(f"combination(n,k) = combination({n},{k}) = {combination(n,k)}")

# Insert your permutation() function here, along with any subroutines that you need.
def permutation(n: int, k: int) -> int:
    """
    Compute the permutation statistic P(n, k) = n · (n-1) · ... · (n-k+1) = n! / (n-k)!.
    Args:
        n: Total number of distinct objects (non-negative).
        k: Number of positions to fill (non-negative).
    Returns:
        The number of ways to choose and order k items from n, i.e., P(n, k).
    """
    # # version 1, naively use subroutine (and duplicate n-k work once)
    # return another_factorial(n)//another_factorial(n - k)

    # version 2, do a little factorial math
    # n!/(n-k)! = (n * (n-1) * ... * (n-k)!)/((n-k)!) = n * (n-1) * ... * (n - k + 1)
    factorial = 1
    # print("initial ", n, n - k + 1 + 1)
    for n in range(n - k + 1, n + 1):
        # print(n)
        factorial *= n
    return factorial

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
    # NOTE: range(start, stop) goes from start to stop-1 inclusive. so 
    # to go from 1 to n inclusive, we do range(1, n+1)
    for n in range(1, n+1):
        # print(n)
        factorial *= n
    return factorial

# Insert your combination() function here, along with any subroutines that you need.
def combination(n: int, k: int) -> int:
    """
    Compute the combination statistic C(n, k) = n! / ((n - k)! * k!).
    Args:
        n: Total number of distinct objects (non-negative).
        k: Size of the subset to choose (non-negative).
    Returns:
        The number of ways to choose k items from n without order (the binomial coefficient).
    """
    # v1, naively use subroutines
    return permutation(n,k)//another_factorial(k)

    # # ACTUALLY, we don't compute k! with permutation(), so we can let the two separate functions
    # # do their own work, and nothing is duplicated/wasted
    # # v2, do a lil math and save the value for k
    # # n!/(n-k)! = (n * (n-1) * ... * (n-k)!)/((n-k)!) = n * (n-1) * ... * (n - k + 1)
    # # and save k! along the way!
    # factorial = 1
    # # print("initial ", n, n - k + 1 + 1)
    # for n in range(n - k + 1, n + 1):
    #     # print(n)
    #     factorial *= n
    # return factorial

if __name__ == "__main__":
    main()
    