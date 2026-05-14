
# 6. Majority Element #169 — Hash Map
# python# ============================================
# # LeetCode #169 - Majority Element
# Difficulty: Easy
# Pattern: Hash Map
# ============================================
#
# Given an array, return the element that appears
# more than n/2 times. It always exists.
#
# Example 1:
# Input:  nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input:  nums = [2,2,1,1,1,2,2]
# Output: 2
# ============================================


# INPUT: a list of elements     
# OUTPUT: a variable holding the number that repeats the most    
# OPERATION: count(primary) → compare → return element
# PATTERN: dict
# DS: dict
# PLAN:
#   1. create new_dict
#   2. loop throgh nums
#   3. nums[n] = nums.get(n, 0) + 1
#   4. 
#   5.


nums = [3, 2, 3]
# nums = [2, 2, 1, 1, 1, 2, 2]

def majority_element(nums):
    new_dict = {}
    for n in nums:
        print(n)

print(majority_element(nums))
# d = {3:2, 2: 4}
# print(max(d.values()))
