# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 18:45:19 2022

@author: OuryBah
"""
global my_medications
global answer
#This program will track the drug intake of a patient 
#it will receive an input of the medication taken 
#the amount taken and the day
#it will output a message that congratulates the patient 
#tell them how many they have left to take that week.

#inputs:
#names of medications
#Quantity
#times needed per week
#days in a week

#task 1 the program will receive the names of the medications relate them to the number of pills per container.

number_of_medications=int(input("How many medications are you taking? "))

print("Enter the name of the medications and the corresponding amount per box:")
my_medications={}
count=0
while count< number_of_medications:
    name=input("Name:")
    total=int(input("Amount:"))
    my_medications[name]=total
    count+=1
    
list_meds=list(my_medications.items())

#Task2 the program asks the user how many times per week they need to take their meds

#def remainig_days():
 ##   for (k,v) in my_medications.items():
   #     pill_week=int(input(f"How many days per week do you take {k}")) # this holds an integer
    #    while True:
     #       answer=int(input("Did you take a medication today? 1 for yes 2 for no :"))
      #      if answer==1:
       #         pill_week-=1
        #        print(f"You have {pill_week} more {k} pills left for this week")
        
         #   elif answer==2:
          #      print(f"you did not take your medication, so you have {pill_week} pills left for this week")
           # else:
            #    print("Not matching")
            

#Task 2 : The program asks the user to confirm if they have taken their medications then to add the number of pills they
# have taken for each medication then return how many pills they have left to take during the week and how many they 
#have left in total

i=0
while True:
    answer=int(input("Did you take a medication today? 1 for yes 2 for no :"))
    if answer==1:
        print("Congratulations\n")
        while i<len(my_medications):
            for (k,v) in my_medications.items():
                pill_week=int(input(f"How many days per week do you take {k}"))
                num_pills=int(input(f"How many {k} pills did you take today:"))
                remaining_pills_total=v-num_pills
                pill_week-=1
                print(f"You have {pill_week} more {k} pills left for this week")
                print(f"And There are a total of {remaining_pills_total} pills left for {k} in the box")
                if (remaining_pills_total==0):
                    print("You need a refill")
                i+=1
        break
    elif answer==2:
        print(f"you did not take your medication, so you have {pill_week} pills left for this week")
        print("Take your medications")
        
    else:
        print("Enter a correct value")

#I need to create functions
#compare strings
#I need to restrict the user on the number of days they can enter which must be less then or equal to 7

        

        
    

##days_of_week={1:'Monday',2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}








    
    


