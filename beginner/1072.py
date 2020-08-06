# -*- coding: utf-8 -*-

A = int(input())
n = 0
out = 0
for i in range(A):
    B = int(input())
    if 10 <= B <= 20:
        n+=1
    else:
        out+=1
print("%i in"%n)
print("%i out"%out)