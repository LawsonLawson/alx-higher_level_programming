#!/usr/bin/python3
for alpha in range(26):
    print('{:c}'.format(97 + alpha) if alpha not in (4, 16) else "", end="")
