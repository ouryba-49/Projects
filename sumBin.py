# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 11:45:16 2022

@author: OuryBah
"""

"""Note that the Python built in function bin(n) converts a decimal
number n to binary, and int(b, 2) converts a string representation of
a binary number to a decimal number. For example bin(3) is '0b11',
and int('11', 2) is the same as int('0b11', 2) which is 3. You can
use either of these functions to answer this question.

Write a Python program to find the sum of the binary numbers
in list L, where the binary numbers do not have the quote marks
necessary for the int() function. For example, if
L = [101, 11, 1010]
then the sum is 5 + 3 + 10 = 18.

What is the sum when L is
L = [10100, 101000, 100000, 1011111, 1000, 1010111, 1010010, 11001, 101100, 10111, 11011, 1011010, 11101, 10, 110011, 1001111, 110010, 101100, 100001, 111001]
"""
def sumBin(L):
    sum=0
    for x in L:
        binary=str(x)
        decimal=int(binary,2)
        sum+=decimal
    return sum

        
L=[10100, 101000, 100000, 1011111, 1000, 1010111, 1010010, 11001, 101100, 10111, 11011, 1011010, 11101, 10, 110011, 1001111, 110010, 101100, 100001, 111001]      

func=sumBin(L)
print(func)