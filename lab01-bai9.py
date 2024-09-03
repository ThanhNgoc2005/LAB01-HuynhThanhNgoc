# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:34:44 2024

@author: Admin
"""

print(" =========== MENU ============ ")
print("\t1. Hu tieu")
print("\t2. Chao long")
print("\t3. Banh canh")
print("\t4. Bun rieu")
print("\t5. Pho bo")
print(" ============================== ")

menu = ["1","2","3","4","5","hu tieu","chao long","banh canh", "bun rieu","pho bo"]

luachon = input(" Moi nhap lua chon: ").lower()
if luachon in menu: 
   print(" ============================== ")
else:
    print("Mon ban chon khong co trong menu. Vui long nhap lai!")