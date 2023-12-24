def fibonnaci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)

def our_recursion(num):
  new_num=0
  if(num%2!=0):
    new_num= our_recursion(num-1)
  else:
    new_num=num*2 # Base case is an even num

  return new_num
  # This function will do one of two things
# If num is odd, it will recursively call itself on the next lowest number.Resulting in an even number then the base case will be performed.
# If the number is even, it will return a new number which is num * 2

def factorial(num):
# Base case is num == 0
   if(num < 1):
       return 1
   else:
       new_num = num * factorial(num - 1)
     
       return new_num


def print_recursively(num):
    if num == 0:
        print("Starting to print at 0")
        return 0
    else:
        a = print_recursively(num - 1)
        print("Now we are at ", a)
        return num
      
fact=factorial(5)
print(f"the factorial of this number is {fact}")

our_rec=our_recursion(10) 
print(our_rec)
    
fibo=fibonnaci(10)
print(fibo)


inp = int(input("What number of recursions would you like to see?")) 
print_recursively(inp)


    
