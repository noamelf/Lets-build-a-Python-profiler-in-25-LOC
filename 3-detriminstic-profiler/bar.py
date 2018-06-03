def bar(x):
    return x * x


for i in range(2_000_000):
    bar(i)
