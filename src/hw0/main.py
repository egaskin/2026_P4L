import math
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

# Insert your power() function here, along with any subroutines that you need.
def power(a: int, b: int) -> int:
    """
    Compute a raised to the b-th power.
    Args:
        a: Base integer (can be negative, zero, or positive).
        b: Exponent integer (must be non-negative).
    Returns:
        The integer value of a^b. By convention, 0^0 returns 1.
    """
    return a**b
    # they probably wanted a for loop
    

# Insert your sum_proper_divisors() function here, along with any subroutines that you need.
def sum_proper_divisors(n: int) -> int:
    """
    Return the sum of all proper (positive) divisors of n, i.e., divisors strictly less than n.
    Args:
        n: Integer input.
    Returns:
        The sum of all positive divisors of n that are < n.
        Returns 0 for n <= 1.
    """
    
    if n <= 1:
        return 0
    
    cum_sum = 1
    # range using the integer square root since if we know i < sqrt(n) is a divisor of n, 
    # then we know that n//i > sqrt(n) and is a divisor of n
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            # print(i)
            # n = i * n//i
            cum_sum += i + n//i # add both divisors in one step
    return cum_sum

def fibonacci_array(n: int) -> list[int]:
    """
    Return an array of Fibonacci numbers from F₀ through Fₙ.
    Args:
        n: A non-negative integer.
    Returns:
        A list F of length n + 1 such that F[k] is the k-th Fibonacci number.
    """
    fib_array = [0] * (n + 1)
    fib_array[0] = 1
    if n == 0:
        return fib_array
    fib_array[1] = 1
    for i in range(2, n + 1):
        fib_array[i] = fib_array[i - 2] + fib_array[i - 1]

    return fib_array

def divides_all(a: list[int], d: int) -> bool:
    """
    Determine whether d divides every element of a.
    Args:
        a: A list of integers.
        d: The candidate divisor.
    Returns:
        True if every element x in a satisfies x % d == 0.
        False immediately if d == 0, since zero is not a divisor of any number.
    """
    if d == 0:
        return False
    
    for cur_int in a:
        if cur_int % d != 0:
            return False
        
    return True

def max_integers(*numbers: int) -> int:
    """
    Return the maximum integer among a variable number of inputs.
    Args:
        numbers: One or more integers.
    Returns:
        The largest integer in numbers.
    Raises:
        ValueError: If no numbers are provided.
    """
    return max(numbers)

# Insert your sum_integers() function here, along with any subroutines that you need.
def sum_integers(*numbers: int) -> int:
    """
    Return the sum of a variable number of integers.
    Args:
        numbers: Zero or more integers.
    Returns:
        The sum of all provided integers. Returns 0 if no arguments are given.
    """
    return sum(numbers)

# Insert your gcd_array() function here, along with any subroutines that you need.
def gcd_array(a: list[int]) -> int:
    """
    Return the greatest common divisor (GCD) of all integers in the list.
    Args:
        a: A non-empty list of integers (values may be negative or zero).
    Returns:
        The non-negative GCD of all numbers in `a`. 
    """
    max_val = max(a)

    gcd = 1
    for i in range(1, max_val + 1):
        if divides_all(a, i):
            gcd = i
    return gcd

def is_perfect(n: int) -> bool:
    """
    Determine whether an integer n is a perfect number.
    Args:
        n: Integer to test.
    Returns:
        True if n is perfect, False otherwise.
    """
    return (sum_proper_divisors(n) == n)

# Insert your next_perfect_number() function here, along with any subroutines that you need.
def next_perfect_number(n: int) -> int:
    """
    Return the smallest perfect number strictly greater than n.
    Args:
        n: Integer threshold.
    Returns:
        The least perfect number > n.
    """
    
    next_perf_num = 6
    print(f"n = {n}, next_perf_num = {next_perf_num}")


    first_exp = 2
    second_exp = 3
    while next_perf_num <= n:
        next_perf_num = calc_perf_num(first_exp, second_exp)
        print(f".    next_perf_num = {next_perf_num}, first_exp = {first_exp}, {second_exp}")

        first_exp += 2
        second_exp += 2

    return next_perf_num

def calc_perf_num(first_exp, second_exp):
    print("THIS FUNCTION IS INCORRECT UNFORTUNATELY. THE PERFECT NUMBERS DONT FOLLOW THE PATTERN I THOUGHT...")
    return (2**(first_exp)) * ((2**(second_exp)) - 1)

# Insert your list_mersenne_primes() function here, along with any subroutines that you need.
def list_mersenne_primes_v2(n: int) -> list[int]:
    """
    List all Mersenne primes of the form 2^p - 1 with p ≤ n.
    Args:
        n: Upper bound on the exponent p (non-negative integer).
    Returns:
        A list of all primes of the form 2^p - 1 where p is prime and p ≤ n,
        in increasing order of p.
    """
    # initialize list for answers
    found_mersenne_primes = []

    # range over all the numbers from 1 to n, check element in primes_1_to_n if exists
    for p in range(1, n + 1):
        candidate_mersenne = 2**p - 1
        if is_prime(candidate_mersenne):
            found_mersenne_primes.append(candidate_mersenne)

    return found_mersenne_primes

# Insert your is_prime() function here, along with any subroutines that you need.
def is_prime(p: int) -> bool:
    """
    Determine whether an integer is prime.
    Test if p is prime.
    Parameters:
    - p (int): an integer
    Returns:
    bool: True if p is prime and False otherwise.
    """

    # 0 and 1 are not prime
    if p < 2:
        return False

    # isqrt is integer square root
    # we only need the integer square root of p because:
        # define p = k * b, with k <= b then we know k <= sqrt(p).
        # proof: assume k > sqrt(p), then b >= k > sqrt(p)
        # so k * b > sqrt(p) * sqrt(p) = p, which is a contradiction
        # so our assumption must be false, so k <= sqrt(p)
    for i in range(2, math.isqrt(p) + 1):
        if p % i == 0:
            return False
    return True

# Insert your list_mersenne_primes() function here, along with any subroutines that you need.
def list_mersenne_primes_v1(n: int) -> list[int]:
    """
    List all Mersenne primes of the form 2^p - 1 with p ≤ n.
    Args:
        n: Upper bound on the exponent p (non-negative integer).
    Returns:
        A list of all primes of the form 2^p - 1 where p is prime and p ≤ n,
        in increasing order of p.
    """
    # initialize list for answers
    found_mersenne_primes = []

    # get all the primes up to and including n
    primes_1_to_n = sieve_of_eratosthenes(2**n - 1)

    # range over all the numbers from 1 to n, check element in primes_1_to_n if exists
    for p in range(1, n + 1):
        candidate_mersenne = 2**p - 1
        if primes_1_to_n[candidate_mersenne]:
            found_mersenne_primes.append(candidate_mersenne)

    return found_mersenne_primes
        
# Insert your sieve_of_eratosthenes() function here, along with any subroutines that you need.
def sieve_of_eratosthenes(n: int) -> list[bool]:
    """
    Returns a list of boolean variables storing the primality of each nonnegative integer up to and including n,
    implementing the "sieve of Eratosthenes" algorithm.
    Parameters:
    - n (int): an integer
    Returns:
    list (bool): a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    """
    prime_booleans = [True] * (n + 1)
    prime_booleans[0], prime_booleans[1] = False, False
    for p in range(2, math.isqrt(n) + 1):
        if prime_booleans[p] == True: # if we reach a gray value in animation, we know it's prime
            prime_booleans = cross_off_multiples(prime_booleans = prime_booleans, p = p)

    return prime_booleans

# Insert your cross_off_multiples() function here, along with any subroutines that you need.
def cross_off_multiples(prime_booleans: list[bool], p:int) -> list[bool]:
    """
    Returns an updated list in which all variables in the array whose indices are multiples of p (greater than p) have been set to false.
    Parameters:
    - prime_booleans (list): a list of boolean variables storing the primality of each nonnegative integer
    - p (int): an integer
    Returns:
    list (bool): a list of boolean variables storing the primality of each nonnegative integer up to and including n with multiples of p (greater than p) set to false.
    """
    
    # n = len(prime_booleans) - 1
    # for i in range(2*p, n + 1, p):
    #   prime_booleans[i] = False

    # print(f"p = {p}") # GOOD DEBUG PRINT STATEMENT
    # len(prime_booleans) is n + 1, we want [0,n] inclusive
    # we can start at 2*p because the first multiple of p that is not p itself is 2*p
    # then we can go to 3*p, 4*p, ..., up to n
    for i in range(2*p, len(prime_booleans), p):
        # print(f"    for p = {p}, i = {i} is set to False") # GOOD DEBUG PRINT STATEMENT
        prime_booleans[i] = False
    
    return prime_booleans

# Insert your next_twin_primes() function here, along with any subroutines that you need.
def next_twin_primes(n: int) -> tuple[int, int]:
    """
    Return the smallest pair of twin primes (p, p+2) such that both p and p+2 are > n.
    Args:
        n: Integer threshold.
    Returns:
        A tuple (p, q) where q = p + 2 are twin primes and p > n.
    """
    
    next_pair = ()
    while len(next_pair) == 0:
        candidate_a = n + 1
        candidate_b = candidate_a + 2

        if is_prime(candidate_a) and is_prime(candidate_b):
            next_pair = (candidate_a, candidate_b)
        n += 1
    
    return next_pair

if __name__ == "__main__":
    main()
    