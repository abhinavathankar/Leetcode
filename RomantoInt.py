#Roman to Integer conversion
def romanToInt(str):
    constant = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    length = len(str)
    previous = 0
    newValue = 0
    #going right to left
    for i in range(length - 1,-1,-1):
        if constant[str[i]] >= previous:
            newValue += constant[str[i]]
        elif constant[str[i]] <= previous:
            newValue -= constant[str[i]]
        else:
            return 0
        previous = constant[str[i]]
    print(newValue)

str ="XI"
romanToInt(str)

