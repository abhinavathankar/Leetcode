def plusone(digits):
    length=len(digits)
    if digits[-1]==9:
        digits[-1]=0
    else:
        digits[-1]=digits[-1]+1
        return digits

    for i in range(length-2,-1,-1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i] + 1
            return digits
            break
    digits[0]==0
    digits.insert(0,1)
    return  digits

digits=[1,9,9]
x=plusone(digits)
print(x)