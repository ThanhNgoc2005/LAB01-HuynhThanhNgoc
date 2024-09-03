# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:46:37 2024

@author: Admin
"""
import math
a=float(input(" nhap vao ban kinh cua hinh tron :"))
if a>=0:
   x=2*math.pi*a
   y=math.pi*a**2
   print(" chu vi hình tron la :",x,)
   print(" dien tich hinh tron la :",y,)
else:
    print("Nhap sai ! moi nhap lai.")
    