"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
"""
def majority_element(nums):
    nums.sort()
    return nums[len(nums)//2]

nums=[1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,4]
x=majority_element(nums)
print(x)