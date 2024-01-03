#!/usr/bin/python3
def uppercase(input_char):
    for x in input_char:
        uppercase = chr(ord(x) - 32) if 97 <= ord(x) <= 122 else x
        print('{}'.format(uppercase), end='')
    print()
