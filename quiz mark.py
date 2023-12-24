# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:12:19 2022

@author: OuryBah
"""
def make_chocolate(small, big, goal):
    big_weight=5
    s_weight=1
    
    small= small* s_weight
    big= big * big_weight
    
  #how many small do we need with the bigs we have to reach the goal  
    if(small+big==goal):
        #return small
        print(f"small bar needed is {small}")
    elif(small+big<goal):
        #return -1
        print("-1")
    elif(small+big>=goal):
        small=goal-big
        #return small
        print(f"small bar needed is {small}")
    else:
        #return 0
        print(f"small bar needed is {small}")
    
 
   # s=(goal-big)/small
    #if((s+big)<goal):
     #   print("-1")
    #if(big<=goal):
         #print(f"small bar needed is {s}")
    
make_chocolate(1, 2 ,7)







