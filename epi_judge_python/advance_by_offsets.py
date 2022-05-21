from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    '''T=O(n), S=O(1)'''
    if len(A) == 1:
        return True
    
    required_steps = 1
    for i in reversed(range(1, len(A)-1)):
        if A[i] >= required_steps:
            required_steps = 1
        else:
            required_steps += 1
    
    if A[0] >= required_steps:
        return True
    return False

# Book's Solution
def can_reach_end(A: List[int]) -> bool:
    '''T=O(n), S=O(1)'''
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))


# Variant
'''
Write a program to compute the minimum number of steps needed to
advance to the last location.
'''