# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:14:22 2022

@author: OuryBah
"""

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
        