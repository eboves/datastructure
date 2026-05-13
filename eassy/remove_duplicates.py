#3. Remove Duplicates from Sorted Array #26 — Two Pointers
# python# ============================================
# LeetCode #26 - Remove Duplicates from Sorted Array
# Difficulty: Easy
# Pattern: Two Pointers (Same Direction)
# ============================================
#
# Given a sorted array, remove duplicates in place.
# Return k — the number of unique elements.
#
# Example 1:
# Input:  nums = [1,1,2]
# Output: k=2, nums=[1,2,_]
#
# Example 2:
# Input:  nums = [0,0,1,1,1,2,2,3,3,4]
# Output: k=5, nums=[0,1,2,3,4,_,_,_,_,_]
# ============================================


# INPUT: a sorted array nums
# OUTPUT: k as the number of unique elements
# OPERATION: compare(primary) → rearrange → return k
# PATTERN: two pointers slow=0, fast=1
# DS: two pointers
# PLAN:
#   1. create slow=0 and fast=1
#   2. while len(nums) > fast:
#   3. if nums[slow] == nums[fast]:
#   4.    fast+=1
#   5. if nums[slow] != nums[fast]:
#          slow += 1; slow=fast; fast +=1
#      return slow + 1

# nums = [1, 1, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

def remove_duplicates(nums):
    slow=0
    fast=1
    while len(nums) > fast:
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
    return slow + 1, nums
    

print(remove_duplicates(nums))


#  if nums[slow] != nums[fast]:
#             slow += 1
#             nums[slow] = nums[fast]
#             fast += 1