# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:13:00 2022

@author: OuryBah
"""

#anagrams: when two strings have the same characters that can be rearranged.
# iterate through the first string, for every character in s1, if it is in s2, 
#rmove it. If the character can't be removed in s2 and not at the end of s1 then they are not anagrams.
def is_anagram(s1,s2):
    #first method:
    #for c in s1:
     #   sn=s2.replace(c,'',1) 
      #  if sn == s2:
       #     return False
        #s2=sn
    #return s2==''
    
    #second method
    s1=list(s1)
    s1.sort()
    s1=''.join(s1)
    
    s2=list(s2)
    s2.sort()
    s2=''.join(s2)
    
    return s1==s2
    
    #3rd method
    #return sorted(s1)==sorted(s2)
print(is_anagram("ate","eat"))