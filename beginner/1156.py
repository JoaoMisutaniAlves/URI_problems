# -*- coding: utf-8 -*-

S = 1
cont = 1
for i in range(1,39):
    if ((i+1)%2) == 1:
        S += (i+1)/(2**cont)
        cont += 1
print("%.2f" %S)