#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argument_count = len(sys.argv) - 1
    if argument_count == 0:
        print("0 arguments.")
    elif argument_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argument_count))
    for args in range(argument_count):
        print("{}: {}".format(args + 1, sys.argv[args + 1]))
