# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:45:33 2019

@author: ferna
"""

# this one is like your scripts with argv
def print_two(*args):# defines what function does
    arg1, arg2 = args # asks for arguments 
    print (f"arg1: {arg1}, arg2: {arg2}")
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):# args inside ()
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")   
print_none() 