import time

"""
Pseudocode for GCD algorithms:

TrivialGCD(a,b)
    d ← 1
    m ← Min2(a,b)
    for every integer p between 1 and m
        if p is a divisor of both a and b
            d ← p
    return d

EuclidGCD(a,b)
    while a ≠ b
        if a > b
            a ← a − b
        else
            b ← b − a
    return a 

# AN EVEN BETTER LEVEL!

GCD(50, 375) = GCD(50, 375 − 50) 
             = GCD(50, 325)
             = GCD(50, 275)
             = GCD(50, 225)
             ...
             = GCD(50, 25)

What's the pattern above? Repeated subtractions of 
25, which is really dividing and taking the remainder
i.e. the modulus operation!

GCD(50, 375) = GCD(50, 375 % 50)
             = GCD(50 % 50, 25)
             = GCD(0, 25)
             = 25
"""

def trivial_gcd(a: int, b: int) -> int:
    """
    Returns the greatest common divisor (GCD) of two integers a and b using the trivial method.
    
    :param a: 
    :type a: int
    :param b:
    :type b: int
    :return: GCD of a and b
    :rtype: int
    """

    if type(a) is not int or type(b) is not int:
        raise TypeError(f"Inputs must be integers, got a={a} ({type(a)}), b={b} ({type(b)}).")

    # we can handle negative inputs by taking absolute values
    if a < 0:
        a = -a
    if b < 0:
        b = -b

    # GCD(0,n) == n for n >= 0 (so GCD (0,0) is zero here)
    # and since we've made everything positive
    # we can just return the other number if one is zero
    if a == 0:
        return b
    if b == 0:
        return a
    
    d = 1 # initialize GCD

    m = min(a,b)

    # try every possible candidate divisor from 1 
    # up to m (inclsusive), and update d every time
    # we find a divisor

    for p in range(2, m + 1):
        # if p is a divisor of both a and b, then d = p
        if (a % p == 0) and (b % p == 0):
            # if we did "or" instead of "and", this would 
            # always return m! since m is equal to either a or b
            # and is always the last value tested, and a number is
            # always divisible by itself
            d = p
    return d


def euclid_gcd(a: int, b: int) -> int:
    """
    Returns the greatest common divisor (GCD) of two integers a and b using Euclid's method.
    
    :param a: 
    :type a: int
    :param b:
    :type b: int
    :return: GCD of a and b
    :rtype: int
    """

    if type(a) is not int or type(b) is not int:
        raise TypeError(f"Inputs must be integers, got a={a} ({type(a)}), b={b} ({type(b)}).")

    # we can handle negative inputs by taking absolute values
    if a < 0:
        a = -a
    if b < 0:
        b = -b

    # GCD(0,n) == n for n >= 0 (so GCD (0,0) is zero here)
    # and since we've made everything positive
    # we can just return the other number if one is zero
    if a == 0:
        return b
    if b == 0:
        return a

    # critical fact:
    # GCD(a,b) == GCD(a-b, b) (if a > b)
    # GCD(a,b) == GCD(a, b-a) (if b > a)
    # example:
        # GCD(63, 42) == GCD(21, 42) == GCD(21, 21) == 21

    while a != b:
        # two cases depending on which is larger (we already know
        # they are not equal bc of while condition)
        if a > b:
            a = a - b
        else:
            b = b - a
    return a # or return b, since a == b here

def euclid_gcd_mod(a: int, b: int) -> int:
    """
    Returns the greatest common divisor (GCD) of two integers a and b using Euclid's method with modulus.
    
    :param a: 
    :type a: int
    :param b:
    :type b: int
    :return: GCD of a and b
    :rtype: int
    """

    if type(a) is not int or type(b) is not int:
        raise TypeError(f"Inputs must be integers, got a={a} ({type(a)}), b={b} ({type(b)}).")

    # we can handle negative inputs by taking absolute values
    if a < 0:
        a = -a
    if b < 0:
        b = -b

    # GCD(0,n) == n for n >= 0 (so GCD (0,0) is zero here)
    # and since we've made everything positive
    # we can just return the other number if one is zero
    if a == 0:
        return b
    if b == 0:
        return a

    # critical fact: GCD(a, b) = GCD(a-b, b) when a > b
    # but subtracting b from a repeatedly is the same as
    # taking a mod b (the remainder when a is divided by b)
    # so we can speed things up by using the modulus operation directly
    # so GCD(a, b) = GCD(a % b, b) when a > b
    # similarly, GCD(a, b) = GCD(a, b % a) when b > a
    while (a != 0) and (b != 0):
        if a > b:
            a = a % b
        else: # so b >= a
            b = b % a

    # if we make it here, then one of a or b is zero
    if a == 0:
        return b
    else:
        return a

def compare_gcd_algorithms(x: int, y: int):
    start_time = time.time()
    answer_1 = trivial_gcd(x, y)
    elapsed_1 = time.time() - start_time
    print(f"\ntrivial_gcd({x}, {y}) = {answer_1}")
    print(f"trivial_gcd took {elapsed_1:.6f} seconds")


    start_time = time.time()
    answer_2 = euclid_gcd(x, y)
    elapsed_2 = time.time() - start_time
    print(f"\neuclid_gcd({x}, {y}) = {answer_2}")
    print(f"euclid_gcd took {elapsed_2:.6f} seconds")

    start_time = time.time()
    answer_3 = euclid_gcd_mod(x, y)
    elapsed_3 = time.time() - start_time
    print(f"\neuclid_gcd_mod({x}, {y}) = {answer_3}")
    print(f"euclid_gcd_mod took {elapsed_3:.6f} seconds")

    # the speedup provided by algorithm 1 to 2
    print(f"\nSpeedup of euclid_gcd over trivial_gcd: {elapsed_1 / elapsed_2}x")

    # the speedup provided by algorithm 1 to 3
    print(f"\nSpeedup of euclid_gcd_mod over trivial_gcd: {elapsed_1 / elapsed_3}x")

    # the speedup provided by algorithm 2 to 3
    print(f"\nSpeedup of euclid_gcd_mod over euclid_gcd: {elapsed_2 / elapsed_3}x")
    print("--------------------------")

def main():
    print("GCD module")

    x = 63
    y = 42
    print(f"Testing trivial_gcd({x}, {y}) = {trivial_gcd(x, y)}")


    # let's time both algorithms on large inputs
    print("\nlarge inputs:")
    x: int = 3782026
    y: int = 2781479
    compare_gcd_algorithms(x, y)

    # let's time both algorithms on small inputs
    print("\nsmall inputs:")
    x: int = 378
    y: int = 278
    compare_gcd_algorithms(x, y)

    # let's time both algorithms on really large inputs
    print("\nreally large inputs:")
    x: int = 378202612
    y: int = 278147912
    compare_gcd_algorithms(x, y)

    # let's time both algorithms on x >>> y large inputs
    print("\n when x >>> y:")
    x: int = 378202612
    y: int = 2781
    compare_gcd_algorithms(x, y)

if __name__ == "__main__":
    main()