import sys

def main():
    print("HW1")
    exercise_4_2_7()
    exercise_4_2_8()

# Please do not remove package declarations because these are used by the autograder. If you need additional packages, then you may declare them above.

# Insert your richness() function here, along with any subroutines that you need.
def richness(sample: dict[str, int]) -> int:
    """
    Compute the richness of a frequency table.

    Args:
        sample: A frequency table mapping strings to occurrence counts.
    Returns:
        The richness of the sample.
    """
    # print(sample.keys())
    count = 0
    for cur_key in sample.keys():
        if sample[cur_key] > 0:
            count += 1
    return count

# Insert your sum_of_values() function here.
def sum_of_values(sample: dict[str, int]) -> int:
    """
    Compute the sum of values in a frequency table.

    Args:
        sample: A frequency table mapping strings to integers.
    Returns:
        The sum of all values in the frequency table.
    """
    return sum(sample.values())

# Insert your simpsons_index() function here, along with any subroutines that you need.
def simpsons_index(sample: dict[str, int]) -> float:
    """
    Compute Simpson's index of a frequency table.

    Args:
        sample: A frequency table mapping strings to integers.
    Returns:
        The Simpson's index of the sample.
    """
    total_num_objects = sum_of_values(sample)

    return sum([(cur_object/total_num_objects)**2 for cur_object in sample.values()])

def exercise_4_2_7():
    sum_minima = 1 + 500
    average_totals = (1000 + 1000)/2
    print(1 - sum_minima/average_totals)

def exercise_4_2_8():
    sum_maxima = 500 + 999
    sum_minima = 1 + 500
    print(1- sum_minima/sum_maxima)

# Insert your sum_of_minima() function here, along with any subroutines that you need.
def sum_of_minima(sample1: dict[str, int], sample2: dict[str, int]) -> int:
    """
    Compute the sum of corresponding minimum values of two frequency tables.

    Args:
        sample1: A frequency table mapping strings to integers.
        sample2: A frequency table mapping strings to integers.
    Returns:
        The sum of the minimum values for each string appearing in both samples.
    """
    # range over all the species in sample1 and see how many (if any) are in sample 2
    # NOTE: since we want minima, we will only need to check one side, because if it's in sample2 but not
    # sample1, then sample1 would return 0
    cumulative_sum_of_minima = 0
    for species_i_sample1, num_species_i_sample1 in sample1.items():
        num_species_i_sample2 = sample2.get(species_i_sample1, 0)
        min_val = min2(num_species_i_sample1, num_species_i_sample2)
        cumulative_sum_of_minima += min_val
    return cumulative_sum_of_minima

# Note: for the sake of convenience, we are providing a min2() function below.
def min2(x: int, y: int) -> int:
    """
    Return the minimum of two integers.

    Args:
        x: An integer.
        y: An integer.
    Returns:
        The smaller of x and y.
    """
    if x < y:
        return x
    return y

# Insert your bray_curtis_distance() function here, along with any subroutines that you need.
def bray_curtis_distance(sample1: dict[str, int], sample2: dict[str, int]) -> float:
    """
    Compute the Bray-Curtis distance between two frequency tables.

    Args:
        sample1: A frequency table mapping strings to integers.
        sample2: A frequency table mapping strings to integers.
    Returns:
        The Bray-Curtis distance between the two samples.
    """
    return 1 - sum_of_minima(sample1, sample2)/average_totals(sample1, sample2)

def average(*some_iterable):
    return sum(some_iterable)/len(some_iterable)

def average_totals(sample1, sample2):
    return average((sample1, sample2))

# Insert your sum_of_maxima() function here.
def sum_of_maxima(sample1: dict[str, int], sample2: dict[str, int]) -> int:
    """
    Compute the sum of corresponding maximum values of two frequency tables.

    Args:
        sample1: A frequency table mapping strings to integers.
        sample2: A frequency table mapping strings to integers.
    Returns:
        The sum of the maximum values for each string appearing in either sample.
    """
    # range over all the species in sample1 and see how many (if any) are in sample2
    # NOTE: since we want maxima, we will need to check both of them since sample2 could
    # have a species that sample1 does not have

    # let's get a list of all UNIQUE species using set notation and list appending for convenience
    set_all_species = set(list(sample1.keys()) + list(sample2.keys()))

    cumulative_sum_of_maxima = 0
    for species_i in set_all_species:
        num_species_i_sample1 = sample1.get(species_i, 0)
        num_species_i_sample2 = sample2.get(species_i, 0)
        max_val = max2(num_species_i_sample1, num_species_i_sample2)
        cumulative_sum_of_maxima += max_val
    return cumulative_sum_of_maxima

# Note: for the sake of convenience, we are providing a max2() function below.
def max2(x: int, y: int) -> int:
    """
    Return the maximum of two integers.

    Args:
        x: An integer.
        y: An integer.
    Returns:
        The larger of x and y.
    """
    if x > y:
        return x
    return y

# Insert your jaccard_distance() function here, along with any subroutines that you need.
def jaccard_distance(sample1: dict[str, int], sample2: dict[str, int]) -> float:
    """
    Compute the Jaccard distance between two frequency tables.

    Args:
        sample1: A frequency table mapping strings to integers.
        sample2: A frequency table mapping strings to integers.
    Returns:
        The Jaccard distance between the two samples.
    """
    return 1 - sum_of_minima(sample1, sample2)/sum_of_maxima(sample1, sample2) 

if __name__ == "__main__":
    main()