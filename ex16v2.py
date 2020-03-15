# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:17:04 2019

@author: ferna
"""

from sys import argv 

script, filename = argv # arguments needed 

print(f"We're going to erase {filename}." )
print("If you don't want that say anything but yes.") 
print("If you do want that, say 'yes' ")

if input("?") == "yes":

    print("Opening the file...")
    target = open(filename, 'w')

    print("Truncating the file. Goodbye!")
    target.truncate()

    
    print("Now I'm going to ask you for three lines.")

    line1 = input("line 1: ")
    line2 = input("line 2: ")
    line3 = input("line 3: ")

    print("I'm going to write these to file.")

    target.write(line1) 
    target.write("\n")
    target.write(line2)
    target.write("\n") 
    target.write(line3)

    print("And finally, we close it.")
    target.close()
else:
    print("Ok I won't delete the file")
