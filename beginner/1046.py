# -*- coding: utf-8 -*-

A, B = input().split(" ")
A = int(A)
B = int(B)

if A > B:
    hours = 24 - A + B
elif A == B:
    hours = 24
else:
    hours = B - A
print("O JOGO DUROU %d HORA(S)"%hours)