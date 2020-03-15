# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 18:53:37 2019

@author: ferna
"""

# to run in Spyder run as 
# runfile('ex13.py',wdir='C:/Users/ferna/python_scripts/hard_way_3', args = 'arg1 arg2 arg3')
# where arg1 arg2 arg3 are 3 arguments

from sys import argv 
# read the WYSS section for how to run this 
script, first , second, third = argv

print("The script is called:", script) # name of script not variable
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


 