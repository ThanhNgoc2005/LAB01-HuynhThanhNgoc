# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:12:51 2024

@author: Admin
"""

a = int(input("Nhap ngay (dd): "))
b = int(input("Nhap thang (mm): "))
c = int(input("Nhap nam (yyyy): "))
if 1<=a<=31 and 1<=b<=12 and 1100<=c :
    a=str(a)
    b=str(b)
    c=str(c)
    print(a+"/"+b+"/"+c)
    print(a+"/"+b+"/"+c[2:4])
    print(c+"/"+b+"/"+a)
else:
    print(" Nhap sai ! Moi nhap lai . ")
    
