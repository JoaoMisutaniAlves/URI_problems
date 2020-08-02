# -*- coding: utf-8 -*-

NAME = input()
SALARY = float(input())
PRODUCT_SOLD = float(input())
TOTAL = ( SALARY + ( PRODUCT_SOLD * 0.15 ) )
print ("TOTAL = R$ %.2f"%TOTAL)