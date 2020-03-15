# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:28:47 2019

@author: ferna
"""

from sys import argv

script, filename = argv # arguments

txt = open(filename)# opens file

print(f"Here's your file {filename}:")
print(txt.read())# prints file

print("Type the filename again:")
file_again = input ("> ") #prints > and takes answer

txt_again = open(file_again)# opens file(makes object) 
# read() reads the file, result can be assigned to variable
print(txt_again.read()) #actually reads and prints it

filename.close()
file_again.close()
