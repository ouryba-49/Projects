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
        for i in big:
            if i=1
      #check how many big can be used, if the total number of big is greater than the goal
      #use one first and check if it equate the goal
      #in that case small is 0
      #if not
      #check the total number of small u have and how much you can add to big to achieve the goal
      #repeat the process, if all big are used and small without reaching the goal then return 1
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







