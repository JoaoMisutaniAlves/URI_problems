# -*- coding: utf-8 -*-

Alcool = 0
Gasolina = 0
Diesel = 0
N = int(input())
while N != 4:
    if N == 1:
        Alcool+=1
    elif N == 2:
        Gasolina+=1
    elif N == 3:
        Diesel+=1
    N = int(input())
print("MUITO OBRIGADO")
print("Alcool: %i"%Alcool)
print("Gasolina: %i"%Gasolina)
print("Diesel: %i"%Diesel)