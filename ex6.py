# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:13:28 2019

@author: ferna
"""
# assigns 10 for number of people
types_of_people = 10
# has embedded strigs in the string, f is needed before string if there's embedded string
x =f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print (x)
print (y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
# {} is space for False 
joke_evaluation = "Isn't that joke so funny?! {} "
# formats previous  sting including if it is hilarious(true or false)
print(joke_evaluation.format(hilarious))

w ="This is the left side of..."
e ="a string with a right side."
# adds strings
print(w + e)