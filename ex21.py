def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b 

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b # prints result in computer, ex- print(subtract(a,b)) can be asked
#return allows result to be used later,ex(printed or assigned to a variable
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b

def divide(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)            # assigns varibles to values(from function)
height = subtract(78, 4)
weight = multiply(90, 2) 
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")# prints values


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print ("That becomes: ", what, "Can you do it by hand?")

