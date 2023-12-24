"""Write a program that generates a sequence of 20 random die tosses 
and then prints the die values, marking the runs by including them 
in parentheses, like this: 1 2 (5 5) 3 1 2 4 3 (2 2 2 2) 3 6 (5 5) 6 3 1"""
import random 

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
             print(")")
             inRun = False
     if not inRun:
         if i!= len(list_of_toss)-1:
             if list_of_toss[i]==list_of_toss[i+1]: 
                 print("(")
                 inRun = True
     print(list_of_toss[i])
if inRun:
     print(")")
     
