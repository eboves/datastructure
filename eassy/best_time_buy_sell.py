
# 8. Best Time to Buy and Sell Stock #121 — Greedy
# python# ============================================
# LeetCode #121 - Best Time to Buy and Sell Stock
# Difficulty: Easy
# Pattern: Greedy
# ============================================
#
# Given an array of prices, return the maximum profit
# from buying on one day and selling on a later day.
# Return 0 if no profit is possible.
#
# Example 1:
# Input:  prices = [7,1,5,3,6,4]
# Output: 5
#
# Example 2:
# Input:  prices = [7,6,4,3,1]
# Output: 0
# ============================================


# INPUT: a list of prices  
# OUTPUT: return profit if there is or 0 if not profit
# OPERATION: compare(primary) → find → return
# PATTERN: greedy
# DS: list     
# PLAN:
#   1. create min_price = prices[0] and max_profit = 0, profit = 0
#   2. loop through prices
#   3.      if price < min_price:
#   4.          min_price = price
#   5.      profit = price - min_price
         #  if profit > max_profit:
         #    max_profit = profit
        # return max_profit







prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]

def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit

print(max_profit(prices))