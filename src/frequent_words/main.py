def main() -> None:
    print("Find frequent words")
    print(frequency_table("ABCDABCD", 2))

    text = "ACGTTTTGAGACGTTTACGC"
    k = 3
    print(f"frequency_table(text, k) = frequency_table({text}, {k}) = {frequency_table(text, k)}")

    print(f"frequent_words(text, k) = frequent_words({text}, {k}) = {frequent_words(text, k)}")

def frequent_words(text:str, k:int) -> list[str]:
    """
    Produces all frequent k-mers (substring of length k) in a longer string.

    :param text: some string
    :type text: str
    :param k: some integer 0 < k < n
    :type k: int
    :return: list of strings representing the most frequent k-mers in text.
    :rtype: list[str]
    """

    if k <= 0:
        raise ValueError("Error: non-positive value of k given to function as input")
    
    if k > len(text):
        return []
    
    freq_patterns = []

    # generate the frequency table of text and k
    freq_map = frequency_table(text, k)

    # what's the maximum value in the table?
    max_val = max(freq_map.values())

    # range over frequency table and identify the strings (keys) that achieve the max value. when
    # we find one, append it to freq_patterns
    for pattern, val in freq_map.items():
        if val == max_val:
            freq_patterns.append(pattern)

    return freq_patterns

def frequency_table(text: str, k: int) -> dict[str, int]:
    """
    Generate frequency table mapping k-mer substrings of text to their number of occurences.
    
    :param text: string
    :type text: str
    :param k: integer defining k-mer length
    :type k: int
    :return: keys are substrings of text having length k, values are number of occurences of that string
    :rtype: dict[str, int]
    """

    if k <= 0:
        raise ValueError("Error: non positive value of k given to function as input")
    
    if k > len(text):
        return {}

    freq_table: dict[str, int] = {}


    # # v1, from scratch naive way
    # for i in range(0, len(text) - k + 1):
    #     kmer = text[i:i+k]
    #     # print(kmer)
        
    #     # increment the key if found
    #     if kmer not in freq_table:
    #         freq_table[kmer] = 0
    #     freq_table[kmer] += 1

    # v2, from scratch with get(key, default)
    # PYTHONIC WAY TO SIMULTANEOUSLY CHECK IF KEY IS IN DICT AND RETURN A VALUE IF NOT PRESENT
    for i in range(0, len(text) - k + 1):
        kmer = text[i:i+k]
        # print(kmer)

        # initialize
        freq_table[kmer] = freq_table.get(kmer, 0) + 1

    # # v3, python builtins + list comprehension
    # from collections import Counter
    # def kmers(seq, k):
    #     return [seq[i:i+k] for i in range(len(seq) - k + 1)]
    # all_kmers = kmers(text, k)
    # freq_table = dict(Counter(all_kmers))

    return freq_table 

if __name__ == "__main__":
    main()