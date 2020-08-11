# -*- coding: utf-8 -*-

A = 0
B = 0
M = 0
while A == 0 or B == 0:
    AUX = float(input())
    if AUX < 0 or AUX > 10:
        print("nota invalida")
    elif A == 0:
        A = AUX
    else:
        B = AUX
    if A != B != 0:
        print("media = %.2f"%((A+B)/2))