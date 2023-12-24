# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:26:12 2022

@author: OuryBah
"""
#Bisection search
#a value n such that n*n is equal to the number we want or very close enough by checking if the target number is
#within some epsilon value, example:
import math   

x=77 
eps=1 
lo=0

hi=x

guess=(lo+hi)/2 #initial guess
n=1

while abs(guess*guess-x)>=eps: #close enough? yes, exit;no,refibe
    if guess*guess< x:
        lo= guess
    else:
        hi= guess
    guess=(lo+hi)/2
    n+=1
    
    print(f"After {n} guesses: ")
    print(guess)




print(math.sqrt(x))
    
