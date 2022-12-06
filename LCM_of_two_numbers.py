# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:40:51 2022

@author: Raj
"""

def LCM(num1,num2):
    for i in range(max(num1, num2), 1 + (num1 * num2)):
        if i % num1 == i % num2 == 0:
            lcm = i
            break
    print("LCM of", num1, "and", num2, "is", lcm)