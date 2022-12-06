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
    

def GCD(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i             
    print("GCD of", x, "and", y, "is", gcd)