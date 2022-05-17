from multiprocessing.sharedctypes import Value
from test_framework import generic_test
from math import log2

def weight(x: int) -> int:
    result = 0
    while x:
        result += 1
        x = x & (x-1)
    return result

def closest_int_same_bit_count(x: int) -> int:
    w = weight(x)
    i = 1
    while True:
        y = x - i
        if weight(y) == w:
            return y
        y = x + i
        if weight(y) == w:
            return y
        i += 1

def closest_int_same_bit_count(x: int) -> int:
    '''T = O(n)'''
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):
        if (x >> i) & 1 != (x >> (i+1)) & 1:
            x ^= (1 << i) | (1 << (i+1))
            return x
    
    raise ValueError('All bits are 0 or 1')

def swap(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        return x ^ bit_mask
    return x

def closest_int_same_bit_count(x: int) -> int:
    '''T = O(1)'''
    lsb = x & 1
    k = x & ~(x-1)
    if lsb == 1:
        y = ~x
        k = y & ~(y-1)
    i =  int(log2(k))
    return swap(x, i, i-1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
