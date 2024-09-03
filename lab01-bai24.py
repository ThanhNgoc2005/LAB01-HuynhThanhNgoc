# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:21:42 2024

@author: Admin
"""

a = int(input("Nhap gio : "))
b = int(input("Nhap phut : "))
c = int(input("Nhập giay : "))

if 0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 59:
    print("Gio , phut, giay hop le.")
else:
    print("Gio , phut , giay khong hop le.")