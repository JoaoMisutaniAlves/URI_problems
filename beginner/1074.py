# -*- coding: utf-8 -*-

A = int(input())
list_A = []
for i in range(A):
    B = int(input())
    list_A.append(B)

for i in list_A:
    if i == 0:
        print("NULL")
    elif i > 0 and (i%2) == 0:
        print("EVEN POSITIVE")
    elif i > 0 and (i%2) != 0:
        print("ODD POSITIVE")
    elif i < 0 and (i%2) == 0:
        print("EVEN NEGATIVE")
    elif i < 0 and (i%2) != 0:
        print("ODD NEGATIVE")