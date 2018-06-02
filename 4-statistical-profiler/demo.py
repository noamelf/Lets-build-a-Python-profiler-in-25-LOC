from statistical_profiler import start, format_stats


def calc(x):
    return x ** x


start()

calc(100_000)
calc(200_000)

print(format_stats())
