def main():
    print("Dictionaries in Python")

    polls: dict[str, float] = {}
    polls["PA"] = 0.517
    polls["OH"] = 0.488
    polls["TX"] = 0.378
    polls["FL"] = 0.5 # swing state
    print(f"polls = {polls}")

    print(f"Number of elements in polls = {len(polls)}")

    try:
        print("Let's get the polls of VA", polls["VA"])
    except KeyError as e:
        print(e)

    # let's get rid of FL, if it's in the dict
    if "FL" in polls:
        del polls["FL"]
    print(f"polls = {polls}")

    # why do we need lists if we have dicts? dict seems more flexible and easier to worth with
    primes = {}
    primes[0] = 2
    primes[1] = 3
    primes[2] = 5
    # etc.
    # DONT DO THIS, THIS IS REALLY BAD. a list is much more efficient. if we have a defined 
    # order, use lists

    # create a small list literal
    primes = [2, 3, 5, 7, 11]

    # dictionary literal
    electoral_votes: dict[str, int] = {
        "PA": 20,
        "OH": 18,
        "TX": 38
    }

    # dictionaries are call by object reference (like pass by reference)
    update_votes_2024(electoral_votes)

    print(f"As of 2024 the number of votes in PA is {electoral_votes["PA"]}")
    print("Passing a dictionary passes the reference to the dict")

    # ranging over dictionaries, v1
    print("range over dict v1:")
    # this ranges over the keys, in the order they were added to dictionary
    for key in electoral_votes:
        print("    Number of votes in", key, "is", electoral_votes[key])

    # ranging over dictionaries, v2
    print("range over dict v2:")
    for key, num_votes in electoral_votes.items():
        print("    Number of votes in", key, "is", num_votes)

    # # ranging over keys alphabetically, v1
    # keys = list(electoral_votes.keys())
    # print(keys)

    # # sort the keys alphabetically
    # keys.sort()
    # print(keys)

    # # range over the states alphabetically
    # for state_name in keys:
    #     print(f"Num of electoral votes in {state_name} is {electoral_votes[state_name]}")

    # ranging over keys alphabetically, v2. NOTE: sorted() works for numbers too
    print("range over dict v3, alphabetically")
    # python has a faster approach
    for state_name in sorted(electoral_votes):
        print(f"    Num of electoral votes in {state_name} is {electoral_votes[state_name]}")

    # we can get the values with dict.values()
    total_votes = 0
    for num_votes in electoral_votes.values():
        total_votes += num_votes
    print(f"total_votes={total_votes}")


def update_votes_2024(votes: dict[str, int]) -> None:
    """
    Updates electoral college votes from 2020 to 2024
    
    :param votes: maps states to votes
    :type votes: dict[str, int]
    :return: None
    :rtype: None
    """
    votes["PA"] = 19
    votes["OH"] = 17
    votes["TX"] = 40

def complement(dna: str) -> str:
    """
    complement function that uses dictionary instead of a switch/match statement or if else
    
    :param dna: Description
    :type dna: str
    :return: Description
    :rtype: str
    """

    comp_dict: dict[str, str] = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    dna2 = ""

    for symbol in dna:
        dna2 += comp_dict[symbol]

    return dna2

if __name__ == "__main__":
    main()