"""
###################################################### PROBLEM 1 ######################################################################

Group Anagrams — LeetCode #49 🟡 Medium
Given an array of strings, group the strings that are anagrams of each other together.
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
Input:  strs = [""]
Output: [[""]]
Input:  strs = ["a"]
Output: [["a"]]

"""

# ============================================
# Maximum Sum Subarray of Size K
# Difficulty: Easy/Medium boundary
# Pattern: Sliding Window (Fixed Size)
# ============================================
#
# Given an array of integers and a number k,
# find the maximum sum of any contiguous
# subarray of size k.
#
# Example:
# Input:  nums = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9  (from subarray [5, 1, 3])
#
# ============================================
# INPUT:     a list of numbers and k (window size)
# OUTPUT:    single number — the maximum window sum
# OPERATION: ACCUMULATE (primary) → FIND → RETURN
# PATTERN:   Sliding Window (Fixed Size)
# DS:        Two variables — current_sum, max_sum
# PLAN:
#   1. create current_sum = 0, max_sum = 0
#   2. loop from 0 to k → build first window sum
#   3. set max_sum = current_sum
#   4. loop from k to end:
#          current_sum += nums[i]      ← add right element
#          current_sum -= nums[i - k]  ← remove left element
#          max_sum = max(max_sum, current_sum)
#   5. return max_sum
#
# KEY INSIGHT:
# Instead of recalculating sum every window → O(n²)
# Just add one element and remove one element → O(n)
#
# Window slide formula:
#   add  → nums[i]
#   remove → nums[i - k]
# ============================================

nums = [2, 1, 5, 1, 3, 2]
k = 3

def max_sum_subarray(nums, k):
    current_sum = 0
    max_sum = 0
    for i in range(k):
        current_sum += nums[i]
    max_sum = current_sum
    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum

# print(max_sum_subarray(nums, k))


# ============================================
# Average of Each Subarray of Size K
# Difficulty: Easy
# Pattern: Sliding Window (Fixed Size)
# ============================================
#
# Given an array of integers and a number k,
# find the average of each contiguous subarray
# of size k and return them all in a list.
#
# Example:
# Input:  nums = [1, 3, 2, 6, 4, 8], k = 3
# Output: [2.0, 3.67, 4.0, 6.0]
#
# Explanation:
# Window 1: [1, 3, 2] → sum=6  → avg=2.0
# Window 2: [3, 2, 6] → sum=11 → avg=3.67
# Window 3: [2, 6, 4] → sum=12 → avg=4.0
# Window 4: [6, 4, 8] → sum=18 → avg=6.0
# ============================================
# INPUT: list of nums and a window size k
# OUTPUT: a list of average from each window sum
# OPERATION: compare (primary) --> find --> collect 
# PATTERN: sliding window
# DS: slidind window
# PLAN:
#   1. create current_sum = 0, result = []
#   2. loop from 0 to k:
#   3.   max_sum = current_sum
#   4.   result.append(max_sum/k)
#   5. loop from k to len(nums)
#        current_sum += nums[i]
#        current_sum -= nums[i-k]
#        max_sum = max(max_sum, current_sum)
#        result.append(max_sum/k)
#
nums = [1, 3, 2, 6, 4, 8]
k = 3

def subarray_averages(nums, k):
    current_sum = 0.0
    
    result = []
    for i in range(k):
        current_sum += nums[i]
    result.append(current_sum/k)
    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i - k]
        result.append(current_sum/k)
    return result

# print(subarray_averages(nums, k))


# ============================================
# Minimum Sum Subarray of Size K
# Difficulty: Easy
# Pattern: Sliding Window (Fixed Size)
# ============================================
#
# Given an array of integers and a number k,
# find the minimum sum of any contiguous
# subarray of size k.
#
# Example:
# Input:  nums = [3, 5, 2, 1, 6, 4, 8], k = 3
# Output: 8  (from subarray [5, 2, 1])
#
# Explanation:
# Window 1: [3, 5, 2] → sum = 10
# Window 2: [5, 2, 1] → sum = 8  ← minimum
# Window 3: [2, 1, 6] → sum = 9
# Window 4: [1, 6, 4] → sum = 11
# Window 5: [6, 4, 8] → sum = 18
#
# ============================================
# INPUT: a list of nums and the window size k
# OUTPUT: a number representing the min sum 
# OPERATION: compare(primary) --> find --> return
# PATTERN: fixed sliding window
# DS: fixed sliding window
# PLAN:
#    create current_sum = 0, min_sum = float('inf')
#    loop from 0 to ramge(k):
#         current_sum += nums[i]
#    min_sum = min(min_sum, current_sum)
#    loop from k to len(nums)
#         current_sum += nums[i]
#         currnen_sum -= nums[i-k]
#         min_sum = min(current_sum, min_sum)
#   return min_sum
#   

nums = [3, 5, 2, 1, 6, 4, 8]
k = 3

def min_sum_subarray(nums, k):
    min_sum = float('inf')
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]
    min_sum = current_sum
    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i - k]
        min_sum = min(min_sum, current_sum)
    return min_sum


# print(min_sum_subarray(nums, k))

"""
============================================
Smallest Subarray With Sum >= Target
Difficulty: Easy/Medium boundary
Pattern: Sliding Window (Variable Size)
============================================

Given an array of positive integers and a target sum,
find the length of the smallest contiguous subarray
whose sum is greater than or equal to the target.
Return 0 if no such subarray exists.

Example 1:
Input:  nums = [2, 1, 5, 2, 3, 2], target = 7
Output: 2  (subarray [5, 2])

Example 2:
Input:  nums = [2, 1, 5, 2, 8], target = 7
Output: 1  (subarray [8])

Example 3:
Input:  nums = [3, 4, 1, 1, 6], target = 8
Output: 3  (subarray [3, 4, 1] or [1, 1, 6])
============================================

INPUT:
OUTPUT:
OPERATION:
PATTERN:
DS:
VALID WINDOW:
INVALID WINDOW:
PLAN:

"""

nums = [2, 1, 5, 2, 3, 2]
target = 7

def smallest_subarray(nums, target):
    pass

print(smallest_subarray(nums, target))

