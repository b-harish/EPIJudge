from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    '''T = O(n), S = O(1)'''

    d = A[-1] + 1
    carry, _sum = d // 10, d % 10
    A[-1] = _sum

    for i in range(len(A)-2, -1, -1):
        if carry == 0:
            break
        d = A[i] + carry
        carry, _sum = d // 10, d % 10
        A[i] = _sum

    if carry != 0:
        A.insert(0, carry)
    
    return A

# Elegant solution in Book with same complexity
def plus_one(A: List[int]) -> List[int]:
    '''T=O(n), S=O(1)'''
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    
    if A[0] == 10:
        # There is a carry-out, so we need one more digit to store the result.
        # A slick way to do this is to append a 0 at the end of the carry,
        # and update the first entry to 1.
        A[0] = 1
        A.append(0)
    return A

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))


# Variant
'''
Write a program which takes as input two strings s and t of bits encoding
binary numbers Bs and Bt, respectively, and returns a new string of bits
representing the numbers Bs + Bt.
'''