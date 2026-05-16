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






