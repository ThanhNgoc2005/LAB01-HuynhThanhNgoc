# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:39:41 2024

@author: Admin
"""

def count_digits(num):
    return len(set(str(num)))

a = 2659
x = count_digits(a)
print("So nut xe cua toi la:", x,)