import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    '''Naive Solution: T=O(n); S=O(n)'''
    if len(A) == 0:
        return 0

    result = [A[0]]
    for i in range(1, len(A)):
        if A[i] == result[-1]:
            continue
        else:
            result.append(A[i])
    
    num_valid = len(result)
    for i in range(len(A)-num_valid):
        result.append(0)
    
    A[:] = result[:]
    return num_valid


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
