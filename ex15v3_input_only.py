# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:28:47 2019

@author: ferna
"""

#from sys import argv #not needed no arguments 

#script = argv # argument(not needed)

input_file = input("What file do you need to open?")

txt = open(input_file)# opens file

print(f"Here's your file {input_file}:")
print(txt.read())# prints file

print("Type the filename again:")
file_again = input("> ") #prints > and takes answer

txt_again = open(file_again)# opens file(makes object) 
# read() reads the file, result can be assigned to variable
print(txt_again.read()) #actually reads and prints it

input_file.close()
file_again.close()
 