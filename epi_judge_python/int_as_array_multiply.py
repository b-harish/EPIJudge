from audioop import reverse
from typing import List

from test_framework import generic_test

# Approach 1: Covert array to integer and multiply and revert back to array
def multiply(num1: List[int], num2: List[int]) -> List[int]:
    '''T=O(n), S=O(n)'''
    a = int(''.join([str(num) for num in num1]))
    b = int(''.join([str(num) for num in num2]))
    product = a * b
    result = [int(num) for num in str(product) if num != '-']
    if product < 0:
        result[0] *= -1
    return result

# Approach 2: No conversion between array and integer. Operate as such.
def multiply_with_single(num1: List[int], b: int) -> List[int]:
    '''Multiplies a list of integers with a single digit integer.
    T=O(n), S=O(1)'''
    num1 = list(num1)
    num1[-1] = num1[-1] * b
    carry = 0
    for i in reversed(range(1, len(num1))):
        if num1[i] >= 10:
            carry = num1[i] // 10
            num1[i] %= 10
        else:
            carry = 0
        num1[i-1] = (num1[i-1] * b) + carry

    if num1[0] >= 10:
        carry = num1[0] // 10
        num1[0] %= 10
        num1.insert(0, carry)
    
    return num1

def add(A: List[int], B: List[int]) -> List[int]:
    '''Adds two array of integers'''
    result = [0] * len(A)
    if len(B) > len(A):
        result = [0] * len(B)
    
    times = min(len(A), len(B))
    carry = 0

    for i in range(-1, -(times+1), -1):
        result[i] = A[i] + B[i] + carry
        if result[i] >= 10:
            carry = result[i] // 10
            result[i] %= 10
        else:
            carry = 0
    
    pending = A if len(A)>len(B) else B
    for i in range(-(times+1), -(len(pending)+1), -1):
        result[i] = pending[i] + carry
        if result[i] >= 10:
            carry = result[i] // 10
            result[i] %= 10
        else:
            carry = 0
    
    if carry != 0:
        return [carry] + result
    
    return result

def multiply(num1: List[int], num2: List[int]) -> List[int]:
    '''T = O(nm), S=O(n+m)'''
    result = None
    num1_sign = 1 if num1[0] >= 0 else -1
    num2_sign = 1 if num2[0] >= 0 else -1

    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])

    if num1[0] == 0 or num2[0] == 0:
        return [0]

    for i in range(len(num2)):
        if i == 0:
            result = multiply_with_single(num1, num2[len(num2)-1-i])
            # print(result)
        else:
            # print(result, end=' ')
            b = num2[len(num2)-1-i]
            temp = multiply_with_single(num1, num2[len(num2)-1-i])
            temp = temp + ([0] * i)
            result = add(result, temp)
            # print(temp, result)

    result[0] = (num1_sign * num2_sign) * result[0]
    return result

# Approach 3: Book Solution. Very Elegant!
# Uses the fact that the resultant array will contain
# n+m digits and trying to fill each of those position from the end.
def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if ((num1[0] < 0) ^ (num2[0] < 0)) else 1 # Nice way to determine the resultant sign
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1)+len(num2)) # resultant array size: n + m
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i+j+1] // 10
            result[i + j + 1] %= 10
    
    # Remove the leading zeros
    result = result[next((i for i, x in enumerate(result)
                            if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))


# Checks if utility functions of Approach 2 is working fine.
assert multiply_with_single([1, 2, 3], 3) == [3, 6, 9]
assert multiply_with_single([0, 0, 0], 3) == [0, 0, 0]
assert multiply_with_single([0, 0, 0], 9) == [0, 0, 0]
assert multiply_with_single([5, 5, 5], 5) == [2, 7, 7, 5]
assert multiply_with_single([1, 9, 3, 7, 0, 7, 7, 2, 1], 7) == [1, 3, 5, 5, 9, 5, 4, 0, 4, 7]
assert multiply_with_single([1, 9, 3, 7, 0, 7, 7, 2, 1], 8) == [1, 5, 4, 9, 6, 6, 1, 7, 6, 8]

assert add([1, 2, 3], [1]) == [1, 2, 4]
assert add([9, 9, 9, 9], [1]) == [1, 0, 0, 0, 0]
assert add([9, 8, 7], [7, 8, 4, 3]) == [8, 8, 3, 0]