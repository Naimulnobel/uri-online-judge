# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 17:48:33 2019

@author: Student Mct
"""

a=int(input())
b=int(input())
c=int(input())
ab=(a+b+abs(a-b))//2
abc=(ab+c+abs(ab-c))//2
print(str(abc),'eh o maior')