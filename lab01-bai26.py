# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:11:37 2024

@author: Admin
"""


a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a, b, c)
x = input("Nhap so nguyen N: ")
y = ''.join(sorted(x))
print(y)
