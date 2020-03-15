# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:46:01 2018

@author: ferna
"""

import cmath 


def solvequadratic(a,b,c): # defines function- (a,b,c) means that those variables are needed in function
    
    formula1 = -(cmath.sqrt((b*b)/4*(a*a)-(c/a)))-b/2*a                               #quadratic formula (negative)
    formula2 =  cmath.sqrt((b*b)/4*(a*a)-(c/a))-b/2*a                        # positive
    
    return formula1 , formula2                           # return alows you to call back result later in program

a =float(raw_input('what is the coefficient of x^2?') )

#if type(a)== float or int:
b =float(raw_input('what is the coeficient of x?') )
    
   # if type(a)== float or int:
c =float(raw_input('what is the constant ?') )
       # if type(a)== float or int:#makes sure that answer is not string
        #        print 'good'
       # else:
         #       print'what you entered are not numbers'
         
y,z = solvequadratic(a,b,c) # you need 2 variables becase the program has 2 things retured 


 

print y, z 
