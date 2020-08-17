# -*- coding: utf-8 -*-

X = int(input())
Z = int(input())
count = 1
while X >= Z:
    Z = int(input())
A = X
B = 0
C = 0
while B < Z:
    C += 1
    B += A
    A += 1
print(C)