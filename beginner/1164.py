# -*- coding: utf-8 -*-

x = int(input())
result = []
for i in range(x):
    a = int(input())
    soma = 0
    for i in range(a):
        if (a%(i+1)) == 0 and a != (i+1):
            soma += (i+1)
    if soma == a:
        result.append("%i eh perfeito"%a)
    else:
        result.append("%i nao eh perfeito"%a)
for i in result:
    print(i)