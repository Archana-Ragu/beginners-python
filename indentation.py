#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#single line comment
"""
user will enter a floating point number lets say 238.915 . your task is to
find out the integer portion before the  point ( in this case 238)
and then check if that integer portion is an even number or not?
"""
x = float(input("enter a real number:"))
y = round(x)  #helps?
if y>x:
    intPortion = y-1 #29.5                          
else:
    intPortion = y
print(intPortion)    


# In[ ]:


# real sum

x = float(input("enter a real number:"))
y = round(x)
if x>0:
    if y>x:
        intPortion = y-1
    else:
        intPortion = y
else:
    if y<x:
        intPortion = y+1
    else:
        intPortion = y
if(intPortion%2) == 0:
    print("even")
else:
    print("odd")

