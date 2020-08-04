# -*- coding: utf-8 -*-

A = float(input())

if 0 < A <= 400:
    earned = A * 0.15
    new = earned + A
    percentage = 15
elif 400 < A <= 800:
    earned = A * 0.12
    new = earned + A
    percentage = 12
elif 800 < A <= 1200:
    earned = A * 0.10
    new = earned + A
    percentage = 10
elif 1200 < A <= 2000:
    earned = A * 0.07
    new = earned + A
    percentage = 7
elif 2000 < A:
    earned = A * 0.04
    new = earned + A
    percentage = 4

print("Novo salario: %.2f"%new)
print("Reajuste ganho: %.2f"%earned)
print("Em percentual: %d %%"%percentage)