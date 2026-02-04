from helper import frequency_table
import requests
# from copy import deepcopy

def main():
    print("Finding clumps!")
    text = "AAAACGCTAAAAA"
    k = 2
    window_length = 4
    t = 2
    clumps = find_clumps_v1(text, k, window_length, t)
    print(clumps)
    
    # let's get a real genome!
    url = "https://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt"
    response = requests.get(url)
    genome_e_coli = response.text # accessses tge string from the response

    # check - was everything OK?
    response.raise_for_status() # error if anything went wrong
    assert len(genome_e_coli) == 4639675, f"len(genome_e_coli) = {genome_e_coli}, expected 4639675"
    
    
    
    k = 9
    window_length = 500
    t = 3
    # clumps_e_coli = find_clumps_v1(genome_e_coli, k, window_length, t)
    print("Using find_clumps_v2...")
    # clumps_e_coli, freq_map_window_1_v2 = find_clumps_v2(genome_e_coli, k, window_length, t)
    clumps_e_coli = find_clumps_v2(genome_e_coli, k, window_length, t)
    
    print(".    We have", len(clumps_e_coli), "total clumps")
    # print(freq_map_window_1_v2)

    print("Using find_clumps_v3...")
    # clumps_e_coli, freq_map_window_1_v3 = find_clumps_v3(genome_e_coli, k, window_length, t)
    clumps_e_coli = find_clumps_v3(genome_e_coli, k, window_length, t)
    print(".    We have", len(clumps_e_coli), "total clumps")
    # print(freq_map_window_1_v3)
    # print(freq_map_window_1_v2 == freq_map_window_1_v3)

def find_clumps_v3(text: str, k: int, window_length: int, t: int) -> list[str]:
    """
    Finds all the substrings of a given length (k) in a longer string (text) that occur 
    more than some threshold (t) number of times within a short region (window_length).
    We improve on find_clumps_v2 by using Python's set() for ignoring duplicates.
    
    :param text: longer string being searched
    :type text: str
    :param k: substring (k-mer) length
    :type k: int
    :param window_length: size of short region in which threshold for count of substring must be met
    :type window_length: int
    :param t: threshold for count of substring
    :type t: int
    :return:
    :rtype: list[str]
    """
    # example
    # text = "BANANASPLIT"
    # window_length = 6
    # k = 3

    # frequency table of first window
    # BAN 1
    # ANA 2
    # NAN 1

    # frequency table of second window ()
    # ANA 2
    # NAN 1
    # NAS 1
    # NOTE: we lose 1 k-mer and gain 1!

    # what do we need to check in terms of errors:
    if k <= 0 or window_length <= 0 or t <= 0:
        raise ValueError(f"Error: expected positive value of parameters, got k = {k}, window_length = {window_length}, t = {t}")
    
    if len(text) == 0:
        raise ValueError("Error: empty string given for text.")
    
    if k > window_length:
        raise ValueError("Error: k must be less than window_length")

    if k > len(text):
        return [] # no solution possible if k longer than len(text)

    # sets in python are unordered, mutable, and dont allow duplicates
    patterns: set[str] = set()
    n: int = len(text)
    first_window = text[:window_length]
    freq_map = frequency_table(first_window, k)

    # freq_map_window_1 = deepcopy(freq_map)

    # what occurs frequently (more than or equal to t times)
    for s, val in freq_map.items():
        # make sure val >= t AND that I haven't added s to patterns

        if val >= t: # i found a "clump"
            patterns.add(s)


    # we need to range over all REMAINING windows in the text
    for i in range(1, n - window_length + 1):

        # what is the pattern that "exited"?
        old_pattern = text[i-1 : i-1+k]

        # what is the pattern that "entered" the window?
        new_pattern = text[i+window_length-k : i+window_length]

        # let's update the frequency map
        freq_map[old_pattern] -= 1
        if freq_map[old_pattern] == 0: # remove from the map
            del freq_map[old_pattern]

        # add the pattern from the end of the current window
        freq_map[new_pattern] = freq_map.get(new_pattern, 0) + 1

        # now the frequency map is updated!

        # two possibibilities now:
        # (1) it was already frequent in previous map (already identified so dont need to check!)
        # (2) new_pattern all of a sudden is frequent (we need to check new_pattern!)
        if freq_map[new_pattern] >= t:
            patterns.add(new_pattern)

    return list(patterns) # , freq_map_window_1


def find_clumps_v2(text: str, k: int, window_length: int, t: int) -> list[str]:
    """
    Finds all the substrings of a given length (k) in a longer string (text) that occur 
    more than some threshold (t) number of times within a short region (window_length).
    We significantly improve on find_clumps_v1 by noting that the kmer frequency table
    for position i and position i + 1 are very similar... in fact they are exactly the 
    same except 1 instance of a kmer drops off from the front of the window and 1 instance
    of a kmer is added to the end of the window! Example below
    
    :param text: longer string being searched
    :type text: str
    :param k: substring (k-mer) length
    :type k: int
    :param window_length: size of short region in which threshold for count of substring must be met
    :type window_length: int
    :param t: threshold for count of substring
    :type t: int
    :return:
    :rtype: list[str]
    """
    # example
    # text = "BANANASPLIT"
    # window_length = 6
    # k = 3

    # frequency table of first window
    # BAN 1
    # ANA 2
    # NAN 1

    # frequency table of second window ()
    # ANA 2
    # NAN 1
    # NAS 1
    # NOTE: we lose 1 k-mer and gain 1!

    # what do we need to check in terms of errors:
    if k <= 0 or window_length <= 0 or t <= 0:
        raise ValueError(f"Error: expected positive value of parameters, got k = {k}, window_length = {window_length}, t = {t}")
    
    if len(text) == 0:
        raise ValueError("Error: empty string given for text.")
    
    if k > window_length:
        raise ValueError("Error: k must be less than window_length")

    if k > len(text):
        return [] # no solution possible if k longer than len(text)

    patterns: list[str] = []
    n: int = len(text)
    first_window = text[:window_length]
    freq_map = frequency_table(first_window, k)
    # let's declare a dictionary that stores whether or not i have seen each string before at least t times
    found_patterns: dict[str, bool] = {}


    # freq_map_window_1 = deepcopy(freq_map)


    # what occurs frequently (more than or equal to t times)
    for s, val in freq_map.items():
        # make sure val >= t AND that I haven't added s to patterns
        if (val >= t) and found_patterns.get(s, False): # i found a "clump"
            patterns.append(s)
            
            # track that we've found a valid pattern
            found_patterns[s] = True


    # we need to range over all REMAINING windows in the text
    for i in range(1, n - window_length + 1):

        # what is the pattern that "exited"?
        old_pattern = text[i-1 : i-1+k]

        # what is the pattern that "entered" the window?
        # start_idx = i+window_length-k
        # end_idx = i+window_length-k + k
        new_pattern = text[i+window_length-k : i+window_length]

        # let's update the frequency map
        freq_map[old_pattern] -= 1
        if freq_map[old_pattern] == 0: # remove from the map
            del freq_map[old_pattern]

        # add the pattern from the end of the current window
        freq_map[new_pattern] = freq_map.get(new_pattern, 0) + 1

        # now the frequency map is updated!

        # two possibibilities now:
        # (1) it was already frequent in previous map (already identified so dont need to check!)
        # (2) new_pattern all of a sudden is frequent (we need to check new_pattern!)
        is_key = found_patterns.get(new_pattern, False)
        if freq_map[new_pattern] >= t and not is_key:
            patterns.append(new_pattern)
            found_patterns[new_pattern] = True

    return patterns # , freq_map_window_1

def find_clumps_v1(text: str, k: int, window_length: int, t: int) -> list[str]:
    """
    Finds all the substrings of a given length (k) in a longer string (text) that occur 
    more than some threshold (t) number of times within a short region (window_length)
    
    :param text: longer string being searched
    :type text: str
    :param k: substring (k-mer) length
    :type k: int
    :param window_length: size of short region in which threshold for count of substring must be met
    :type window_length: int
    :param t: threshold for count of substring
    :type t: int
    :return:
    :rtype: list[str]
    """

    # what do we need to check in terms of errors:
    if k <= 0 or window_length <= 0 or t <= 0:
        raise ValueError(f"Error: expected positive value of parameters, got k = {k}, window_length = {window_length}, t = {t}")
    
    if len(text) == 0:
        raise ValueError("Error: empty string given for text.")
    
    if k > window_length:
        raise ValueError("Error: k must be less than window_length")

    if k > len(text):
        return [] # no solution possible if k longer than len(text)

    patterns: list[str] = []
    n: int = len(text)

    # we need to range over all windows in the text
    for i in range(0, n - window_length + 1):

        # # debug statement
        # if i % 1000 == 0:
        #     print("Executing i equal to ", i)

        # catalog number of counts of each k-mer in the current window
        current_window = text[i:i + window_length]

        freq_map = frequency_table(current_window, k)

        # patterns = add_new_frequent_strings(freq_map, patterns, t)

        # what occurs frequently (more than or equal to t times)
        for s, val in freq_map.items():
            # make sure val >= t AND that I haven't added s to patterns
            if (val >= t) and (s not in patterns): # i found a "clump"
                patterns.append(s)

    return patterns


if __name__ == "__main__":
    main()