def palindrome(x):
    string = str(x)
    palstr= string[::-1]
    if palstr == string:
        print("Palindrome")
    else:
        print("false")

x = 1212
palindrome(x)
