# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 09:13:34 2018

@author: ferna
"""

import math 


def solvequadratic(a,b,c):
    
    r = math.sqrt(a*b*c)
    
    
    return r, 3*r

a =float(raw_input('what is the coefficient of x^2?') )

#if type(a)== float or int:
b =float(raw_input('what is the coeficient of x?') )
    
   # if type(a)== float or int:
c =float(raw_input('what is the constant ?') )
       # if type(a)== float or int:#makes sure that answer is not string
        #        print 'good'
       # else:
         #       print'what you entered are not numbers'
         
r1,r2 = solvequadratic(a,b,c)
b1,b2 = solvequadratic(2*a,2*b,2*c)

 

print r1,r2,b1,b2


    
         
         
                