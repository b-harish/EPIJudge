from test_framework import generic_test

def divide(x: int, y: int) -> int:
    quotient, k = 0, 64
    two_k_y = y << k
    while x >= y:
        while two_k_y > x:
            two_k_y >>= 1
            k -= 1
        quotient += (1 << k)
        x -= two_k_y

    return quotient

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
