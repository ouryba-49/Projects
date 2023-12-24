# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 11:07:57 2022

@author: OuryBah
"""


"""Write a program sumDigits(stringofdigits) to add the digits from a string, where all of the letters are digits.  For example, sumDigits('123') prints 6, since 1 + 2 + 3 is 6.  What is sumDigits('09876543211234567890')?  Your answer should be a number.  
The function int() should help.  Your function should be written in the file test1.py."""

def sumDigits(stringofdigits):
    sum_= 0
    for x in stringofdigits:
        if x.isdigit():
            sum_+=int(x)
            
    return(sum_)
string=input("Enter a number: ")
ans=sumDigits(string)
print(ans)
"""Write a Python program to find all the numbers from 1 to 1000, inclusive, that are divisible by 7 but not by 5. 
 The sum of those numbers is:"""
summ=0
for num in range(1,1001):
    if (num%7==0 and num%5!=0):
        summ+=num
    print(summ)
    
"""Write a Python program that finds S = the sum of all the integers from 1 to N inclusive that evenly divide into N = 4312943

For example, if N = 10, then the sum S = 1 + 2 + 5 + 10 = 18

The value of S is:"""

def sumDivisble(N):
  sum=0
  for x in range(1,N+1):
    if (N%x== 0):
      sum+=x
  
  return sum

limit=int(input("Enter the limit: "))
function=sumDivisble(limit)
print(function)
 
    

    

