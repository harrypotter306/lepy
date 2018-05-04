#This file is used to solve a*x^2+b*x+c==0
#only int or float input is allowed
#only the real roots could be gotten
import math
def quadratic(a,b,c):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        delta=b**2-4*a*c
        if delta>=0:
            x1=(-b+math.sqrt(delta))/(2*a)
            x2=(-b-math.sqrt(delta))/(2*a)
            return x1,x2
        else:
            print('There is no real roots in this equation')
            return None
    else:
        print('TypeError: bad operand type')
        return None