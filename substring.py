# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 19:45:19 2018

@author: Adam Robinson
"""
s = str(input("Enter a string of letters: "))
index = 0
count = 1 # first letter in string is the current longest alpha string
result = s[0]
while index <= (len(s) - 1):
    # first cond prevents out of bounds index
    if index < (len(s) - 1) and s[index] <= s[index + 1]:
        count += 1 # if the next letter is greater (alphabetically) than the current index, add to count
    else: 
        if count <= len(result):
            count = 1 # resets counter if new string is smaller than previous largest and continues
        else: #if new string is bigger...
            result = s[index - count + 1: index + 1] # the new substring is our new longest
            count = 1 # reset counter to keep looking      
    index += 1
print("Longest substring in alphabetical order is: " + result)
