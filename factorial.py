

def factorial(num):
    
    
    fact = 1
    for i in range(1,num+1):
      fact = fact*i
    return fact



def power_sum(num):
    
    
    sum = 0
    for i in range(1,num+1):
      sum = sum + 0.5**i
    return sum

num = int(input('Number'))


#fact = factorial(num)      function 1 stuff
#fact2 = factorial(num-1)
#print(fact)
#print (fact / fact2)


sum = power_sum(num)  # function 2 stuff
print(sum)