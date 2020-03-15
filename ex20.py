from sys import argv

script, input_file = argv # arguments,script name and file input

def print_all(f): # prints the script that has been read in the computer
    print(f.read())
    
def rewind(f): # function to move pointer back , f is for file
    f.seek(-5) #moves pointer to 0 (begging) of file

def print_a_line(line_count, f):
    print(line_count, f.readline()) #prints number of the line and reads line

current_file = open(input_file) # asigns new variable to opened file

print("First let's print the whole file:\n") # \n makes the stuff after it go on a new line

print_all(current_file) #reads and print the chosen file which has been opened inside computer

print("Now lets's rewind, kind of like a tape.")

rewind(current_file) # brings back pointer in file

print("Let's print three lines:")

current_line = 1 # gives argument value
print_a_line(current_line, current_file)#  prints number of next line and reads it

current_line = current_line + 1 # adds 1 to 
print_a_line(current_line, current_file)# 

current_line = current_line + 1 # with += say only current_line += 1   ,no assigning needed
print_a_line(current_line, current_file)
