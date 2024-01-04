#!/usr/bin/python3

if __name__ == "__main__":
    """ Print the addition of all arguments."""
    import sys

    outcome = 0
    for args in range(len(sys.argv) - 1):
        total += int(sys.argv[args + 1])
    print("{}".format(outcome))
