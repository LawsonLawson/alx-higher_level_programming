#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    for count in range(0, x):
        try:
            print('{:d}'.format(my_list[count]), end='')
            index += 1
        except IndexError:
            pass
    print()
    return index
