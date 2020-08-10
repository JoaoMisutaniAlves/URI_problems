# -*- coding: utf-8 -*-

A, B = input().split(" ")
A = int(A)
B = int(B)
result = []
while A != B:
    if A > B:
        result.append("Decrescente")
    else:
        result.append("Crescente")
    A, B = input().split(" ")
    A = int(A)
    B = int(B)
for i in result:
    print(i)