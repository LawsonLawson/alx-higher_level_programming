#!/usr/bin/python3
for x in range(ord('z'), ord('A') -1, -1):
    print('{:c}'.format(x), end='')
    x -= 1
