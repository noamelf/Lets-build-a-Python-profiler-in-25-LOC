def super_power(x):
    return x ** x ** x


def count_digits(num):
    return len(str(num))


result = super_power(7)
digit_count = count_digits(result)
print(digit_count)
