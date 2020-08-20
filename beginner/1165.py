# -*- coding: utf-8 -*-

x = int(input())
result = []
for i in range(x):
    a = int(input())
    soma = 0
    for i in range(a):
        if (a%(i+1)) == 0:
            soma += (i+1)
    if soma == (a+1):
        result.append("%i eh primo"%a)
    else:
        result.append("%i nao eh primo"%a)
for i in result:
    print(i)