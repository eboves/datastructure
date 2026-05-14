
# 7. Valid Anagram #242 — Hash Map
# python# ============================================
# LeetCode #242 - Valid Anagram
# Difficulty: Easy
# Pattern: Hash Map
# ============================================
#
# Given two strings, return True if t is an anagram of s.
#
# Example 1:
# Input:  s = "anagram", t = "nagaram"
# Output: True
#
# Example 2:
# Input:  s = "rat", t = "car"
# Output: False
# ============================================


# INPUT: two string: s and t
# OUTPUT: return a boolean True if it is, else False.
# OPERATION: count(primary) → compare → return
# PATTERN: dict    
# DS: dict
# PLAN:
#   1. create new_list
#   2. loop through s and count chars
#   3.  new_list[n] = new_list.get(n, 0) + 1
#   4. loop through t:
#   5.  if t[n] in new_list
#         new_list[t[n]] -= 1
#       else:
#           return False
#       return True



# s = "anagram"
# t = "nagaram"
# s = "rat"
# t = "car"
s = "aa"
t = "aaa"

def valid_anagram(s, t):
    new_list = {}
    for char in s:
        new_list[char] = new_list.get(char, 0) + 1
    for char in t:
        if char in new_list and new_list[char] > 0:
            new_list[char] -= 1
        else:
            return False
    return True

print(valid_anagram(s, t))