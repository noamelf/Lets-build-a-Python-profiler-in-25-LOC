from src import sfProfiler


def calc(x):
    return  x ** x


def main():
    calc(100_000)
    calc(200_000)


sfProfiler.start()
main()
print(sfProfiler.format_stats())
