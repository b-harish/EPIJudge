import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

def reorder(A, pivot_index):
    '''T = O(n), S = O(n)'''
    pivot = A[pivot_index]
    less, equal, greater = [], [], []
    for elt in A:
        if elt == pivot:
            equal.append(elt)
        elif elt < pivot:
            less.append(elt)
        else:
            greater.append(elt)
    A[:] = less + equal + greater

def reorder(A, pivot_index):
    '''T = O(n), S = O(1)'''
    pivot = A[pivot_index]

    next_less = 0
    # Groups all the elements less than pivot to the left
    for i in range(len(A)):
        if A[i] < pivot:
            A[next_less], A[i] = A[i], A[next_less]
            next_less += 1
    
    next_greater = len(A)-1
    # Groups all the elements greater than pivot to the right
    for i in range(len(A)-1, next_less-1, -1):
        if A[i] > pivot:
            A[next_greater], A[i] = A[i], A[next_greater]
            next_greater -= 1

    # By here, all the equal to pivot elements would be in the middle


def reorder(A, pivot_index):
    '''
    T = O(n), S = O(1), Single Pass
    Maintain 4 groups: less than pivot, equal to pivot, unclassified, greater than pivot.
    Initially all the elements are in unclassified group.
    '''
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)-1
    while equal <= larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] > pivot:
            A[larger], A[equal] = A[equal], A[larger]
            larger -= 1
        else:
            equal += 1

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    reorder(A, pivot_index)
    return

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))


# Variant
'''
Assuming that keys take on of thre values, reorder the array so that all objects with the
same key appear together. The order of the subarrays is not important.
Use O(1) additional space and O(n) time.
'''

# This is same as the above problem instead we can choose
# any element as pivot and apply the algorithm we already arrived at.
def reorder_same_key_together(A):
    '''T = O(n), S = O(1)'''
    # Assume first element as pivot always
    pivot_index = 0
    reorder(A, pivot_index)

'''
Given an array A of n objects with keys that takes one of four values,
reorder the array so that all objects that have the same key appear together.
Use O(1) additional space and O(n) time
'''

# TODO

'''
Given an array A of n objects with Boolean-valued keys, reorder the array
so that objects that have the key false appear first.
Use O(1) additional space and O(n) time
'''

# TODO

'''
Given and array A of n objects with Boolean-valued keys, reorder the array
so that objects that have key false appear first. The relative ordering
of objects with key true should not change.
Use O(1) additional space and O(n) time
'''

# TODO