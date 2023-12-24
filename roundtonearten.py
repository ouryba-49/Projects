def round_sum(a, b, c):
  #round an int to the next multiple of 10, if its rightmost digit is 5 or more
  #round down to the previous multiple of 10 if its rightmost digit is less than 5
  #Given 3 ints, a b c, return the sum of their rounded values.
  x=round10(a)
  y=round10(b)
  z=round10(c)
  summ= x+y+z
  
  return summ
  
def round10(num):
    #num=float(num)
    #for i in num[0:]:
        #print(num[:-1])
        if num%10<5:
            num=num - (num % 10)
            
            return num
            #print(f"rounded is {num}")
        else:
         num=num + (10 - num % 10)
       
         return num
       # print(f"rounded is {num}")
       
x=round_sum(12,15,13)
print(f"{x}")

      


 