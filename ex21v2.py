def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b 

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b # prints result in computer, ex- print(subtract(a,b)) can be asked

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

def square(a):
    print(f"SQUARING {a}*{a}")
    return a*a


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print ("That becomes: ", what, "Can you do it by hand?")

#same thing as line 35
res=divide(iq, 2)         #assingning result to res 
res2=multiply(weight,res) # Using result in function and assinging that result to res2 
res3=subtract(height,res2)#
res4=add(age, res3)       #
print (res4)              #


print (res4 * square(3))# using new function
#cels = (fahr-32)*5/9
fahr = 70
cels = multiply(5/9,subtract(fahr,32))
print(f"{fahr} fahrenhiet is {cels} celsius")# prints final result
                                  







