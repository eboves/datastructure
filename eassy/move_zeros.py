
# 4. Move Zeroes #283 — Two Pointers
# python# ============================================
# LeetCode #283 - Move Zeroes
# Difficulty: Easy
# Pattern: Two Pointers (Same Direction)
# ============================================
#
# Given an array, move all 0s to the end while
# maintaining the order of non-zero elements.
# Do it in place.
#
# Example 1:
# Input:  nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Example 2:
# Input:  nums = [0]
# Output: [0]
# ============================================



# INPUT: a list of numbers 
# OUTPUT: same modified list
# OPERATION: comparing(primary) → rearenging → collecting
# PATTERN: two pointers, slow=0, fast=0
# DS: two pointers (list)
# PLAN:
#   1. create slow=0, fast=0
#   2. while len(nums) > fast:
#   3. if num[fast] == 0:
#   4.      fast += 1
#   5. else:
#       num[slow] = nums[fast]
        # slow += 1
        # fast += 1





nums = [0, 1, 0, 3, 12]
# nums = [0]

def move_zeroes(nums):
    slow = 0
    fast = 0
    while len(nums) > fast:
        if nums[fast] == 0:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1

    return nums

print(move_zeroes(nums))



