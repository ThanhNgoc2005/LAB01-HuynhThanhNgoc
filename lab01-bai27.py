# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:37:05 2024

@author: Admin
"""

import math

def calculate_square():
    side = float(input(" nhap chieu dai cua hinh vuong: "))
    perimeter = 4 * side
    area = side * side
    print(f" P = {perimeter:.2f}  S = {area:.2f}")

def calculate_rectangle():
    width = float(input("Nhap chieu rong cua hinh chu nhat: "))
    length = float(input("Nhap chieu dai cua hinh chu nhat: "))
    perimeter = 2 * (width + length)
    area = width * length
    print(f" P = {perimeter:.2f}  S = {area:.2f}")

def calculate_circle():
    radius = float(input("nhap ban kinh cua hinh tron: "))
    perimeter = 2 * math.pi * radius
    area = math.pi * radius * radius
    print(f" P = {perimeter:.2f}  S = {area:.2f}")

def main():

    shape = input("Nhap hinh (v - hinh vuong, n - hinh chu nhat, t - hinh tron): ").strip().lower()
    
    if shape == 'v':
        calculate_square()
    elif shape == 'n':
        calculate_rectangle()
    elif shape == 't':
        calculate_circle()
    else:
        print("Loại hình không hợp lệ. Vui lòng nhập v, n, hoặc t.")

if __name__ == "__main__":
    main()
