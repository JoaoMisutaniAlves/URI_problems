# -*- coding: utf-8 -*-

A = int(input())
if (A % 2) != 0:
    A-=1
for i in range(A,A+12):
    if ( i + 1 ) % 2 != 0:
        print("%i"%(i+1))