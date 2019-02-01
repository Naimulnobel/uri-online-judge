# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 00:26:41 2019

@author: NOBEL
"""

a=int(input())
b=int(a/3600)
c=int(a%3600/60)
d=int(a%3600)%60
print(str(b)+':'+str(c)+':'+str(d))