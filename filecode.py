# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:33:42 2022

@author: OuryBah
"""

file=open("words.txt")
print(file.tell())
str1=file.read(8)

print(str1)
#the new line character is counted
print(file.tell()) ##print the location
file.seek(0)#bring us back to the first byte
str1=file.read(8)
print(str1)

file.seek(5000)
str2=file.read(15)
print(str2)

file.seek(0)

for x in range(5):
    print(file.readline()) #this prints line by line including the new line white space.
    
for x in range(10):
    print(file.readline(), end='')## this reads from the file until the end given the limit without a balnk line in between

##if we want to read from the beginning of the file to the end, we can loop through like a list.

#for line in file:
    #print(line, end='') #prints every line until the end
    
#if we have  multiple words per line
#And want to read one word at a time, instead of a whole line
#we can print a line and split the words.
file.close()

file2= open("programming.txt")

for x in range(10): #it goes up to line 10 and return that one because it will forget the other lines
    
    line=file2.readline()
    
print(line)

words=line.split()

print(words)

file2.close()

##Ways of reading a file:
    #text = file.readlines()
#text = list(file)


