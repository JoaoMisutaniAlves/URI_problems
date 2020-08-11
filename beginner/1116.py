# -*- coding: utf-8 -*-

A = int(input())
result = []
for i in range(A):
    N1, N2 = input().split(" ")
    N1 = int(N1)
    N2 = int(N2)
    if N2 == 0:
        result.append("divisao impossivel")
    else:
        result.append(N1/N2)
for i in result:
    print(i)