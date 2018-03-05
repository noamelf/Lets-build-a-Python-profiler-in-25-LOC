from stacksampler import Sampler

sampler = Sampler(interval=0.005)
sampler.start()


def get_number():
    for x in range(2000):
        yield x


def expensive_function():
    for x in get_number():
        for y in get_number():
            i = x ^ y


expensive_function()

print(sampler.output_stats())
