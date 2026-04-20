"""
###################################################### PROBLEM 1 ######################################################################

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

    2 <= nums.length <= 104
     before IF-109 <= nums[i] <= 109
    -109 <= target <= 109

"""

# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 print(f"i: {i}; j: {j}")
#                 return [i, j]

# nums = [2,7,11,15]
# target = 9

nums = [3,2,4]
target = 6

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
       
# sum = two_sum(nums, target)
# print(sum)

"""

###################################################### PROBLEM 2 ######################################################################

Given an array of integers prices where prices[i] is the price of a stock on day i,
return the maximum profit you can achieve by buying on one day and selling on a later day.
You can only buy once and sell once. If no profit is possible return 0.
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price=1), sell on day 5 (price=6), profit = 6-1 = 5
Input:  prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: prices only go down, no profit possible
"""
prices = [7, 1, 5, 3, 6, 4]

def stock_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price 
    
        if profit > max_profit:
            max_profit = profit
        
    return max_profit

# # profit = stock_profit(prices)
# profit = stock_profit(prices)
# print(profit)


"""
###################################################### PROBLEM 3 ######################################################################

Contains Duplicate

Given an integer array nums, return True if any value appears at least twice, and False if every element is distinct.
Input:  nums = [1, 2, 3, 1]
Output: True
Input:  nums = [1, 2, 3, 4]
Output: False
Input:  nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: True

Before coding, answer these questions:
1. What am I given and what must I return?
    GIVEN AN IRRAY OF INTS AND HAVE TO RETURN TRUE IF DUPLICATE OR FALSE IF NOT DUPLICATES.
2. What do I need to check at each step?
    IF I HAVE SEEN THAT NUM BEFORE
3. Do I need a list, dict, or set?

"""

""" MY WAY """

nums = [1, 2, 3, 1]
# nums = [1, 2, 3, 4]

# def contains_duplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         else: 
#             seen.add(num)
#     return False

# print(contains_duplicate(nums))


""" CLAUDE CODE's WAY 

the else statement is not needed since this is what is called an early return

"""

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


"""
###################################################### PROBLEM 4 ######################################################################

Valid Anagram

Given two strings s and t, return True if t is an anagram of s, and False otherwise.
An anagram is a word formed by rearranging the letters of another word using all original letters exactly once.
Input:  s = "anagram", t = "nagaram"
Output: True
Input:  s = "rat", t = "car"
Output: False
Input:  s = "cat", t = "act"
Output: True

Before coding, answer these questions:
1. What am I given and what must I return?
    GIVEN 2 STRING, TRUE IF ANAGRAM OR FALSE IF NOT ANAGRAM.
2. What makes two strings an anagram?
    THAT WITH ONE WORD I CAN RECREATE A DIFFERENT WORD USING THE LETTER OF THE FIRST ONE.
3. What do I need to track for each string?
    EACH LETTER
4. List, dict, or set?
    DICT




"""
# s = "anagram"
# t = "nagaram"

s = "rat" 
t = "car"

def valid_anagram(s, t):
    if len(s) != len(t):           # quick check — if lengths differ
        return False         # can't be an anagram

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1     # add 1 to the count each time you see it
      
    for char in t:
        count[char] = count.get(char,0) - 1  # subtract 1 each time you see it in t
   
    for val in count.values():
        if val != 0:       # if any count isn't 0
            return False     # letters don't match

    return True

# result = valid_anagram(s, t)
# print(result)



"""
###################################################### PROBLEM 5 ######################################################################
============================================
LeetCode #125 - Valid Palindrome
Difficulty: Easy
Pattern: Two Pointers
============================================

A phrase is a palindrome if, after converting all uppercase letters
into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward.

Given a string s, return True if it is a palindrome, False otherwise.

Example 1:
Input:  s = "A man, a plan, a canal: Panama"
Output: True
Explanation: "amanaplanacanalpanama" is a palindrome

Example 2:
Input:  s = "race a car"
Output: False
Explanation: "raceacar" is not a palindrome

Example 3:
Input:  s = " "
Output: True
Explanation: empty string after cleaning is a palindrome


"""


s = "A man, a plan, a canal: Panama"

def is_palindrome(s):
    new_s = "".join([char for char in s if char.isalnum()]).lower()
    left = 0
    right = len(new_s) - 1

    while left < right:
        if new_s[left] != new_s[right]:
            return False
        left += 1
        right -= 1

    return True     
    
# print(is_palindrome(s))

"""
###################################################### PROBLEM 6 ######################################################################

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
    The input is generated such that a majority element will exist in the array.

 
Follow-up: Could you solve the problem in linear time and in O(1) space?

"""

# nums = [3,2,3]
nums = [2,2,1,1,1,2,2]

def mayority_num(nums):
    best_num = None
    best_value = 0
    seen = {}
    for i in range(len(nums)):
        seen[nums[i]] = seen.get(nums[i], 0) + 1 
    for key, value in seen.items():
        if value > best_value:
            best_value = value
            best_num = key
    return best_num
    
# may_num = mayority_num(nums)
# print(may_num)



"""
# Input:
# Output:
# Pattern:
# Why:

# Input:  one string
# Output: True or False
# Pattern: Two Pointers
# Why: comparing from both ends, just existence check

# """
"""
# ============================================
# LeetCode #283 - Move Zeroes
# Difficulty: Easy
# Pattern: Two Pointers
# ============================================
#
# Given an integer array nums, move all 0's to the end
# while maintaining the relative order of the non-zero elements.
# You must do this IN PLACE (modify the original array, no new array)
#
# Example 1:
# Input:  nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
#
# Example 2:
# Input:  nums = [0]
# Output: [0]
#
# Example 3:
# Input:  nums = [1, 0, 1]
# Output: [1, 1, 0]
#
# ============================================

# Input: a list of numbers
# Output: a "sorted" list where 0 are at the end of the list (in place)
# Pattern: 
# Why:

"""

nums = [0, 1, 0, 3, 12]
# nums = [1, 0, 1]
# nums = [0]

# def move_zeroes(nums):

#     for n in nums:
#         if n == 0:
#             nums.remove(0)
#             nums.append(0)
#     return nums

# new_n = move_zeroes(nums)
# print(new_n)

def move_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]  # place non-zero at slow position
            slow += 1
    
    # fill the rest with zeros
    while slow < len(nums):

        nums[slow] = 0 #fix this (is wrong added because back to work)
        slow += 1
    
    return nums

"""
# new_n = move_zeroes(nums)
# print(new_n)

# ============================================
# LeetCode #26 - Remove Duplicates from Sorted Array
# Difficulty: Easy
# Pattern: Two Pointers (Same Direction)
# ============================================
#
# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates IN PLACE so each unique element appears only once.
# Return k — the number of unique elements.
#
# The first k elements of nums should hold the unique values.
# What remains after k doesn't matter.
#
# Example 1:
# Input:  nums = [1, 1, 2]
# Output: k = 2, nums = [1, 2, _]
#
# Example 2:
# Input:  nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: k = 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
#
# ============================================

Input:
Output:
Pattern:
Why:



"""
nums = [1, 1, 2]
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

def remove_duplicates(nums):
    pass

print(remove_duplicates(nums))



