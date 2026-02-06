import random
import time

def main():
    print("pseudo random numbers module! Rolling dice and playing craps.")

    # 2 most important functions for pseudo random number generation (PRNG)
    # random.randrange(a,b): generates a pseudo random number between a and b-1 inclusively
    # random.random(): generates a pseudo random uniform float in [0,1]

    print("uncontrolled seed PRNG")
    for _ in range(0,5):
        print("\t", random.randrange(0, 10))
        print("\t", random.random())

    random.seed(0) # establishes the start of the PRNG process
    print("controlled seed PRNG")
    for _ in range(0,5):
        print("\t", random.randrange(0, 10))
        print("\t", random.random())

    # seeding the PRNG allows us to "control" the randomness.
    # random.seed(time.time_ns()) establishes the start of the number generation process with a 
    # seed based on our initial time. python does something like this when we dont choose a seed

    print("rolling a die with a PRNG seeded by current time")
    random.seed(time.time_ns())
    for _ in range(0,5):
        print("\t", roll_die())

    print("Simulate playing craps 10 times manually")
    for _ in range(10):
        outcome = play_craps_once()
        if outcome == True:
            outcome = "Win!"
        else:
            outcome = "Loss..."
        print(f"\tresult of play_craps_once() = {outcome}")

    num_trials = 1_000_000
    # NEGATIVE IT TO MAKE IT FROM THE HOUSE'S PERSPECTIVE (currently we are calculating from the player's perspective)
    edge = -compute_craps_house_edge(num_trials=num_trials)
    print(f"Esimtated average house edge with {num_trials} trials is: {edge:.6f}")

    print(f"\nThat's about {edge*100:.3f}% of the amount wagered per bet")

def sum_dice(n: int) -> int:
    """
    Simulates the rolling of n dice. See https://andymath.com/probability-with-dice/

    :return: a pseudo random integer in range [2,12] corresponding to simulating the roll of two six-sided dice.
    :rtype: int
    """

    return sum([roll_die() for _ in range(0,n)])


def compute_craps_house_edge(num_trials: int) -> float:
    """
    Determine the house edge of a dice game of craps for num_trials trials.
    
    :param num_trials: number of times to simulate
    :type num_trials: int
    :return: house edge, averaged over num_trials trials, where we wager a single unit of currency each time
    :rtype: float
    """

    if num_trials <= 0:
        raise ValueError("Error: non-positive number of trials given")
    
    # first glimpse at monte carlo simulation: generate a large number of ranomdized trials to make an estimate of
    # a simulation

    total_wins = 0
    for _ in range(num_trials):
        # play the game, did we win (true) or lose (false)
        total_wins += play_craps_once() # True or False, Python maps True to 1 and False to 0 for arithmetic

    total_losses = num_trials - total_wins

    count = total_wins - total_losses # amount won (positive) or lost (negative) from player's perspective

    return count/num_trials

def play_craps_once() -> bool:
    """
    Simulates the process of playing craps one time, returning True for a win and False otherwise
    
    :return: result of playing craps game once. True is win, False is loss.
    :rtype: bool
    """

    # roll two dice to give a sum x.
    first_roll = sum_dice(2)

    # case 1: did we win?
    if first_roll == 7 or first_roll == 11:
        return True
    
    # case 2:  did we lose immediately?
    if first_roll == 2 or first_roll == 3 or first_roll == 12:
        return False
    
    # case 3: we rolled something else, so we keep rolling until we either roll the original number (win) or
    # we roll 7 (loss)
    new_roll = sum_dice(2)
    while new_roll != first_roll and new_roll != 7:
        new_roll = sum_dice(2)
    
    if new_roll == first_roll:
        return True
    else:
        return False

def sum_two_dice() -> int:
    """
    Simulates the rolling of two dice. See https://andymath.com/probability-with-dice/

    :return: a pseudo random integer in range [2,12] corresponding to simulating the roll of two six-sided dice.
    :rtype: int
    """
    # v1 using roll_die()
    return roll_die() + roll_die()


    # # v2 using random.random() and mapping to interval
    # roll = random.random() # between 0 and 1
    # if roll < 1.0/36.0: # 1 way to get 2
    #     return 2
    # elif roll < 2.0/36.0: # 2 ways to get 3
    #     return 3
    # elif roll < 3.0/36.0: # 3 ways to get 4
    #     return 4
    # # etc.
    # # NOTE: any time we have a probabilistic process where we know the probability of each outcome,
    # # the probabilities of the sample space must sum to 1 so we know that generating a number between [0,1) can help us
    # # map unto any probabilistic scenario. Practically, this means we can divide up the interval [0,1) proportionally
    # # based on how likely each event is, then choose a number between [0,1) and then select the event based on where 
    # # the PRN fell in the interval. e.g. we know 4/12 chance of snow, 3/12 chance of rain, and 5/12 chance of sun for
    # # the weather of the past week. We can generate a PRN in [0,1) like so: 
    # #   PRN = random.random()
    # #   if PRN < 4/12 then snow, 
    # #   else if 4/12 <= PRN < 4/12 + 3/12 then rain,
    # #   else 4/12 + 3/12 <= prn

def roll_die() -> int:
    """
    
    :return: a pseudo random integer in range [1,6]
    :rtype: int
    """
    return random.randrange(1,7)

if __name__ == "__main__":
    main()