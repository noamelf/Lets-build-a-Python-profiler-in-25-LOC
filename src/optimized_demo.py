# optimized_demo.py
import math


def super_power(x):
    return x ** x ** x


def count_digits(num):
    return int(math.log10(num)) + 1


result = super_power(7)
digit_count = count_digits(result)
print(digit_count)
