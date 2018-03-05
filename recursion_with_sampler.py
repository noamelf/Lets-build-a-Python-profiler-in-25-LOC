from stacksampler import Sampler


def recur(n):
    if n == 0:
        return
    recur(n-1)


sampler = Sampler()
sampler.start()

for i in range(5000):
    recur(700)


sampler.output_stats()
