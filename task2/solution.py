from itertools import count
from collections import OrderedDict


def groupby(func, seq):
    return {result: [item for item in seq if func(item) == result] for
            result in set(map(func, seq))}


def iterate(func):
    def iterate_times(times, x):
        result = x

        for i in range(times):
            result = func(result)

        return result

    for times in count():
        yield lambda x: iterate_times(times, x)


def zip_with(func, *iterables):
    return (func(*args) for args in zip(*iterables))


def cache(func, cache_size):
    store = OrderedDict()

    def func_cached(*args):
        if args in store:
            return store[args]

        result = func(*args)

        if cache_size:
            if len(store) == cache_size:
                store.popitem(False)
            store[args] = result

        return result

    return func_cached
