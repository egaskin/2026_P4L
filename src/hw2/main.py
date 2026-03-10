import sys
import random # this should be helpful!
import numpy as np

f = open("hw2/output.txt", "w")
sys.stdout = f
sys.stderr = f

def main():
    print("HW2, output being saved to file output.txt in the hw2 folder")
    # print("Run this code with the command: python hw2/main.py > hw2/output.txt 2>&1, to get output.txt")
    # exercise_6_2_3 = 0.607937761
    # print(f"exercise_6_2_3 = {exercise_6_2_3()}")
    # print(f"test_simulate_one_birthday_trial_v1: {test_simulate_one_birthday_trial_v1()}")

    # print(f"test_simulate_one_birthday_trial_v2: {test_simulate_one_birthday_trial_v2()}")

    # print(f"test_simulate_one_birthday_trial_v3: {test_simulate_one_birthday_trial_v3()}")
    # print(f"test_shared_birthday_probability_v1(): {test_shared_birthday_probability_v1()}")

    # print(f"exercise_6_3_4(): {exercise_6_3_4()}")

    print(f"exercise_6_4_5() = {exercise_6_4_5()}")

    print(f"exercise_6_5_2() = {exercise_6_5_2()}")

# Write your weighted_die() function here along with any subroutines that you need.
def weighted_die() -> int:
    """
    Simulate a weighted die that has a 10% chance of rolling a 1, a 10% chance of rolling a 2, 
    a 50% chance of rolling a
    3, a 10% chance of rolling a 4, a 10% chance of rolling a 5, and a 10% chance of rolling a 6.

    Args:
        None
    Returns:
        A pseudorandom integer between 1 and 6, inclusive, where the
        probability of rolling a 3 is 0.5 and the probability of rolling
        any other number is 0.1.
    """
    rand_num = random.random()

    if rand_num < 0.1:
        return 1
    elif rand_num < 0.2:
        return 2
    elif rand_num < 0.7:
        return 3
    elif rand_num < 0.8:
        return 4
    elif rand_num < 0.9:
        return 5
    else:
        return 6

# Write your estimate_pi() function here along with any subroutines that you need.
def estimate_pi(num_points: int) -> float:
    """
    Estimate pi using a Monte Carlo method. an estimate of the value of 𝝅 
    produced by sampling numPoints points uniformly from the square of side 
    length 2 centered at the origin, and multiplying 4 times the fraction of these 
    points falling in the circle of radius 1 centered at the origin.

    Args:
    - num_points (int): the number of points to use in the Monte Carlo method

    Returns:
    float: an estimate of pi
    """
    # get a random 2D cartesian coordinate for a square with 
    # side length = side_length, and center = center

    # if check_in_circle(coordinate_point_square, radius = 1, center = (0,0))
    count_in_circle = 0
    for idx in range(num_points):
        random_square_point = get_coordinate_square()

        if check_in_circle(random_square_point, radius = 1, center = (0,0)):
            count_in_circle += 1

    return 4*(count_in_circle/num_points)

def get_coordinate_square(side_length = 2, center: tuple[float, float] = (0,0)) -> tuple[float, float]:

    # random.random():
    # Return the next random floating-point number in the range 0.0 <= X < 1.0

    # so let's multiple both sides by side_length/2
    # 0.0*side_length/2 <= X < 1.0*side_length/2
    # 0.0 <= X < side_length/2
    # then adjust the bottom and lower boundaries based on the center x coordinate
    # 0.0 + center_x <= X < side_length/2 + center_x
    # and do similarly for the y coordinate


    x_coord = random.random()*side_length/2 + center[0]
    y_coord = random.random()*side_length/2 + center[1]

    return (x_coord, y_coord)

def check_in_circle(random_point, radius = 1, center = (0,0)):
    # formula for a circle in caretesian plane:
    # (x- h)^2 + (y - k)^2 = r^2 
    # where (h, k) is the center, r is the radius, and x and y are any point along the circle's
    # perimeter. 
    # https://www.cuemath.com/geometry/equation-of-circle/

    # Thus, using the formula, if plugging in the random_point results in a number greater than
    # the radius squared, it cannot be in the circle since it will be outside the circle's 
    # perimeter
    if ((random_point[0] - center[0])**2 + (random_point[1] - center[1])**2 > radius**2):
        return False
    else:
        return True
    

def euclid_gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor of two integers using Euclid's algorithm.

    Args:
        a: A positive integer.
        b: A positive integer.
    Returns:
        The greatest common divisor of a and b.
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Write your improved relatively_prime() function here. Use euclid_gcd!
def relatively_prime(a: int, b: int) -> bool:
    """
    Check if a and b are relatively prime. 
    
    Two positive integers are called relatively prime (also called coprime) if 
    they do not share any divisors other than 1. 

    Args:
    - a (int): an integer
    - b (int): an integer

    Returns:
    bool: True if a and b are relatively prime, False otherwise
    """
    return euclid_gcd(a, b) == 1

# Write your relatively_prime_probability() function here along with any subroutines that you need
# Hint: include your relatively_prime() function and any subroutines that it calls.
def relatively_prime_probability_v1(
    lower_bound: int,
    upper_bound: int,
    num_pairs: int) -> float:    
    """
    Compute the probability that two randomly chosen integers in the range [lower_bound,upper_bound]     are relatively prime.

    Parameters:
    - lower_bound (int): the lower bound of the range
    - upper_bound (int): the upper bound of the range
    - num_pairs (int): the number of pairs to trial

    Args:
    float: the probability that two randomly chosen integers in the range [lower_bound, upper_bound]     are relatively prime
    """
    
    count_rel_prime_pairs = 0 

    # loop num_pairs times and check if the two random numbers generated are relatively prime
    for _ in range(num_pairs):
        rand_int_1 = random.randint(lower_bound, upper_bound)
        rand_int_2 = random.randint(lower_bound, upper_bound)
        if relatively_prime(rand_int_1, rand_int_2):
            count_rel_prime_pairs += 1

    return count_rel_prime_pairs/num_pairs

def exercise_6_2_3():
    # return relatively_prime_probability_v1(1, 1_000_000_000_000, 1_000_000_000)
    return relatively_prime_probability_v2(1, 1_000_000_000_000, 1_000_000_000)

def relatively_prime_probability_v2(
    lower_bound: int,
    upper_bound: int,
    num_pairs: int,
    seed : int = 42) -> float:    
    """
    Compute the probability that two randomly chosen integers in the range [lower_bound,upper_bound]     are relatively prime.
   BUT USE NUMPY FOR SPEED
    Parameters:
    - lower_bound (int): the lower bound of the range
    - upper_bound (int): the upper bound of the range
    - num_pairs (int): the number of pairs to trial

    Args:
    float: the probability that two randomly chosen integers in the range [lower_bound, upper_bound]     are relatively prime
    """

    rng = np.random.default_rng(seed)

    r_ints = rng.integers(
        low = lower_bound, 
        high = upper_bound, 
        size = (num_pairs, 2), 
        endpoint = True
    )

    gcds = np.gcd.reduce(r_ints, axis = 1)
    # print(r_ints)
    # print(gcds)
    return np.mean(gcds == 1)

# Write your has_repeat() function here along with any subroutines that you need
def has_repeat_v1(a: list[int]) -> bool:
    """
    Check if a list has repeat elements.

    Args:
    - a: a list of integers

    Returns:
    bool: True if a has repeat elements, False otherwise
    """
    return len(a) != len(set(a))
    
def has_repeat_v2(a: list[int]) -> bool:
    """
    Check if a list has repeat elements.

    Args:
    - a: a list of integers

    Returns:
    bool: True if a has repeat elements, False otherwise
    """
    repeat_vals = set()
    for val in a:
        if val in repeat_vals:
            return True
        repeat_vals.add(val)
    return False

def simulate_one_birthday_trial_v1(num_people: int, rng = np.random.default_rng(), debug: bool = False) -> bool:
    """
    Simulate one trial of the birthday game with num_people people. USING numpy FOR SPEED

    Args:
    - num_people (int): the number of people in the group

    Returns:
    bool: True if there is a collision, False otherwise
    """
    # rng = np.random.default_rng(seed)
    birthdays = rng.integers(low = 1, high = 366, size = num_people, endpoint = False)
    _, uniq_counts = np.unique(birthdays, return_counts = True)
    if debug == True:
        birthdays = np.append(birthdays, birthdays[0])
        _, uniq_counts = np.unique(birthdays, return_counts = True)
        print(f"birthdays = {birthdays}")
        print(f"uniq_counts = {uniq_counts}")  
    return uniq_counts.max() > 1

def simulate_one_birthday_trial_v2(num_people: int, seed: int = 42, debug: bool = False) -> bool:
    """
    Simulate one trial of the birthday game with num_people people. USING random

    Args:
    - num_people (int): the number of people in the group

    Returns:
    bool: True if there is a collision, False otherwise
    """
    if num_people <= 1:
        return True

    birthdays = [random.randint(1, 366) for _ in range(num_people)]

    if debug == True:
        birthdays.append(birthdays[0])
        print(f"birthdays = {birthdays}")
    
    return has_repeat_v2(birthdays)

def simulate_one_birthday_trial_v3(num_people: int, seed: int = 42, debug: bool = False) -> bool:
    """
    Simulate one trial of the birthday game with num_people people. USING numpy FOR SPEED, but 
    only using older functions since im not sure what version of numpy Cogniterra has

    Args:
    - num_people (int): the number of people in the group

    Returns:
    bool: True if there is a collision, False otherwise
    """
    
    np.random.seed(seed)
    birthdays = np.random.randint(low = 1, high = 366, size = num_people)
    # rng = np.random.default_rng(seed)
    # birthdays = rng.integers(low = 1, high = 366, size = num_people, endpoint = False)
    # _, uniq_counts = np.unique(birthdays, return_counts = True)
    uniq_vals = np.unique(birthdays)
    if debug == True:
        birthdays = np.append(birthdays, birthdays[0])
        print(f"birthdays = {birthdays}")

        uniq_vals = np.unique(birthdays)
        print(f"uniq_vals = {uniq_vals}")
        # print(f"uniq_counts = {uniq_counts}")  
    return len(uniq_vals) < num_people

def test_simulate_one_birthday_trial_v1():
    print("----------")
    print("Testing simulate_one_birthday_trial_v1(23) = ", simulate_one_birthday_trial_v1(23, debug=True))

def test_simulate_one_birthday_trial_v2():
    print("----------")
    print("Testing simulate_one_birthday_trial_v2(23) = ", simulate_one_birthday_trial_v2(23, debug=True))

def test_simulate_one_birthday_trial_v3():
    print("----------")
    print("Testing simulate_one_birthday_trial_v3(23) = ", simulate_one_birthday_trial_v3(23, debug=True))

# Write your shared_birthday_probability() function here along with any subroutines that you need
def shared_birthday_probability_v2(num_people: int, num_trials: int) -> float:
    """
    Compute the probability that two people in a group of num_people have the same birthday, after running
    num_trials trials.

    Args:
    - num_people (int): the number of people in the group
    - num_trials (int): the number of trials to run

    Returns:
    float: the average probability that two people in a group of num_people have the same birthday
    """
    list_shared_birthdays = [simulate_one_birthday_trial_v1(num_people) for _ in range(num_trials)]
    return sum(list_shared_birthdays)/num_trials

def shared_birthday_probability_v1(num_people: int, num_trials: int, rng = np.random.default_rng()) -> float:
    """
    Compute the probability that two people in a group of num_people have the same birthday, after running
    num_trials trials. using numpy for speed!

    Args:
    - num_people (int): the number of people in the group
    - num_trials (int): the number of trials to run

    Returns:
    float: the average probability that two people in a group of num_people have the same birthday
    """

    # generate a num_trials by num_people array of random integers between 1 and 366
    # each row is a trial, with num_people in it
    birthdays = rng.integers(1, 366, size=(num_trials, num_people))

    # sort the birthdays in each row (so axis = 1 means arrange the second axis, num_people, i.e. the columns)
    sorted_birthdays = np.sort(birthdays, axis=1)

    # for each row, check if there are any pairs of birthdays that are the same. np.diff() calculates
    # "The first difference... by out[i] = a[i+1] - a[i] along the given axis"
    # so if there are any pairs of birthdays that are the same, then np.diff() will be 0
    # then if we check if any of the differences are 0, then we know that there are any pairs of birthdays that are the same
    results = np.any(
        np.diff(sorted_birthdays, axis=1) == 0, 
        axis=1
    )
    # print(f"birthdays = {birthdays}")
    # print(f"sorted_birthdays = {sorted_birthdays}")
    # print(f"results = {results}")
    return np.mean(results)

def test_shared_birthday_probability_v1():
    print("----------")
    print("Testing shared_birthday_probability_v1(23, 100) = ", shared_birthday_probability_v1(23, 100))

def exercise_6_3_4():
    print("----------")
    for num_people in range(1, 100):
        probability = shared_birthday_probability_v1(num_people, 1_000_000)
        print(f"num_people = {num_people}, probability = {probability}")
        if probability > 0.5:
            print(f"num_people = {num_people}, probability = {probability}")
            break

def count_num_digits(x: int) -> int:
    """
    Count the number of digits in an integer x.

    Args:
    - x (int): an integer

    Returns:
    int: the number of digits in x
    """
    # return len(str(x))
    if x == 0:
        return 1

    if x < 0:
        x = -x

    count = 0
    # remove one digit at a time by dividing by 10
    while x > 0:
        print(f"x = {x}, count = {count}")
        x = x // 10
        count += 1
    print(f"x = {x}, count = {count}")
    return count

# Write your square_middle() function here along with any subroutines that you need.
def square_middle(x: int, num_digits: int) -> int:
    """
    Get the middle digits of x squared.

    Args:
    - x (int): a positive integer
    - num_digits (int): the number of digits in the middle of x squared to return

    Returns:
    int: the middle digits of x squared

    Note: Returns the result of squaring x and taking the "middle" numDigits digits in the resulting number that has 2 · numDigits total digits. You should add zeroes to the start of the number if needed so that it has 2 · numDigits total digits. Furthermore, your function should return -1 if numDigits is odd, if x is negative, if numDigits is not positive, or if the number of digits in x is greater than numDigits.
    """

    if num_digits % 2 != 0 or x < 0 or num_digits < 1 or len(str(x)) > num_digits:
        return -1
    
    square_x = x**2
    string_square_x = str(square_x)

    # if the result of squaring x has less than 2*num_digits digits, 
    # prepend zeroes such that it has length 2*num_digits
    if len(string_square_x) < 2*num_digits:
        string_square_x = "0"*(2*num_digits - len(string_square_x)) + string_square_x
    
    # print(f"string_square_x = {string_square_x}")
    # we know that the number of digits in string_square_x is 2*num_digits. we want to take off
    # num_digits//2 from either side of the string thus,
    # start index is the length of the string divided minus num_digits, all divided by 2
    # and the end index is the start index plus num_digits
    start_idx = (len(string_square_x) - num_digits)//2
    end_idx = start_idx + num_digits
    return int(string_square_x[start_idx : end_idx])

# Write your generate_middle_square_sequence() function here along with any subroutines that you need.
def generate_middle_square_sequence(seed: int, num_digits: int) -> list[int]:
    """
    Generate a middle square sequence.

    Args:
    - seed (int): the first value in the sequence
    - num_digits (int): the number of digits in the middle of each squared value to add to the sequence

    Returns:
    list: a middle-square sequence
    """
    seen_vals = set([seed])
    sequence = [seed]
    cur_idx = 0
    next_val = square_middle(sequence[cur_idx], num_digits)
    while next_val not in seen_vals:
        sequence.append(next_val)
        seen_vals.add(next_val)
        next_val = square_middle(sequence[cur_idx+1], num_digits)
        cur_idx += 1
    sequence.append(next_val)

    return sequence

# Write your compute_period_length() function here along with any subroutines that you need
def compute_period_length(a: list[int]) -> int:
    """
    Compute the period length of a list of integers.

    Args:
    - a: a list of integers

    Returns:
    int: the length of the period of a
    """
    # seen vals is a dictionary mapping a given value from a (a_i) to it's first occurence
    seen_vals = {}
    for i, a_i in enumerate(a):
        if a_i not in seen_vals:
            seen_vals[a_i] = i
        else:
            break
    return i - seen_vals[a_i]

def exercise_6_4_5():
    """
    Exercise (ungraded): Call GenerateMiddleSquareSequence() on your computer for every four-digit seed between 1 and 9999. How many seeds produce a sequence having period equal to 10 or smaller?

    Note: This question is really asking, "Is the Middle-Square approach a good PRNG?"
    """
    count = 0
    for seed in range(1, 10000):
        if compute_period_length(generate_middle_square_sequence(seed, 4)) <= 10:
            count += 1
    return count

def generate_linear_congruence_sequence(seed: int, a: int, c: int, m: int) -> list[int]:
    """
    Generate a linear congruence sequence.

    Args:
    - seed (int): the first value in the sequence
    - a (int): the multiplier
    - c (int): the increment
    - m (int): the modulus

    Returns:
    list: a sequence of integers produced by the linear congruential generator
    """
    seen_vals = set([seed])
    sequence = [seed]
    cur_idx = 0
    next_val = get_next_LCG_val(sequence[cur_idx], a, c, m)
    while next_val not in seen_vals:
        sequence.append(next_val)
        seen_vals.add(next_val)
        next_val = get_next_LCG_val(sequence[cur_idx+1],  a, c, m)
        cur_idx += 1
    sequence.append(next_val)

    return sequence

def get_next_LCG_val(x_n, a, c, m):
    """
    https://en.wikipedia.org/wiki/Linear_congruential_generator
    """
    return (a*x_n + c) % m

def exercise_6_5_2():
    """
    Exercise (ungraded): Let a = 5, c = 1, and m = 2^13 = 8192. 
    hat is the period of the linear congruential generator when the seed is equal to 1? 
    (What can we conclude about the period of every seed between 1 and m− 1?)

    Answer: 8192. I'm guessing the period is equal to m?
    """
    print("-------")
    m = 2**14
    print(f"m = {m}")
    return compute_period_length(generate_linear_congruence_sequence(1, a = 5, c = 1, m = m))


if __name__ == "__main__":
    main()