"""
Problem source: Leetcode
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


def TwoSum(nums, target):
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            print(h[n], i)

nums = [3,3,2,7,8,1,4,5]
target= 9

TwoSum(nums,target)