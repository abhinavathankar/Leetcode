def missing_number(nums):
    length = len(nums)
    # using gauss formula
    real_sum = (length * (length+1))//2
    expected_sum = sum(nums)
    return real_sum - expected_sum

nums = [0,1,2,3,4,5,6,8]
x = missing_number(nums)
print(x)