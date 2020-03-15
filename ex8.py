# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 20:09:58 2019

@author: ferna

"""
# formatter is a made up function
formatter = " {} {} {} {} " # 4 {}'s means that there are 4 arguments needed
# each line has 4 different arguments for the the function to take
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
    
