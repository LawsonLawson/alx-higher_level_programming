#!/usr/bin/python3
# Before importing, check if the script is being run as the main program
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    outcome = add(a, b)
    print("{} + {} = {}".format(a, b, outcome))
