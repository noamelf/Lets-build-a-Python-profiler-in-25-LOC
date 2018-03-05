import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()


def fib(n):
    # from http://en.literateprograms.org/Fibonacci_numbers_(Python)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


fib(10)

pr.disable()
ps = pstats.Stats(pr, stream=io.TextIOBase()).sort_stats('cumulative')
ps.print_stats()
print(s.getvalue())
