# -*- coding: utf-8 -*-

A = int(input())
result = []
for i in range(A):
    B, C, D = input().split(" ")
    B = float(B)
    C = float(C)
    D = float(D)
    result.append((B*2+C*3+D*5)/10)
for i in result:
    print("%.1f"%i)