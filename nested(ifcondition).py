#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = int(input())
if a > 10:
    print(">10")
    print("inside the top if")
    if a > 20:
        print(">20")
        print("inside the nested if")
        if a >30:
            print(">30")
            print("inside the nested if of nested if")
        else:
            print("<=30")
            print("inside the else part of nested if of nested if")
    else:
        print("<=20")
        print("inside the else part of nested if")
print("outside all ifs") 

