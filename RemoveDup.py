"""
Remove duplicates from sorted array.
Example:
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
"""
def RemoveDup(nums):
    indextwo = 1
    if nums == []:
        return 0
    for i in range(len(nums)):
        if (i + 1 < len(nums)):
            if nums[i] < nums[i + 1]:
                nums[indextwo] = nums[i + 1]
                indextwo = indextwo + 1
    print (nums[:indextwo])
    print (indextwo)



nums= [1,1,2,3,4,5,5,6,7,8,9,9,9,10,11,11,12,13,14,14,15]
RemoveDup(nums)
