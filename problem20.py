# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 00:40:56 2019

@author: NOBEL
"""

n=int(input())
y=int(n/365)
m=int((n%365)/30)
d=int((n%365)%30)
print(str(y),'ano(s)')
print(str(m),'mes(es)')
print(str(d),'dia(s)')