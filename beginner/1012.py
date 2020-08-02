# -*- coding: utf-8 -*-

VALUES = input().split(" ")
A, B, C = VALUES
π = 3.14159
TRIANGULO = ( float(A) * float(C) ) / 2
CIRCULO = π * float(C) * float(C)
TRAPEZIO = ( ( float(A) + float(B) ) * float(C) ) / 2
QUADRADO = float(B) * float(B)
RETANGULO = float(A) * float(B)
print ("TRIANGULO: %.3f"%TRIANGULO)
print ("CIRCULO: %.3f"%CIRCULO)
print ("TRAPEZIO: %.3f"%TRAPEZIO)
print ("QUADRADO: %.3f"%QUADRADO)
print ("RETANGULO: %.3f"%RETANGULO)