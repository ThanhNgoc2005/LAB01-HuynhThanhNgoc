# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:49:46 2024

@author: Admin
"""

 
h1 = int(input("Nhao vao thoi gian thu 1 \n\tGio: "))
p1 = int(input("\tPhut: "))
s1 = int(input("\tGiay: "))

h2 = int(input("Nhap vao thoi gian thu 2 \n\tGio: "))
p2 = int(input("\tPhut: "))
s2 = int(input("\tGiay: "))

if ( 0 <= h1 < 24 and 0 <= p1 < 60 and 0 <= s1 < 60
    and 0 <= h2 < 24 and 0 <= p2 < 60 and 0 <= s2 < 60):
    giay1 = h1 * 3600 + p1 * 60 + s1
    giay2 = h2 * 3600 + p2 * 60 + s2

    tonggiay = giay1 + giay2
    giotong = tonggiay // 3600
    tonggiay = tonggiay % 3600
    phuttong = tonggiay // 60
    giaytong = tonggiay % 60
    print("Tong hai gio la : ",giotong,"gio",phuttong,"phut",giaytong,"giay")

    if giay1 < giay2:
        giay1, giay2  = giay2, giay1
    hieugiay = giay1 - giay2
    giohieu = hieugiay // 3600
    hieugiay = hieugiay % 3600
    phuthieu = hieugiay // 60
    giayhieu = hieugiay % 60
    print("Hieu hai gio la : ",giohieu,"gio",phuthieu,"phut",giayhieu,"giay")
else:
    print(" Nhap sai ! moi nhap lai !")