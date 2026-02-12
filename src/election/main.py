from election_io import read_electoral_votes, read_polling_data
import random
import sys

sys.stdout = open("output.txt", "w")

def main() :
    print("Simulating an election!")
    electoral_vote_file = "data/electoralVotes.csv"
    poll_file = "data/earlyPolls.csv"
    electoral_votes = read_electoral_votes(electoral_vote_file)
    polls = read_polling_data(poll_file)

    print("Files read successfully!")
    # print("electoral_votes:\n", electoral_votes)
    # print("polls:\n", polls)

    # simulation v1
    num_trials = 1_000_000
    margin_of_error = 0.05

    probability_1, probability_2, probability_tie = simulate_multiple_elections(
        polls = polls, 
        electoral_votes = electoral_votes, 
        num_trials = num_trials, 
        margin_of_error = margin_of_error
    )

    print(f"v1 Simulation of early polls complete for num_trials = {num_trials}, margin_of_error = {margin_of_error}")
    print(f"Probability of candidate 1 winning: {probability_1}")
    print(f"Probability of candidate 2 winning: {probability_2}")
    print(f"Probability of tie: {probability_tie}")
    print("------")

   # simulation v2
    num_trials = 1_000_000
    margin_of_error = 0.1

    probability_1, probability_2, probability_tie = simulate_multiple_elections(
        polls = polls, 
        electoral_votes = electoral_votes, 
        num_trials = num_trials, 
        margin_of_error = margin_of_error
    )

    print(f"v2 Simulation of early polls complete for num_trials = {num_trials}, margin_of_error = {margin_of_error}")
    print(f"Probability of candidate 1 winning: {probability_1}")
    print(f"Probability of candidate 2 winning: {probability_2}")
    print(f"Probability of tie: {probability_tie}")
    print("------")

   # simulation v3
    poll_file = "data/conventions.csv"
    polls = read_polling_data(poll_file)

    num_trials = 1_000_000
    margin_of_error = 0.05

    probability_1, probability_2, probability_tie = simulate_multiple_elections(
        polls = polls, 
        electoral_votes = electoral_votes, 
        num_trials = num_trials, 
        margin_of_error = margin_of_error
    )

    print(f"v3 Simulation after convention (later time) complete for num_trials = {num_trials}, margin_of_error = {margin_of_error}")
    print(f"Probability of candidate 1 winning: {probability_1}")
    print(f"Probability of candidate 2 winning: {probability_2}")
    print(f"Probability of tie: {probability_tie}")
    print("------")

   # simulation v4
    poll_file = "data/debates.csv"
    polls = read_polling_data(poll_file)

    num_trials = 1_000_000
    margin_of_error = 0.05

    probability_1, probability_2, probability_tie = simulate_multiple_elections(
        polls = polls, 
        electoral_votes = electoral_votes, 
        num_trials = num_trials, 
        margin_of_error = margin_of_error
    )

    print(f"v4 Simulation after debates (latest time) complete for num_trials = {num_trials}, margin_of_error = {margin_of_error}")
    print(f"Probability of candidate 1 winning: {probability_1}")
    print(f"Probability of candidate 2 winning: {probability_2}")
    print(f"Probability of tie: {probability_tie}")
    print("------")

def simulate_multiple_elections(
    polls: dict[str, float],
    electoral_votes: dict[str, int],
    num_trials: int,
    margin_of_error: float,
) -> tuple[float, float, float]:
    """
    Simulates multiple elections and calculates winning probabilities.

    Parameters:
    - polls (dict[str, float]): A dictionary of state names to polling percentages for candidate 1.
    - electoral_votes (dict[str, int]): A dictionary of state names to electoral votes.
    - num_trials (int): The number of trials to run.
    - margin_of_error (float): The margin of error in the polls.

    Returns:
    - tuple[float, float, float]: The estimated probabilities of candidate 1 winning,
      candidate 2 winning, and a tie.
    """

    if num_trials <= 0:
        raise ValueError("num_trials must be positive.")
    if margin_of_error < 0:
        raise ValueError("margin_of_error must be non-negative.")

    win_count_1 = 0
    win_count_2 = 0
    tie_count = 0
    # these hold number of wins for each outcome; what we want is ratio of these counts to the total
    for _ in range(num_trials):
        # run an individual simulation
       votes_1, votes_2 = simulate_one_election(
            polls = polls, 
            electoral_votes = electoral_votes, 
            margin_of_error = margin_of_error
        )
       
       # who won?
       if votes_1 > votes_2:
            win_count_1 += 1 
       elif votes_2 > votes_1:
            win_count_2 += 1
       else:
           tie_count += 1


    probability_1 = win_count_1/num_trials
    probability_2 = win_count_2/num_trials
    probability_tie = tie_count/num_trials
    return probability_1, probability_2, probability_tie

def simulate_one_election(
    polls: dict[str, float],
    electoral_votes: dict[str, int],
    margin_of_error: float
) -> tuple[int, int]:
    """
    Simulates one election and calculates electoral college votes for each candidate.

    Parameters:
    - polls (dict[str, float]): A dictionary of state names to polling percentages for candidate 1.
    - electoral_votes (dict[str, int]): A dictionary of state names to electoral votes.
    - margin_of_error (float): The margin of error in the polls.

    Returns:
    - tuple[int, int]: The number of electoral college votes for each of the two candidates.
    """
    # basic checks
    if margin_of_error < 0:
        raise ValueError("margin_of_error must be non-negative.")
    
    college_votes_1 = 0
    college_votes_2 = 0

    # range over all states and simulate each one
    for state, polling_value in polls.items():
        # access the number of EC votes in this state
        num_votes = electoral_votes[state]

        # where is the randomness?
        adjusted_poll = add_noise(polling_value = polling_value, margin_of_error = margin_of_error)

        # as a result, which candidate wins?
        if adjusted_poll >= 0.5:
            college_votes_1 += num_votes
        else:
            college_votes_2 += num_votes

    return college_votes_1, college_votes_2

def add_noise(polling_value: float, margin_of_error: float) -> float:
    """
    Adds random noise to a polling value.

    Parameters:
    - polling_value (float): The polling value for candidate 1.
    - margin_of_error (float): The margin of error.

    Returns:
    - float: An adjusted polling value for candidate 1 after adding random noise.
    """
    if margin_of_error < 0 or polling_value < 0 or polling_value > 1:
        raise ValueError("Invalid polling value or margin of error.")

    # margin_of_error is the value y such that there is a 95% chacne of the true value being in the range 
    # [polling_value - y, polling_value + y]

    # a pseudo random number (PRN) from the standard normal dist has a 95% chance of being in [-2, 2]
    x = random.gauss(0, 1) # gives a normal distribution with a mean of 0, and std dev 1 (std normal)
    x /= 2.0 # now it's 95% chance of being in [1,1]
    x *= margin_of_error # now it's a 95% chance of being in [-margin_of_error, +margin_of_oerror]

    # to get the range we desired, add polling_value and it will have a 95% chance of being in 
    # [polling_value - moe, polling_value + moe]
    return polling_value + x

if __name__ == "__main__":
	main()

# close the stdout redirection!
sys.stdout.close()
