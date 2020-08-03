# -*- coding: utf-8 -*-

N1, N2 = input().split(" ")
N1 = float(N1)
N2 = float(N2)

if N1 == 0 and N2 == 0:
    print("Origem")
elif N1 == 0:
    print("Eixo Y")
elif N2 == 0:
    print("Eixo X")
elif N1 > 0 and N2 > 0:
    print("Q1")
elif N1 > 0 and N2 < 0:
    print("Q4")
elif N1 < 0 and N2 > 0:
    print("Q2")
elif N1 < 0 and N2 < 0:
    print("Q3")