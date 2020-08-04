# -*- coding: utf-8 -*-

A, B, C, D = input().split(" ")
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if A == B == C == D:
    hours = 24
    minutes = 0
elif A > C:
    hours = 24 - A + C
    if B > D:
        hours-=1
        minutes = 60 - B + D
    elif B < D:
        minutes = D - B
    else:
        minutes = 0
elif A < C:
    hours = C - A
    if B > D:
        hours-=1
        minutes = 60 - B + D
    elif B < D:
        minutes = D - B
    else:
        minutes = 0
elif A == C:
    if B > D:
        hours = 23
        minutes = 60 - B + D
    elif B < D:
        hours = 0
        minutes = D - B
print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"% (hours, minutes))