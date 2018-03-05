from stacksampler import Sampler

sampler = Sampler()
sampler.start()


def get_number():
    for x in range(5000000):
        yield x


def expensive_function():
    for x in get_number():
        i = x ^ x ^ x


expensive_function()

print(sampler.output_stats())

