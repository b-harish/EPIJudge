import functools
import random
import math

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)

def random_integer(total_bits: int) -> int:
    '''Returns a random integer between 0 and 2**total_bits - 1'''
    result = 0
    for i in range(total_bits):
        bit = zero_one_random()
        result |= (bit << i)
    return result

def uniform_random(lower_bound: int, upper_bound: int) -> int:
    n = upper_bound - lower_bound
    total_bits = math.floor(math.log2(n)) + 1
    k = random_integer(total_bits)

    while k > n:
        k = random_integer(total_bits)
    return lower_bound + k


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
