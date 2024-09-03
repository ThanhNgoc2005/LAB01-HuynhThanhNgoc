# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:16:38 2024

@author: Admin
"""

import math
a=float(input("Nhap so a:"))
b=float(input("Nhap so b:"))
x=((((a+b)/(pow(a,1/3) +pow(b,1/3)))-(pow(a*b,1/3)))/pow((pow(a,1/3)-pow(b,1/3)),2))
print("Ket qua la:",round(x,3))