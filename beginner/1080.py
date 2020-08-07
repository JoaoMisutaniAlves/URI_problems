# -*- coding: utf-8 -*-

A = []
for i in range(100):
    A.append(int(input()))
max_a = max(A,key=int)
print(max_a)
print(A.index(max_a)+1)