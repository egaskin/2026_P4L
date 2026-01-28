
def main():
    print("Strings module!")

    s = 'Hi'
    t = "Lovers"

    # concaternation glues together strings
    new_string = s + " " + t
    print(new_string)

    # multiplication with strings is just like integers
    # it's repeated additions
    print(s * 3) # s + s + s

    # strings are (kinda) tuple of symbols
        # 1. can access individual elements with the indexing operator []
        # 2. strings are immutable
    # 1. examples
    print(f"The first symbol of new_string: {new_string[0]}")
    print(f"The last symbol of new_string: {new_string[-1]}")

    if t[2] == "v":
        print("The symbol at the 3rd position [index 2] of t is v")
    if t[2] != "V": # strings are case sensitive
        print("The symbol at the 3rd position [index 2] of t is NOT V")

    # 2. examples
    # try: 
    #     t[0] = "N"
    # except 

    # but we can change the entire string at once :)
    s = "Yo"
    print(s)

    s +=  "-Yo"
    s += " Ma"
    print(s)

    dna = "ACCGAT"
    print(complement(dna)) # TGGCTA
    try:
        dna = "ACCGAU"
        print(complement(dna)) # TGGCTA
    except ValueError as e:
        print(e)

    test_rev = "ABCDE"
    print(f"testing reverse:\n{test_rev}\n{reverse(test_rev)}")


# Write your reverse_complement() function here, along with any subroutines that you need.
def reverse_complement(dna: str) -> str:
    """
    Compute the reverse complement of a DNA string. Uses DNA alphabet only (A, C, G, T).
    Complementary base pairs are classic: A-T, C-G

    Args:
        dna: A DNA string.
    Returns:
        The reverse complement of the DNA string.
    """
    return reverse(complement(dna))

# Insert your complement() function here.
def complement(dna: str) -> str:
    """
    Return the complementary DNA string (without reversing it).

    Args:
        dna: A DNA string.
    Returns:
        The DNA string formed by replacing A with T, T with A,
        C with G, and G with C.
    """
    new_dna = ""
    for i, symbol in enumerate(dna):
        # # what is the current symbol in my string
        # if symbol == "A":
        #     new_dna += "T"
        # elif symbol == "T":
        #     new_dna += "A"
        # elif symbol == "C":
        #     new_dna += "G"
        # elif symbol == "G":
        #     new_dna += "C"
        # else:
        #     raise ValueError(f"dna is expected to follow the DNA alphabet, but {dna} symbol at dna[{i}]={symbol}")

        # python's version of a switch statement!
        match symbol:
            case "A":
                new_dna += "T"
            case "T":
                new_dna += "A"
            case "C":
                new_dna += "G"
            case "G":
                new_dna += "C"
            case _: # default case
                raise ValueError(f"dna is expected to follow the DNA alphabet, but for dna={dna}, symbol at dna[{i}]={symbol}")
        
    return new_dna

# Write your reverse() function here.
def reverse(s: str) -> str: # type: ignore
    """
    Reverse a string.

    Args:
        s: A string.
    Returns:
        The string formed by reversing the order of the symbols of s.
    """
    # v1
    # return s[::-1] # pythonic indexing

    # v2
    # return s.reverse() # python built-in

    # v3
    # print(f"len(s) = {len(s)}")
    # # the starter python way
    # rev = ""
    # for cur_char in s:
    #     rev = s + cur_char
    # return rev

    # v4
    # # the "general" programmer way
    # # NOTE: this is slow because we are creating a new string everytime! we have to reallocate memory for a new, increasingly long string at each of the n steps
    # rev = ""
    # n = len(s)
    # for i in range(n):
    #     # rev = s[i] + rev
    #     rev += s[(n - 1) - i]
    #     # i         index of s
    #     # 0         n - 1
    #     # 1         n - 2
    #     # ...       (n - 1) - i
    #     # n - 1     0
    # return rev

    # v5
    # # better "general" programmer way for speed
    # characters = []
    # n = len(s)
    # for i in range(n):
    #     characters.append(s[(n - 1) - i])
    # return "".join(characters)

    # # v6 - linear memory, linear runtime (2n memory)
    # # better "general" programmer way for speed, preallocate an array and access each element once
    # n = len(s)
    # characters = [""]*n
    # for i in range(n):
    #     characters[(n - 1) - i] = s[(n - 1) - i]
    # return "".join(characters)

    # v7 - linear memory, linear runtime (1n memory)
    # somewhat better "general" programmer way for speed and def better for memory
    # split the existing string to a list in place (assign to s), then range over that
    # list and switch 
    # "ABCDE", n = 5
    # i         i_switch
    # 0         4 = (n - 1) - i
    # 1         3 = (n - 1) - i
    # 2         2 = (n - 1) - i

    # "ABCD", n = 4
    # i         i_switch
    # 0         3 = (n - 1) - i
    # 1         2 = (n - 1) - i
    # 2         1 = (n - 1) - i
    # (but not faster than v6 since we preprocess the string into a list) 
    s: list[str] = list(s)
    n = len(s)

    for i in range(0, n//2):
        i_switch = n - i - 1
        # print(i, i_switch)
        if i >= i_switch:
            break
        tmp = s[i]
        s[i] = s[i_switch]
        s[i_switch] = tmp

    return "".join(s)

if __name__ == "__main__":
    main()
    