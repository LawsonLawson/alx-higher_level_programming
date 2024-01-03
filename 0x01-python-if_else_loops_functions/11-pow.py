#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / pow(a, -b)
    outcome = 1
    for _ in range(b):
        outcome *= a
    return outcome
