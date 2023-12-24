# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 08:18:07 2022

@author: OuryBah
"""

secret_indices = [64, 1162, 561, 6801, 79, 14636, -1, 1670, 2300, 6, 31868, 130, 93, 413, 1663, -1, 124, 9991, 61592, 436, 1413, 1663, 2553, 51544, 8, -1, 1670, 1791, 406, 1669, 274, 303, 324, 87, 3664, -1, -1, 1663, 3965, 2166, 79, 4167, 1670, 4136, 1663, 2553, 12194, -1, 37148, 79, 474, 1670, 24496, -1, -1, 2227, 77, 79, 18935, 1670, 247, -1, 2227, 77, 79, 1841, 1670, 359, -1, 2227, 77, 79, 3795, 32213, 130, 5633, 1670, -1, 2227, 77, 79, 474, 1670, 19153, -1, 2227, 77, 79, 1868, 100563, -1, 2227, 77, 79, 4167, 124, 16102, 130, 8580, 1670, -1, -1, 64, 315, 3923, 1422, 87, 110, 93, 848, -1, 2232, 3087, 1033, 257, 8580, 1085, 1670, 1162, 3453, 1453, 79, 1868, 10, -1, 4720, 64, 163, 2300, 1413, 436, 257, 77, 106, -1, 64, 2300, 6, 9336, 130, 64, 1162, 77, 79, 20467, 10, -1, -1, 130, 1196, 1670, 5353, 2395, 4136, 1663, 2553, 12194, -1, 413, 406, 4167, 2395, 1670, 1162, 3453, 56395, 79, 2396, -1, -1, 2227, 77, 79, 18935, 1670, 247, -1, 2227, 77, 79, 1841, 1670, 359, -1, 2227, 77, 79, 3795, 32213, 130, 5633, 1670, -1, 2227, 77, 79, 474, 1670, 19153, -1, 2227, 77, 79, 1868, 100563, -1, 2227, 77, 79, 4167, 124, 16102, 130, 8580, 1670, -1, -1, 2227, 77, 79, 18935, 1670, 247, -1, 2227, 77, 79, 1841, 1670, 359, -1, 2227, 77, 79, 3795, 32213, 130, 5633, 1670, -1, 2227, 77, 79, 474, 1670, 19153, -1, 2227, 77, 79, 1868, 100563, -1, 2227, 77, 79, 4167, 124, 16102, 130, 8580, 1670, -1, -1, 64, 315, 3923, 1422, 87, 110, 93, 848, -1, 2232, 3087, 1033, 257, 8580, 1085, 1670, 1162, 3453, 1453, 79, 1868, 10, -1, 4720, 64, 163, 2300, 1413, 436, 257, 77, 106, -1, 64, 2300, 6, 9336, 130, 64, 1162, 77, 79, 20467, 10, -1, -1, 1663, 3965, 2166, 79, 4167, 1670, 4136, 1663, 2553, 12194, -1, 37148, 79, 474, 1670, 24496, -1, -1, 2227, 77, 79, 18935, 1670, 247, -1, 2227, 77, 79, 1841, 1670, 359, -1, 2227, 77, 79, 3795, 32213, 130, 5633, 1670, -1, 2227, 77, 79, 474, 1670, 19153, -1, 2227, 77, 79, 1868, 100563, -1, 2227, 77, 79, 4167, 124, 16102, 130, 8580, 1670, -1, -1, 2227, 77, 79, 18935, 1670, 247, -1, 2227, 77, 79, 1841, 1670, 359, -1, 2227, 77, 79, 3795, 32213, 130, 5633, 1670, -1, 2227, 77, 79, 474, 1670, 19153, -1, 2227, 77, 79, 1868, 100563, -1, 2227, 77, 79, 4167, 124, 16102, 130, 8580, 1670, -1, -1, 2227, 77, 79, 18935, 1670, 247, -1, 2227, 77, 79, 1841, 1670, 359, -1, 2227, 77, 79, 3795, 32213, 130, 5633, 1670, -1, 2227, 77, 79, 474, 1670, 19153, -1, 2227, 77, 79, 1868, 100563, -1, 2227, 77, 79, 4167, 124, 16102, 130, 8580, 1670]

decoder_dict={}


myfile = open('A_Tale_Of_Two_Cities.txt', encoding='utf-8')

myfile.seek(2825)

str_1= myfile.read()


str_list=str_1.split()

for x in secret_indices:
    decoder_dict[x]=str_list[x]
    
        
print(decoder_dict)      
            
running_str=""

for i in secret_indices:
    if i==-1:
        running_str+="\n"
        
    else:
        running_str+= decoder_dict[i]+ " "
print(running_str)
    

myfile.close()

with open("decoded_message.txt","w") as output:
    output.write(running_str)
    


