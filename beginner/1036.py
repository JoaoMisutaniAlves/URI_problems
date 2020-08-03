# -*- coding: utf-8 -*-

numbers = input().split(" ")
A, B, C = numbers
A = float(A)
B = float(B)
C = float(C)

D = ( B ** 2 - 4 * A * C )
if A == 0 or D < 0:
    print("Impossivel calcular")
else:
    R1= ( - B + D ** ( 1 / 2 ) ) / ( 2 * A )
    R2= ( - B - D ** ( 1 / 2 ) ) / ( 2 * A )
    print("R1 = %.5f"%R1)
    print("R2 = %.5f"%R2)