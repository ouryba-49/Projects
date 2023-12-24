 # a recursive function is a function that calls itself somewhere in the code.
#takes as an input argument a list of booleans, and returns a single boolean
#If there is nothing in the list then return False
#If there is only one boolean in the list then:
    #If the boolean is True return False
     #If the boolean is False return True
    # Otherwise,
       # If the length of the list is odd, return the “and” operator of RecursiveAndOrFlip of the first half of the list and RecursiveAndOrFlip of the second half of the list. 
       # If the length of the list is even, return the “or” operator of RecursiveAndOrFlip of the first half of the list and RecursiveAndOrFlip of the second half of the list.
#Note that in the case of a list with an odd length, let the first half take the extra element


def RecursiveAndOrFlip(list_1):
    if (len(list_1==0)):
        return False
    elif(len(list_1>=1)):
        for i in list_1[0:]:
            if list_1[i]== 1:
                list_1[i]== False
                return list_1
            elif list_1[i]== 0:
                list_1[i]== True
                return list_1
my_list=[True,False]
test= RecursiveAndOrFlip(my_list)
print(test)
    
          
    

            
        
    
    