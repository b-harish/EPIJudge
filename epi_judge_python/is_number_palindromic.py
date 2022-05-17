from test_framework import generic_test
import math

def reverse(x: int) -> int:
    result, x_remaining = 0, abs(x)
    while x_remaining:
        d = x_remaining % 10
        result = (result * 10) + d
        x_remaining = x_remaining // 10

    return -result if x < 0 else result

def is_palindrome_number(x: int) -> bool:
    '''T = O(1)'''
    if x < 0:
        return False
    x_reverse = reverse(x)
    return True  if x == x_reverse else False

def is_palindrome_number(x: int) -> bool:
    '''Without using reverse operation'''
    if x <= 0:
        return x == 0
    
    num_digits = math.floor(math.log(x, 10)) + 1
    msd_mask = 10 ** (num_digits-1)

    for _ in range(num_digits//2):
        if (x // msd_mask) != (x % 10):
            return False
        # Remove MSD
        x = x % msd_mask
        # Remove LSD
        x = x // 10
        # Update MSD Mask
        msd_mask = msd_mask // 100
    
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
