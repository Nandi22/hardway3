# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:13:15 2019

@author: ferna
"""

from sys import argv 

script, user_name, pet = argv # how many arguments are needed
prompt  = 'type here'

print(f"Hi {user_name}, I'm the {script} script.")
print(f"You have a pet {pet}")
print("I'd like to ask you a few questions.")
print(f"Do you like me  {user_name}? ") 
likes = input(prompt) # prints pronpt (>)and expects answer

print(f"Where do you live {user_name}? ")
lives = input(prompt)

print("What kind of computer do you have? " )
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")      

