import math

def main():
    print("Arrays module (tuples, lists, sets) begins here!")
    print("Dicts are next!")

    # tuples are useful if we know the values in advance and they wont change
    # tuples are immutable arrays (we cannot change their values or length after creation)
    # tuples are defined with parentheses ()
    # Python is zero indexed, so first element is index 0
    # tuples can be heterogeneous (contain different types)
    point: tuple[int, int] = (3, 4)  # x, y
    print(f"point = {point}")
    print(f"point[0] = {point[0]}")  # x coordinate
    print(f"point[1] = {point[1]}")  # y coordinate

    point_3d: tuple[int, int, int] = (1, 2, 3)  # x, y, z
    print(f"point_3d = {point_3d}")
    print(f"point[0] = {point[0]}")  # x coordinate
    print(f"point[1] = {point[1]}")  # y coordinate
    print(f"point_3d[2] = {point_3d[2]}")  # z coordinate

    try:
        point[0] = 10  # type: ignore # this will raise an error because tuples are immutable
    except TypeError as e:
        print(f"Error: {e}")

    # Lists are mutable arrays defined with square brackets []
    empty_list = []
    empty_lsit = list() # equivalent
    print(f"empty_list = {empty_list}")

    # a list of 6 zeros
    # NOTE: this creates a list with 6 references to the same integer object 0,
    # if we were to do this with a mutable object (like a list of lists), then changing one
    # element would change them all! so only good for immutable objects like ints, floats, strings, tuples
    n = 6
    a = [0] * n  # list of n zeros
    print(f"(v1) a = {a}")

    a[0] = 10  # change first element to 10
    print(f"(v2) a = {a}")

    i = 3
    k = 4
    a[2*i - 4] = (k // 2) ** 4 # a[2] = 16
    print(f"(v3) a = {a}")

    # len(a) gives number of elements in list a
    print(f"length of a = {len(a)}")

    # how to get last element of list
    print(f"last element of a = {a[len(a) - 1]}")
    print(f"last element of a (easier) = {a[-1]}")
    # negative indices count from the end of the list, so
    # a[-1] = a[len(a)-1], 
    # a[-2] = a[len(a)-2],
    # ...
    # a[0] = a[-len(a)]

    # what happens if you give Python something wierd?
    try:
        idx = len(a)
        print(a[idx])  # index out of range
    except IndexError as e:
        print(f"Error: {e}, idx = {idx}, len(a) = {len(a)}")
    try:
        idx = -len(a)-1
        print(a[idx])  # index out of range
    except IndexError as e:
        print(f"Error: {e}, idx = {idx}, len(a) = {len(a)}")


    # let's make a small list of mixed types
    mixed_list = [1, 2.5, "hello", (3, 4), False, [5.01, 6]]
    print(f"mixed_list = {mixed_list}")

def factorial_array(n: int) -> list[int]:
    """
    Produces a list of all factorials from 0! to n!

    :param n: a nonnegative integer
    :type n: int
    
    :return: list of factorials from 0! to n!, so length n+1 where k-th element is k!
    :rtype: list[int]
    Raises an error if n is negative.
    """

    if n < 0:
        raise ValueError(f"Input n must be non-negative, got {n}.")
    
    fact: list[int] = [0] * (n + 1)  # list to hold factorials from 0! to n!
    fact[0] = 1  # 0! = 1
    for k in range(1, n + 1):
        # if we range(0, n +1), then k goes from 0 to n inclusive, which is wrong
        # because we would try to access fact[-1] when k=0, which will be last element
        # and will fill the list with all zeros (since last element is zero and propogates)
        fact[k] = fact[k - 1] * k  # k! = (k-1)! * k

    return fact

def min_integer_array(a: list[int]) -> int:
    """
    Returns the minimum integer in a list of integers.

    :param a: list of integers
    :type a: list[int]
    :return: minimum integer in the list
    :rtype: int

    Raises an error if the list is empty.
    """
    if len(a) == 0:
        raise ValueError("Input list must not be empty.")

    min_val = a[0] # initialize min_val to first element

    # first way, using indices
    # for i in range(1, len(a)):
    #     if a[i] < min_val:
    #         min_val = a[i]
    # return min_val

    # pythonic way
    for val in a:
        if val < min_val:
            min_val = val
    return min_val

# let's look at variadic functions
# min() can take an abitrary number of arguments
# min(2,3), mmin(-1, 47, 58, 900), etc.
# ^see how many values there are in each call
# ^^ we can define our own variadic functions using *args syntax
def min_integers(*numbers: int) -> int:
    """
    Returns the minimum integer among the input integers.

    :param numbers: arbitrary number of integer arguments
    :type numbers: int
    :return: minimum integer among the inputs
    :rtype: int

    Raises an error if no integers are provided.
    """
    # # THIS LOOKS SIMILAR TO WHAT WE WROTE ABOVE, SO LET'S CALL THAT
    # if len(numbers) == 0:
    #     raise ValueError("At least one integer must be provided.")

    # min_val = numbers[0]  # initialize min_val to first argument

    # for val in numbers:
    #     if val < min_val:
    #         min_val = val
    # return min_val

    # LET'S CALL THE PREVIOUS FUNCTION INSTEAD AFTER TYPE CASTING
    m = min_integer_array(list(numbers))
    return m

def change_first_element_list(a: list[int]) -> None:
    """
    Changes the first element of the input list to 42.

    :param a: list of integers
    :type a: list[int]
    :return: None
    :rtype: None
    Raises an error if the list is empty.
    """
    if len(a) == 0:
        raise ValueError("Input list must not be empty.")

    a[0] = 42  # change first element to 42
    return None  # optional, since functions return None by default if no return statement

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

    if p == 0 or p == 1:
        return False

    # isqrt is integer square root
    for i in range(2, math.isqrt(p) + 1):
        if p % i == 0:
            return False
    return True

# Insert your trivial_prime_finder() function here, along with any subroutines that you need.
"""
Pseudocode:

TrivialPrimeFinder(n)
    primeBooleans ← array of n + 1 false boolean variables
    for every integer p from 2 to n
        if IsPrime(p) is true
            primeBooleans[p] ← true
    return primeBooleans
"""
def trivial_prime_finder(n: int) -> list[bool]:
    """
    Returns a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    Parameters:
    - n (int): an integer
    Returns:
    list (bool): a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    """

    prime_booleans = [False] * (n + 1)

    for i in range(2, n + 1):
        if is_prime(i):
            prime_booleans[i] = True

    return prime_booleans

# Insert your cross_off_multiples() function here, along with any subroutines that you need.
def cross_off_multiples(prime_booleans: list[bool], p:int) -> list[bool]:
    """
    Returns an updated list in which all variables in the array whose indices are multiples of p         (greater than p) have been set to false.
    Parameters:
    - prime_booleans (list): a list of boolean variables storing the primality of each nonnegative         integer
    - p (int): an integer
    Returns:
    list (bool): a list of boolean variables storing the primality of each nonnegative integer up to                 and including n with multiples of p (greater than p) set to false.
    """
    
    # n = len(prime_booleans) - 1
    # for i in range(2*p, n + 1, p):
    #   prime_booleans[i] = False

    print(f"p = {p}")
    # len(prime_booleans) is n + 1, we want [0,n] inclusive s
    for i in range(2*p, len(prime_booleans), p):
        print(f"    for p = {p}, i = {i} is set to False")
        prime_booleans[i] = False
    
    return prime_booleans

"""
Pseudocode:
SieveOfEratosthenes(n)
    primeBooleans ← array of n + 1 true boolean variables
    primeBooleans[0] ← false
    primeBooleans[1] ← false
    for every integer p between 2 and √n
        if primeBooleans[p] = true
            primeBooleans ← CrossOffMultiples(primeBooleans,p)
    return primeBooleans
"""

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
        if prime_booleans[p] == True:
            prime_booleans = cross_off_multiples(prime_booleans = prime_booleans, p = p)

    return prime_booleans

# Hint: insert your cross_off_multiples() function here

# Insert your list_primes() function here, along with any subroutines that you need.
def list_primes(n: int) -> list[int]:
    """
    List all prime numbers up to and (possibly) including n.
    Parameters:
    - n (int): an integer
    Returns:
    list (int): a list containing all prime numbers up to and (possibly) including n.
    """
    
    prime_booleans = sieve_of_eratosthenes(n = n)

    primes_list = []

    for i in range(2, n + 1):
        if prime_booleans[i]:
            primes_list.append(i)

    return primes_list

# Hint: insert your sieve_of_eratosthenes() and cross_off_multiples functions here


if __name__ == "__main__":
    main()

    # Test the factorial_array function
    n = 10
    factorials = factorial_array(n)
    print(f"Factorials from 0! to {n}! : {factorials}")

    c = [3,2,1]
    print(f"min of c = {min_integer_array(c)}")

    print(f"min of (5,3,8,1,4) = {min_integers(5,3,8,1,4)}")

    c = [0] * 6 # [0, 0, 0, 0, 0, 0]
    change_first_element_list(c)
    print(f"After change_first_element, c = {c}")
    # NOTE: this behavior is different than from what we've seen before with integers and strings,
    # because lists are mutable, so when we pass them to functions, the function can modify
    # the original list. with integers and strings, the function gets a copy of the value,
    # so modifying it inside the function does not affect the original variable

    print(f"sieve_of_eratosthenes({10}) = {sieve_of_eratosthenes(10)}")

    print(f"all primes between 1 and 100: {list_primes(100)}")
