# -*- coding: utf-8 -*-

A, B = input().split(" ")
A = int(A)
B = int(B)

if (A%B == 0 and B != 0) or (B%A == 0 and A != 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")