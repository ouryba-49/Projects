# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

def getCircumference(rad):
    circ=math.pi*2*rad
    return circ

def getArea(rad):
    area = math.pi*rad**2
    return area


print("\nPython Circle Calculator")

radius= float(input("Enter raduis: "))# the float converts the inputed numeric value

c=getCircumference(radius)
a=getArea(radius)

print(f"Circumference = {c}") 
print(f"Area ={a}")

# the curly braces let python knows that the 
#variable in it has to be converted in to a float , the f is to let it know it is formated.


