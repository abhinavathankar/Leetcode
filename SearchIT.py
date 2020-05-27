"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
"""

def search_insert_target(nums,target):
    for i in range(len(nums)):
        if target==nums[i]:
            return i
        if target!=nums[i]:
            if target<=nums[i]:
                return i
            if target>nums[-1]:
                return len(nums)

nums=[1,3,5,6]
target=5

x=search_insert_target(nums,target)
print(x)