# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:10:44 2024

@author: Admin
"""

a=float(input(" nhap so chieu cao(m):"))
b=float(input(" nhap so can nang(kg):"))
if a>0 and b>0:
    BMI=b/a**2
    print("chi so BMI cua ban la :",BMI,)
else:
    print(" nhap sai! moi nham lai.")