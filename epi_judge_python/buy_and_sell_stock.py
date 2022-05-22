from typing import List

from test_framework import generic_test


# Approach 1: Naive Solution
# Test Case #40x took HUGE time.
def buy_and_sell_stock_once(prices: List[float]) -> float:
    '''T=O(n^2); S=O(1)'''
    max_profit = 0.0
    for i in range(len(prices)-1):
        bought = prices[i]
        sold = max(prices[i+1:])
        max_profit = max(max_profit, sold - bought)
    return max_profit

# Approach 2: Linear Time and Space
# Test Case #40x took LESS time now.
def buy_and_sell_stock_once(prices: List[float]) -> float:
    '''T=O(n); S=O(n)'''
    max_sell_array = [0] * len(prices)
    for i in range(len(prices)-2, -1, -1):
        max_sell_array[i] = max(prices[i+1], max_sell_array[i+1])
    
    max_profit = 0
    for i in range(len(prices)):
        max_profit = max(max_profit, max_sell_array[i]-prices[i])
    
    return max_profit

# Approach 3: Constant Space
def buy_and_sell_stock_once(prices: List[float]) -> float:
    '''T=O(n); S=O(1)'''
    max_sell, max_profit = 0, 0
    for i in range(len(prices)-2, -1, -1):
        max_sell = max(max_sell, prices[i+1])
        buy = prices[i]
        profit = max_sell - buy
        max_profit = max(profit, max_profit)
    
    return max_profit

# Book Solution
# Use minimum price seen so far and use current price
# to compute the profit if we want to sell at current price.
def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price_seen_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_seen_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_seen_so_far = min(min_price_seen_so_far, price)
    
    return max_profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))

# Variant

'''
Write a program that takes an array of integers and finds
the length of a longest subarray all of whose entries are equal.
'''