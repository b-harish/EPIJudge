from typing import List

from test_framework import generic_test

def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_sell, max_profit = 0, 0
    for i in range(len(prices)-2, -1, -1):
        max_sell = max(max_sell, prices[i+1])
        buy = prices[i]
        profit = max_sell - buy
        max_profit = max(profit, max_profit)
    
    return max_profit

# Keeps on running at [400/402] test case. Halted the program.
def buy_and_sell_stock_twice(prices: List[float]) -> float:
    '''T=O(n^2); S=O(1)'''
    if not prices:
        return 0

    max_profit = 0
    # +1 in the for loop allows for  doing a single transaction from start to end
    for i in range(1, len(prices)+1):
        profit1 = buy_and_sell_stock_once(prices[:i])
        profit2 = buy_and_sell_stock_once(prices[i:])
        profit = profit1 + profit2
        max_profit = max(profit, max_profit)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
