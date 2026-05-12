
# 2. Plus One #66 — Array Basics
# python# ============================================
# LeetCode #66 - Plus One
# Difficulty: Easy
# Pattern: Array Basics
# ============================================
#
# Given a large integer represented as an array of digits,
# add one to the integer and return the result as an array.
#
# Example 1:
# Input:  digits = [1,2,3]
# Output: [1,2,4]
#
# Example 2:
# Input:  digits = [1,2,9]
# Output: [1,3,0]
#
# Example 3:
# Input:  digits = [9,9,9]
# Output: [1,0,0,0]
# ============================================

# INPUT: a large interget in an array of digits    
# OUTPUT: same array modified   
# OPERATION: compare(primary) → rearrange → collect
# PATTERN: dict (modify existing list by adding 1 to the end)
# DS: dict      
# PLAN:
#   1. loop through digits:
#   2. if digits[-1] != 9:
#   3. add 1 to number and return dict
#   4. if digits[-1] == 9:
#   5. convert 9 to 0 and add 1 to next number
#      digit.insert(0, 1)


digits = [1, 2, 3]
# digits = [1, 2, 9]
# digits = [9, 9, 9]

def plus_one(digits):
    for n in range(digits[-1], -1, -1):
        if digits[n] != 9:
            digits[n] += 1
            return digits
        print(n)
   

print(plus_one(digits))






# INPUT: a large interger broken down in an array
# OUTPUT: same array of large integer modified
# OPERATION: find(primary) → look up → collect
# PATTERN: list (look for last number to add 1) return modified list   
# DS: list       
# PLAN:
#   1. loop through digits
#   2. if last digits not equals 9
            #add 1 to last digit and return list
#   3. if last digit is iqual to 9
#           change last digit to 0 and add 1 to next number
#      if end of loop and not more digits insert 1 in position 0


