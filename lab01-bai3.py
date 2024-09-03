# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:19:44 2024

@author: Admin
"""

a = int(input("Nhap so nguyen duong a : "))
b = int(input("Nhap so nguyen duong b: "))

if a > 0 and b > 0:
    x = a // b
    y = a % b
    print("Phan nguyên cua a chia cho b:", x)
    print("Phan du của a chia cho b:", y)
else:
    print("Nhap sai ! moi nhap lai.")




