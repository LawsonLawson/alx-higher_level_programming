#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    outcome = 0
    for args in range(len(sys.argv) - 1):
        outcome += int(sys.argv[args + 1])
    print("{}".format(outcome))
