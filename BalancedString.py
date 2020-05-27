"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.



Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
"""


def balance(s):
    countl = 0
    countr = 0
    counter = 0
    for i in range(0, len(s)):
        if s[i] == 'R':
            countr += 1
        if s[i] == 'L':
            countl += 1
        if countr == countl:
            counter += 1
    return counter

s = "RLRRLLRLRL"
x = balance(s)
print(x)

