# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:06:51 2024

@author: Admin
"""

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

if a == 0:
   print(" phuong trinh vo nghiem ")
elif a>0:
    print(" phuong trinh co nghiem la",-b/a)
else:
    print(" phuong trinh co nghiem la ",b/a)