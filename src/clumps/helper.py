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
