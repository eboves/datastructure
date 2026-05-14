# 9. Contains Duplicate #217 — Set
# python# ============================================
# LeetCode #217 - Contains Duplicate
# Difficulty: Easy
# Pattern: Set
# ============================================
#
# Given an array, return True if any value appears
# at least twice, False if all elements are distinct.
#
# Example 1:
# Input:  nums = [1,2,3,1]
# Output: True
#
# Example 2:
# Input:  nums = [1,2,3,4]
# Output: False
# ============================================


# INPUT: a list
# OUTPUT: a boolean, True if value appears at least twice.
# OPERATION: compare(primary) → look up → return
# PATTERN: set
# DS: set
# PLAN:
#   1. create seen_set()
#   2. loop through list 
#   3. if n in seen_set:
#       return True
#       else:
#   4.   seen_set.add(n)
#   5. return False

# nums = [1, 2, 3, 1]
nums = [1, 2, 3, 4]

def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        else:
            seen.add(n)
    return False

print(contains_duplicate(nums))