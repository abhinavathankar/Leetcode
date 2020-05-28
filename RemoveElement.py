"""
Remove duplicate from array.
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
"""
def Remove(nums,val):
    count = 0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[count]=nums[i]
            count+=1
    print (count)
    print(nums[:count])


nums= [0,1,2,2,3,0,4,2]
val=2
Remove(nums,val)