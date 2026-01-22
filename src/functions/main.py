# structure of functions
"""
def function_name(parameter_1: type, parameter_2: type) -> return_type:
    # function body
    return value
"""
# NOTE 2: the defintion of functions can occur in any order, but when functions are executed, defintions must have already been encountered!

# NOTE 2a: this function can be defined up heare
def sum_two_ints_v1(a, b):
    """
    Returns the sum of two input integers. v1 doesn't use type hints.

    Parameters:
    - a (int): The first integer.
    - b (int): The second integer.

    Returns:
    - int: The sum of the two integers.
    
    """
    return a + b
def sum_two_ints_v2(a: int, b: int) -> int:
    """
    Returns the sum of two input integers. v2 uses type hints.

    Parameters:
    - a (int): The first integer.
    - b (int): The second integer.

    Returns:
    - int: The sum of the two integers.
    
    """
    return a + b

# functions can return multiple values
def double_and_duplicate(x: float) -> tuple[float, float]:
    """
    Returns double the input value and the input value duplicated as a tuple.

    Parameters:
    - x (float): The input float value.

    Returns:
    - tuple: A tuple containing double the input value and the duplicated input value.
    
    """
    return 2*x, 2*x # this works
    # return (2 * x, x * 2) # this also works

def main():
    """
    Special function that takes no inputs, produces no outputs, but constitutes the runnable component of the current python script.
    """


    print("Functions module beginning!")

    x = 3
    y = 5
    n = sum_two_ints_v1(x, y)
    print(f"""\nSum of x and y using version 1:
x + y = n
{x} + {y} = {n}""")

    n = sum_two_ints_v2(x, y)
    print(f"""\nSum of x and y using version 2:
x + y = n
{x} + {y} = {n}""")
    
    # what if i do not pass integers?
    n = sum_two_ints_v2(3.5, 2.1)  # type: ignore # this will work, but is not type safe
    print(f"""\nSum of 3.5 and 2.1 using version 2:
3.5 + 2.1 = n
3.5 + 2.1 = {n}
(Note: this worked, but is not type safe since floats were passed to a function expecting ints)""")
    # type hints are just that - they are hints. they do not enforce type checking at runtime.

    print(f"\nDemonstrating function that returns multiple values, double_and_duplicate(x) = double_and_duplicate({x}) = {double_and_duplicate(x)}")

    # let's test print_hi, a function with no input or output
    print("\ntesting print_hi function:")
    print_hi()
    # what if we save the output of print_hi to a variable?
    result = print_hi()  # this will execute print_hi, but result will be None
    print(f"\nThe result of calling print_hi() and saving to a variable is: {result} (type: {type(result)})")

    # let's test add_one, a function that takes an int and returns an int
    m = 17
    print(f"\nTesting add_one function, add_one({m}) = {add_one(m)}")
    print(f"value of m is after add_one: m = {m}")
    # add_one does not modify the input variable!!!

    # with basic types (str, int, float, bool), python uses "pass by value" semantics
    # this means that when you pass a variable to a function, the function gets a copy of the value
    # "pass by reference" semantics would mean that the function gets access to the original variable and can modify it. Python uses "pass by reference" for complex types (lists, dictionaries) and custom objects

    test_dict = {"a": 1, "b": 2}
    print(f"\nOriginal test_dict before passing to function: {test_dict} (id: {id(test_dict)})")

# NOTE 2b: this function can be defined down here
# def sum_two_ints_v1

def print_hi():
    """
    Takes no input and simply prints "Hi" to the console.

    Returns:
    None
    
    """
    print("Hi from print_hi function!")
    # other things could happen here
    # print() does not return any value

def add_one(k: int) -> int:
    """
    Adds one to the input integer and returns the result.

    Parameters:
    - k (int): The input integer.

    Returns:
    - int: The input integer plus one.
    
    """
    # when you see variable assignment (x = blah)
    # the left side of the equation is a variable
    # the RHS of the equation is accessing the values inside the variables
    k = k + 1
    return k
    # k gets modified here, but this does not affect the variable passed in

########################################
# Homework: https://cogniterra.org/lesson/29831/step/1?unit=21910
########################################

# Insert your sum_two_ints() function here.
def sum_two_ints(a: int, b: int) -> int:
    """
    Return the sum of two integers.
    Args:
        a: (int).
        b: (int).
    Returns:
        The integer sum of a and b.
    """
    return a + b

if __name__ == "__main__":
    main() # function call to main function

# NOTE 2c: this function CAN NOT be defined down here below the if __name__ == "__main__": block so that it is not found when called in main()
# def sum_two_ints_v1 # ERROR because function is not defined yet when main() is called