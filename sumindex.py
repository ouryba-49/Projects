# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:08:57 2022

@author: OuryBah
"""
"""Write a function sumIndices(string), which considers each letter of the parameter string and checks what is the index of that letter in the alphabet, and adds that index to a running sum.  (The find() method will help).  The function prints the sum of the indices.  If a letter is not found in the alphabet, then -1 is added to the sum.  Thus sumIndices('ab') is 1 because 'a' has index 0 in the alphabet, and 'b' has index 1 and 0 + 1 is 1.  Similarly sumIndices('cab') is 3.  However, sumIndices('cab.') is 2, since '.' is not in the alphabet and it contributes -1.    Note, alphabet is 'abcdefghijklmnopqrstuvwxyz'.  You can assume that capital letters are not in the alphabet. 

What does your program print for sumIndices('I went to town!') ?"""

def sumIndices(string):
    sum_=0
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for x in string:
        letter=x.lower()
        index= alphabet.find(letter)  
        sum_+=index
       
    return sum_

string_=input("Enter a string: ")

r=sumIndices(string_)

print(r)




            
    