import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Approach 1: Naive Solution
def delete_duplicates(A: List[int]) -> int:
    '''T=O(n); S=O(n)'''
    if len(A) == 0:
        return 0

    result = [A[0]]
    for i in range(1, len(A)):
        if A[i] == result[-1]:
            continue
        else:
            result.append(A[i])
    
    num_valid = len(result)
    
    A[:] = result[:]
    return num_valid

# Approach 2: Constant Space
def delete_duplicates(A: List[int]) -> int:
    '''T=O(n); S=O(1)'''
    unique = 0
    for i in range(1, len(A)):
        if A[i] != A[unique]:
            unique += 1
            A[unique] = A[i]
    
    num_valid = unique + 1
    return num_valid

# Book Solution
def delete_duplicates(A: List[int]) -> int:
    '''T=O(n); S=O(1)'''
    if not A:
        return 0
    
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index

@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))

# Variant

'''
Implement a function which takes as input an array and a key, and updates the
array so that all occurrences of the input key have been removed and the
remaining elements have been shifted left to fill the emptied indices. Return
the number of remaining elements. There are no requirements as to the values
stored beyond the last valid element.
'''

'''
Write a program which takes as input a sorted array A of integers and a
positive integer m, and updates A so that if x appears m times in A it
appears exactly min(2, m) times in A. The update to A should be performed
in one pass, and no additional storage may be allocated.
'''