# -*- coding: utf-8 -*-

N1, N2 = input().split(" ")
N1 = float(N1)
N2 = float(N2)
result = []
while N1 != 0 and N2 != 0:
    if N1 > 0 and N2 > 0:
        result.append("primeiro")
    elif N1 > 0 and N2 < 0:
        result.append("quarto")
    elif N1 < 0 and N2 > 0:
        result.append("segundo")
    elif N1 < 0 and N2 < 0:
        result.append("terceiro")
    N1, N2 = input().split(" ")
    N1 = float(N1)
    N2 = float(N2)
for i in result:
    print(i)