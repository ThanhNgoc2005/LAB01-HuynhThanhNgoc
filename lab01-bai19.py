# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:34:38 2024

@author: Admin
"""

a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
c = int(input("Nhap so nguyen c: "))
d = int(input("Nhap so nguyen d: "))
smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c
if d < smallest:
    smallest = d
print("So nho nhat la:", smallest)