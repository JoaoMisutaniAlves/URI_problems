# -*- coding: utf-8 -*-

A, B, C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)
if A + B <= C or A + C <= B or C + B <= A:
    print("NAO FORMA TRIANGULO")
elif A**2 == B**2 + C**2 or B**2 == A**2 + C**2 or C**2 == B**2 + A**2:
    print("TRIANGULO RETANGULO")
elif A**2 > B**2 + C**2 or B**2 > A**2 + C**2 or C**2 > B**2 + A**2:
    print("TRIANGULO OBTUSANGULO")
elif A**2 < B**2 + C**2 or B**2 < A**2 + C**2 or C**2 < B**2 + A**2:
    print("TRIANGULO ACUTANGULO")
if A == B == C:
    print("TRIANGULO EQUILATERO")
elif A == B or A == C or B == C:
    print("TRIANGULO ISOSCELES")