def main():
    print("Variables module!")

    # this is a comment. Python will ignore it
    my_variable = 10  # this is an inline comment

    # COMMENT YOUR CODE FREQUENTLY

    # let's declare some variables (dynamic typing)
    j = 14   # int
    x = -2.3   # float
    yo_world = "Hi"   # str, snake case variable naming is all lowercase with underscores
    statement = True   # bool, can be either True or False

    print("Here are the test variables (no type hinting):")
    print(f"""j: {j} 
x: {x}
yo_world: {yo_world}
statement: {statement}""")

    # let's declare some variables (type hinting)
    j: int = 14   # int
    x: float = -2.3   # float
    yo_world: str = "Hi"   # str, snake case variable naming is all lowercase with underscores
    statement = True   # bool, can be either True or False

    print("\nHere are the test variables (dynamic typing):")
    print(f"""j: {j} 
x: {x}
yo_world: {yo_world}
statement: {statement}""")

    statement = "python is dumb"
    print(f"\nAfter changing statement to a different type, statement = {statement}")

    # we can check the type of a variable using the type() function
    print(f"""\nChecking types:
type of j = {type(j)}
type of x = {type(x)}
type of yo_world = {type(yo_world)}
type of statement = {type(statement)}""")
    
    # if we're not sure something will work, a try except block can help us catch errors (good practice to specify the type of error catching)
    try:
        print(2(j + 5))  # this will raise an error
    except TypeError as e: # could be just "except:" to catch all errors, but it's better to be specific
        print(f"\nCaught an error for code 2(j + 5): {e}")

    # arithmetic in python
    print(2*(j+5))  # correct way to do multiplication
    print(x/4 + 3.16) # division and addition

    # python even allows mixed types!
    print(x*j)
    print("after multiplication, x and j still have their original values and types:")
    print("x:", x, "type:", type(x))
    print("j:", j, "type:", type(j))

    # we have additional mathematical operations
    print(14/3)  # division, results in a float
    print(14//3)  # floor division, results in an int
    print(14%3)  # modulus, results in the remainder of the division
    print(14**3) # exponentiation, 14 to the power of 3


if __name__ == "__main__":
    main()