"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""


def defangip(address):
    s=''
    for i in address:
        if i=='.':
            s=s+'[.]'
        else:
            s=s+i
    return s

address='1.1.1.1'
x=defangip(address)
print(x)