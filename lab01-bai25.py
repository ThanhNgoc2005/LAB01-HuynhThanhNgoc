# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:29:09 2024

@author: Admin
"""

a = input("Nhap mot chu cai: ")
if a.islower():
    x = a.upper()
elif a.isupper():
    x = a.lower()
else:
    x = "Khong phai chu cai hop le."
print("Chu cai sau khi chuyen doi la:", x)