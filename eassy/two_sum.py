# 10. Two Sum #1 — Hash Map
# python# ============================================
# LeetCode #1 - Two Sum
# Difficulty: Easy
# Pattern: Hash Map
# ============================================
#
# Given an array and a target, return indices of
# the two numbers that add up to target.
#
# Example 1:
# Input:  nums = [2,7,11,15], target = 9
# Output: [0,1]
#
# Example 2:
# Input:  nums = [3,2,4], target = 6
# Output: [1,2]
# ============================================


# INPUT: a list and a target
# OUTPUT: a list of the indices that the value add to target
# OPERATION: look up(primary) → find → collect
# PATTERN: dict
# DS: dict
# PLAN:
#   1. create seen = {}
#   2. loop through nums:
#   3.  complement = target - nums[n]
#   4.  if complement in seen:
#   5.      return [seen[complement], n]
#       seen[complement] = n


nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    
    seen = {}
    for n in range(len(nums)):
        complement = target - nums[n]
        if complement in seen:
            return [seen[complement], n]
        seen[nums[n]] = n
print(two_sum(nums, target))





