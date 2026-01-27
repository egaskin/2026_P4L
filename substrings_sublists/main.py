def main():
    print("Substrings and sublists")

    # Python uses text[i: i+k: 1] to indicate the substring of text that starts at position i and goes up to
    # (but not including) i + k
    # why exclusive? Convience: substract i + k - i = k gives the length of the substring

    print("\nsubstrings")
    s = "Hi Lovers"
    print(s[1:5])      # length 4 "i Lo"

    print(s[0:7])      # Hi Love
    print(s[:7])       # shorthand meaning start at 0

    print(s[4:len(s)]) # overs
    print(s[4:])       # shorthand meaning end at len(s)

    print("\nsublists")
    a = [0] * 6
    for i in range(len(a)):
        a[i] = 2*i + 1
    # a = [1, 3, 4, 7, 9, 11]
    print(a)
    print(a[3:5])
    print(a[:3])
    print(a[4:])

    text = "ATATA"
    pattern = "ATA"
    print(f"pattern_count(pattern, text) = pattern_count({pattern}, {text}) = {pattern_count(pattern, text)}")
    print(f"built-in isn't the same: text.count(pattern) = {text.count(pattern)}") # the built-in doesnt count overlaps!

def pattern_count(pattern: str, text: str) -> int:
    """
    Finds the number of times that a pattern (text) occurs in a longer
    text string.

    Parameters:
    - pattern: str
    - text: str, a longer string to search for pattern ins

    Returns:
    int: the number of times that pattern occurs in text, with overlaps.
    e.g. "ATA" occurs twice in "ATATA."
    """
    # USE SUB ROUTINE
    # k = len(pattern) # pattern length
    # n = len(text) # text length

    # if k == 0:
    #     raise ValueError("empty pattern not allowed")
    # elif k > n:
    #     print("If pattern longer than text cannot find pattern in text")
    #     return 0

    # # range over text, incrementing count every time we find a pattern match
    # match_count = 0
    # # there are n - k + 1 total substrings of length k in a string of length n (ranging from starting position 0 to n - k)
    # for i in range(n - k + 1): # the last place `pattern` can occur in `text` is the final position minus the length of pattern
    #     print("    Current substring is", text[i:i + k])
    #     if text[i:i + k] == pattern:
    #         match_count += 1
    # return match_count

    return len(starting_indices(pattern, text))

# Insert your starting_indices() function here.
def starting_indices(pattern: str, text: str) -> list[int]:
    """
    starting_indices returns the list containing all the starting positions of pattern in text.
    Parameters:
    - pattern (str): A given substring.
    - text (str): A given superstring.
    Returns:
    - list[int]: A list containing the starting positions of pattern in text (indices).
    """
    k = len(pattern) # pattern length
    n = len(text) # text length

    if k == 0:
        raise ValueError("empty pattern not allowed")
    elif k > n:
        print("If pattern longer than text cannot find pattern in text")
        return []
    
    # range over all starting postiions and if i find a match, append it to positions
    positions = []
    print(f"Current text: {text}")
    print(f"Current pattern: {pattern}")
    for i in range(n - k + 1):
        print("    Current substring is", text[i:i + k])
        if text[i:i + k] == pattern:
            positions.append(i)

    return positions

if __name__ == "__main__":
    main()

