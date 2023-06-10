#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def chechIfNotNumeric(*args):
    if x in args:
        if not(isinstance(x,(int,float))):
            return False
    return True

def addAllNumeric(*args):
    s = 0
    for x in args:
        s += x
    return s

myName = "python course"

