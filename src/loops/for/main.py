# general rule: use a for loop any time you can!
# when use a while loop? when you dont know how many iterations you'll need ahead of time
# range can be used three ways:
# range(stop) : goes from 0 to stop-1 inclusive
# range(start, stop) : goes from start to stop-1 inclusive
# range(start, stop, step) : goes from start to stop-1 inclusive, stepping by step each time

def say_hi_five_times() -> None:
    """
    Prints "Hi!" five times using a for loop.
    """
    for _ in range(5):  # _ is a throwaway variable since we don't use it
        print("Hi!")

# example, random 
def roll_die_till_n(n: int) -> None:
    import random
    die = 0
    count = 0
    while die != n:
        count += 1
        die = random.randint(1, 6)
        print(f"Iteration {count}: got {die}")

    print(f"Took {count} rolls to get a value of {n}!")

def main():
    print("For loops module begins here!")
    n = 5
    print(f"\nTesting another_factorial(n) = another_factorial({n}) = {another_factorial(n)}")
    # print(another_factorial(n))

    print(f"\nTesting sum_even(k) = sum_even({n}) = {sum_even(n)}")
    # print(sum_even(n))

    print(f"\nTesting roll_die_till_n(n) = roll_die_till_n({n})")
    roll_die_till_n(n)

    say_hi_five_times()

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

    # # let's do it backwards too
    # for n in range(n, 0, -1): # start at n, go to 1 inclusive (so put 0 for stop), step -1 each time
    #     factorial *= n
    # return factorial

# Insert your sum_even() function here.
def sum_even(k: int) -> int:
    """
    Takes as input an integer k and returns the sum of all even positive integers up to and             (possibly) including k.
    Parameters:
    - k (int): an integer
    Returns:
    int: sum of all even positive integers up to and (possibly) including k

    Raises an error if k is negative.
    """
    if k < 0:
        raise ValueError(f"Input k must be non-negative, got {k}.")

    # # v1: naive way:
    # cum_sum_even = 0
    # for k in range(0, k + 1, 1):
    #     if k % 2 == 0:
    #         cum_sum_even += k
    # return cum_sum_even

    # # v2: half the amount of work by stepping by 2
    # cum_sum_even = 0
    # if k < 0:
    #     raise ValueError(f"Input k must be non-negative, got {k}.")
    # elif k % 2 != 0:
    #     k -= 1  # make k even if it's odd
    # for k in range(0, k + 1, 2): # start at 0, go to k inclusive, step by 2 each time
    #     cum_sum_even += k
    # return cum_sum_even

    # v3: use gauss formula for sum of first n even numbers: n(n+1), where n is number of even numbers
    # number of even numbers up to and including k is k//2
    n = k // 2
    return 2 * gauss_sum(n//2)

def gauss_sum(n: int) -> int:
    """
    Compute the sum of the first n positive integers.
    Args:
        n: A non-negative integer.
    Returns:
        The sum of the first n positive integers.
    """
    return n * (n + 1) // 2

if __name__ == "__main__":
    main()
    