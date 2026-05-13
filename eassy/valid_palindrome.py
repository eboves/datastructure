# 5. Valid Palindrome #125 — Two Pointers
# python# ============================================
# LeetCode #125 - Valid Palindrome
# Difficulty: Easy
# Pattern: Two Pointers (Opposite Ends)
# ============================================
#
# A phrase is a palindrome if after removing non-alphanumeric
# characters and lowercasing, it reads the same forwards and backwards.
#
# Example 1:
# Input:  s = "A man, a plan, a canal: Panama"
# Output: True
#
# Example 2:
# Input:  s = "race a car"
# Output: False
# ============================================


# INPUT: a phrase 
# OUTPUT:  return a boolean True or False  
# OPERATION: compare(primary) → return 
# PATTERN: two pointers different positions, left=0; right=len(s)-1
# DS: two pointers
# PLAN:
#   1. create left=0; fast=len(s) - 1
#   2. while left <= fast:
#      s = s.low()
#   3. s = ''.join(c for c in s if c.isalnum())
#   4. if s[left] == s[right]:
#   5.      left += 1; right -= 1
#       else:
#           return False
#       return True



# s = "A man, a plan, a canal: Panama"
s = "race a car"

def is_palindrome(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    left=0
    right=len(s) - 1
    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


print(is_palindrome(s))