# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 19:45:19 2018

@author: macro
"""
s = str(input("Enter a string of letters: "))
index = 0
count = 1
result = s[0]
while index <= (len(s) - 1):
    if index < (len(s) - 1) and s[index] <= s[index + 1]:
        count += 1
    else:
        if count <= len(result):
            count = 1
        else:
            result = ""
            result += s[index - count + 1: index + 1]
            count = 1      
    index += 1
print("Longest substring in alphabetical order is: " + result) # should be bklm
