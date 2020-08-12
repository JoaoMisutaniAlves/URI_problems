# -*- coding: utf-8 -*-

N = 1
while N == 1:
    A = 0
    B = 0
    M = 0
    N = 0
    while A == 0:
        A = float(input())
        if A < 0 or A > 10:
            print("nota invalida")
            A = 0
    while B == 0:
        B = float(input())
        if B < 0 or B > 10:
            print("nota invalida")
            B = 0
    print("media = %.2f"%((A+B)/2))
    while N == 0:
        print("novo calculo (1-sim 2-nao)")
        N = int(input())
        if N == 2:
            break
        elif N == 1:
            pass
        else:
            N = 0