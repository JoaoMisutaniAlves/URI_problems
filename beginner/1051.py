# -*- coding: utf-8 -*-

A = float(input())

if 0 < A <= 2000:
    print("Isento")
else:
    if 2000 < A <= 3000:
        tax = (A-2000) * 0.08
    if 3000 < A <= 4500:
        tax = 1000 * 0.08
        tax += (A-3000) * 0.18
    if 4500 < A:
        tax = 1000 * 0.08
        tax += 1500 * 0.18
        tax += (A-4500) * 0.28
    print("R$ %.2f"%tax)