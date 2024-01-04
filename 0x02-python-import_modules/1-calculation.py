#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
addition_outcome = add(a, b)
subtraction_outcome = sub(a, b)
product_outcome = mul(a, b)
division_outcome = div(a, b)
print(f'{a} + {b} =', addition_outcome)
print(f'{a} - {b} =', subtraction_outcome)
print(f'{a} * {b} =', product_outcome)
print(f'{a} / {b} =', division_outcome)
