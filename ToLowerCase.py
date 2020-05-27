"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.



Example 1:

Input: "Hello"
Output: "hello"
"""


def tolowercase(str):
    str = str.lower()
    return str

str = "Hello"
x= tolowercase(str)
print(x)