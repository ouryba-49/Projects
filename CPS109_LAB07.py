# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 09:35:35 2022

@author: OuryBah
"""

import random

print("\n#question 1:")

list_of_toss=[]
x=0
while x<20:
     r=random.randrange(0,7)
     list_of_toss.append(r)
     x+=1 
 
inRun=False
for i in range(len(list_of_toss)):  
     if inRun:
         if list_of_toss[i]!= list_of_toss[i-1]:
             print(')', end = '')
             inRun = False
     if not inRun:
         if i!= len(list_of_toss)-1:
             if list_of_toss[i]==list_of_toss[i+1]: 
                 print('(', end = '')
                 inRun = True
     print(list_of_toss[i],end='')
if inRun:
     print(')', end = '')

print("\n")
     
print("\n#question 2:")
    
    
L = [random.randrange(1, 7) for i in range(20)]
runs = []
#print(L)

inRun = False
run = ""
for i in range(len(L)):
    if inRun:
        if L[i] != L[i-1]:
           
            runs.append(run)
            run = ""
            inRun = False
            continue
        else:
            run += str(L[i])
    if not inRun:
        if i != len(L)-1:
            if L[i] == L[i+1]:
                run += str(L[i])

                inRun = True

runs = sorted(runs, key=len)
result = ""
if (len(runs) > 0):
    result = result.join(str(x) for x in L)
    result = result.replace(runs[-1], "(" + runs[-1] + ")" , 1)
print(result)

print("\n")
     
print("\n#question 3:")
    
"""Assume that L is a list of Boolean values, True and False.
Write a function longestFalse(L) which returns a tuple (start, end) representing the start and end 
indices of the longest run of False values in L. 
If there is a tie, then return the first such run. 
For example, if L is:
False False True False False False False True True False False
0     1     2    3     4     5     6     7    8    9     10
Then the function would return (3, 6), since the longest run of False is from 3 to 6."""

def longestFalse(L):
    start = None
    bestStart = None
    bestEnd = None
    for i in range(len(L)):
        if(L[i]==False and start==None):
            start = i
        if (L[i] == True) and (start!=None):
            if (bestStart == None) or ((i-1-start)>(bestEnd-bestStart)):
                bestStart = start
                bestEnd = i-1
            start = None
    if(L[-1]==False):
        if (bestStart == None) or ((len(L) - 1 - start) > (bestEnd - bestStart)):
            bestStart = start
            bestEnd = len(L)-1
    return bestStart,bestEnd

my_list=[False, False, True, False, False, False, False, True, True, False, False]

testq3=longestFalse(my_list)

print(testq3)

print("\n")
     
print("\n#question 4:")
def occupy(n):
    #assuming that each bird will choosethe nest in 
    #the middle of the largest unccupied run of nests.
    
    nest=['_']*n
    goal=['X']*n
    print(' '.join(nest))
    first=0
    last=n-1
    
    list_=[(first,last)]
    
    while nest!=goal:
        first,last = list_.pop(0)
        count=last- first+1
        
        if count % 2 == 0:
            middle=(first+last)//2 +1
        else:
            middle=(first+last)//2
        if nest[middle]=='X':
            continue
        nest[middle]='X'
        print(' '.join(nest))
        list_.append((first,middle-1))
        
        list_.append((middle + 1,last))

testq4=occupy(10)

print("\n")
     
print("\n#question 5:")
def isPalindrom(L):
    new_list = L.copy()
    new_list.reverse()
    if L==new_list:
        return True
    else:
        return False
list_= [5, 2, 9, 9, 2, 5]
testq5=isPalindrom(list_)

print(testq5)
    
    