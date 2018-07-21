from src import sProfiler


def calc(x):
    return  x ** x


def main():
    calc(100_000)
    calc(200_000)


sProfiler.start()
main()
print(sProfiler.format_stats())
