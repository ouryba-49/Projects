# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:07:29 2022

@author: OuryBah
"""
import math
import random
#Factorial For Loop:
def factorial(n):
    a=1
    for x in range(n,1,-1):
        a= a * x
    return a

print(math.factorial(5))

#Max value for loop:
    
def find_max(list_):
    max_=list_[0]
    for x in list_:
        if x>max_:
            max_=x
    return max_

#min value with for loop:
    
def find_min(seq):
    min_=seq[0]
    for x in seq:
        if x<min_:
            min_=x
    return min_
  
def out_new_list(list_):
    new_list=[]
    total=0
    for x in list_:
        total+=x
        new_list.append(total)
    return new_list

#dice rolling
def roll_dice(n,faces=6):
    rolls=[]
    rand=random.randrange #to generate the rand function
    
    for x in range(n):
        rolls.append(rand(1,faces+1))
        
    return rolls

#snake eye

def roll_snake_eyes():
    rand=random.randint
    count=1 
    for x in range(10):
        a,b = rand(1,6) , rand(1,6)
        count+=1
        if(a+b==2):
            return count
    return -1


def roll_snake_eye():
    rand=random.randint
    count=1
    a,b =rand(1,6) , rand(1,6)
    while (a+b!=2):
        a,b =rand(1,6) , rand(1,6)
        count+=1
    return count
x=roll_snake_eye()
print(x)

        


#enumerate to find the index of a value in a list:
    
nums=[1,1,2,3,5,8,13,21]

e=enumerate(nums)
li_e=list(e)
print(li_e)

l=[x for (i,x) in e if i%2==1]
print(l)

       

