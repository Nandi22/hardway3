import math as m
def list_of_primes(max_num):
    
    
     
    
#    for i in range(2,int(m.sqrt(num)+1)):
    count = 0
    for j in range (2,max_num):
        primeN = True
        for i in range(2,int(m.sqrt(j)+1)):
        
            if (j%i) == 0 :
                primeN = False
                break
  
            
        if primeN == True:
            count = count +1
            print("The  ", count, " prime is", j)
        
        
list_of_primes(100)