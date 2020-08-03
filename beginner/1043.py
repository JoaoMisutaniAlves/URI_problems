# -*- coding: utf-8 -*-

x = input().split(" ")
N1, N2, N3 = x
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)

if N1 + N2 > N3 and N1 + N3 > N2 and N3 + N2 > N1:
    print("Perimetro = %.1f"%(N1+N2+N3))
else:
    print("Area = %.1f"%(((N1+N2)*N3)/2))