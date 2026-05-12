# 1. Intersection of Two Arrays II #350 — Hash Map
# python# ============================================
# LeetCode #350 - Intersection of Two Arrays II
# Difficulty: Easy
# Pattern: Hash Map
# ============================================
#
# Given two integer arrays nums1 and nums2, return an array
# of their intersection. Each element in the result must
# appear as many times as it shows in both arrays.
#
# Example 1:
# Input:  nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
#
# Example 2:
# Input:  nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# ============================================

# INPUT: two dif. unsorted list
# OUTPUT: a new list with intersection of both arrays
# OPERATION: count(primary) → compare → collect
# PATTERN: dict (frequency > 0)
# DS: dict
# PLAN:
#   1. create new_list array, create result_list
#   2. loop through nums1:
#       new_list[n] = new_list.get(n, 0) + 1 
#   3. loop thrugh nums2:
#       compare new_list with nums2.
#       if nums2 in new_list:
#           reduce value in new_list
#           result_list.append(nums2[n])
#   4. return result_list.
#   5.



# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

def intersect(nums1, nums2):
    result = []
    new_dict = {}
    
    for num in nums1:
        new_dict[num] = new_dict.get(num, 0) + 1
    for n in nums2:
        if n in new_dict and new_dict[n] > 0:
            result.append(n)
            new_dict[n] = new_dict.get(n, 0) - 1
            
    return result
# print(intersect(nums1, nums2))