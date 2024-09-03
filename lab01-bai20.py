# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:40:31 2024

@author: Admin
"""

a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
c = float(input("Nhap so c: "))
highest = a
if b > highest:
    highest = b
if c > highest:
    highest = c
print("So lon nhat la:", highest)