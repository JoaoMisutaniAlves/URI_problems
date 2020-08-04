# -*- coding: utf-8 -*-

positive = 0
for i in range(6):
    A = float(input())
    if A > 0:
        positive +=1
print("%i valores positivos"%positive)