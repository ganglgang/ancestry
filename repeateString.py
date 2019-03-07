#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:59:50 2019

@author: gangliu
"""

# ask input from user
name = input("Enter your string you want:")
print("Your input is " + name)
char_dict ={}

# store each char with position to dict ignore case
for i in range(len(name)):
    if name[i].isalpha()==False:
        char_dict ={}
        print('the \''+str(name[i])+'\' is not char...')
        break;
    else:
        if name[i].lower() in char_dict:
            char_dict[name[i].lower()]=char_dict[name[i].lower()]+','+str(i)
        else:
            char_dict[name[i].lower()] = str(i)


# sort dict according to the amount of elements    
result =  ''.join(sorted(char_dict, key=lambda k: len(char_dict[k]), reverse=False))  

# rebuild string
sol = ""
for j in result:
    chara = ''.join(char_dict[str(j)]).split(',')
    for i in chara:
        sol+=name[int(i)]
if sol[0].lower()==sol[1].lower():
    print('No letter that is not repeated')
else:
    print('The first letter without repeat is : '+str(sol[0]))
    
print('re-string:'+ str(sol))
