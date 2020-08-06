# -*- coding: utf-8 -*-

even = 0
for i in range(5):
    A = float(input())
    if (A % 2) == 0:
        even +=1
print("%i valores pares"%even)