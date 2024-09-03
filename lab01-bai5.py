# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:24:59 2024

@author: Admin
"""

a=int(input("nhap so gio:"))
b=int(input("nhap so phut:"))
c=int(input("nhap so giay:"))
if a>=0 and a<24 and b>=0 and b<60 and c>=0 and c<=60:
    print("bay gio la:",a,"h:",b,"m:",c,"s")
    x=a*3600
    y=a*60
    print(" doi ra giay:",x+y+c,"s")
else:
    print("nhap sai ! moi nhap lai")