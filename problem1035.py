# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 01:23:46 2019

@author: NOBEL
"""

A, B, C, D = map(int,input().split())

if (B > C) and (D > A) and (C + D) > (A + B) and (A, B, C > 0):
	print("Valores aceitos")
else: 
    print("Valores nao aceitos")