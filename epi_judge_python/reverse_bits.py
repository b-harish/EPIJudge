from test_framework import generic_test


def reverse_bits(x: int) -> int:
    NUM_BITS = 64
    result = 0
    for _ in range(NUM_BITS):
        lsb = x & 1
        x = x >> 1
        result = result << 1
        result = result | lsb
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
