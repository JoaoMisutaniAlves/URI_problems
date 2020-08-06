# -*- coding: utf-8 -*-

A = int(input())
for i in range(2, A+1):
    if i % 2 == 0:
        print("%i^2 = %i"%(i,(i**2)))