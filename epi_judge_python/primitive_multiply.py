from test_framework import generic_test

def add_bits(x, y, cin):
    '''Adds three bits and returns its sum & carry.
    Assumes x & y & ciin are single bits.'''
    s = x ^ y ^ cin
    c = ((~x & y & cin) | (x & ~y & cin) |
         (x & y & ~cin) | (x & y & cin))
    return s, c

def add_nums(x, y):
    '''Adds two integers. T = O(n)'''
    NUM_BITS = 64
    result, cin = 0, 0
    for i in range(NUM_BITS):
        lsb_x = x & 1
        lsb_y = y & 1
        s, cin = add_bits(lsb_x, lsb_y, cin)
        result |= (s << i)
        x >>= 1
        y >>= 1
    return result

# Practically faster than above version
def add_nums(a, b):
    running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
    while temp_a or temp_b:
        ak, bk = a & k, b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        running_sum |= ak ^ bk ^ carryin
        carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
    return running_sum | carryin

def multiply(x: int, y: int) -> int:
    '''Multiplies x & y using binary operators.'''
    result = 0
    while y:
        if y & 1:
            result = add_nums(result, x)
        x, y = x << 1, y >> 1
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
