"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

    2 <= nums.length <= 104
     before IF-109 <= nums[i] <= 109
    -109 <= target <= 109

"""

# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 print(f"i: {i}; j: {j}")
#                 return [i, j]

# nums = [2,7,11,15]
# target = 9

nums = [3,2,4]
target = 6

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
       
# sum = two_sum(nums, target)
# print(sum)

"""
Given an array of integers prices where prices[i] is the price of a stock on day i,
return the maximum profit you can achieve by buying on one day and selling on a later day.
You can only buy once and sell once. If no profit is possible return 0.
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price=1), sell on day 5 (price=6), profit = 6-1 = 5
Input:  prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: prices only go down, no profit possible
"""
prices = [7, 1, 5, 3, 6, 4]

def stock_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price 
    
        if profit > max_profit:
            max_profit = profit
        
    return max_profit

# profit = stock_profit(prices)
profit = stock_profit(prices)
print(profit)