def ReverseInt(x):
    if x > 0:
        number = int(str(x)[::-1])
    if x < 0:
        number = -1 * int(str(x*-1)[::-1])
    #handle 32bit overflow
    min= -2**31
    max= 2**31-1
    if number not in range(min,max):
        return 0
    else:
        return number

x= 1232
ReverseInt(x)