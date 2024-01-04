#!/usr/bin/python3

# Before importing, check if the script is being run as the main program
if __name__ == "__main__":
    # Importing the add function from the add_0.py file
    from add_0 import add

    # Assigning values a and b
    a = 1
    b = 2

    # Invoking the add function, already defined in add_0.py file
    outcome = add(a, b)

    # Printing the result to stdout
    print("{} + {} = {}".format(a, b, outcome))
