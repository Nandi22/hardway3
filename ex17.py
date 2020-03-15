# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:20:44 2019

@author: ferna
"""

from sys import argv 
from os.path import exists 

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)# assigns opened file to another name 
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")# len is size in bytes

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continute, CTRL-C to abort." )
input()# Any input 

out_file = open(to_file, 'w+')# w+ is read and write, opens and truncates the file, and assigns a variable to it

print("indata: ", indata)

out_file.write(indata) # writes file assigned to indata in the outfile

print("Alright, all done. This is the new file: ")

 
out_file.close()# has to close and reopen to refresh and print new text
in_file.close()
