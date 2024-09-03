# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:47:47 2024

@author: Admin
"""

a = int(input("Nhap mot so nguyen: "))
number_words = { 0: "Khong",  1: "Mot", 2: "Hai", 3: "Ba", 4: "Bon", 5: "Nam", 6: "Sau", 7: "Bay", 8: "Tam", 9: "Chin"}

if a in number_words:
    print(number_words[a])
else:
    print("Khong doc duoc")
