# -*- coding: utf-8 -*-

positive = 0
average = 0
for i in range(6):
    A = float(input())
    if A > 0:
        positive +=1
        average+= A
print("%i valores positivos"%positive)
print("%.1f"%(average/positive))