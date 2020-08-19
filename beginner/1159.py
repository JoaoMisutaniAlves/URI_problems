# -*- coding: utf-8 -*-

result = []
num1 = int(input())
while num1 != 0:
    soma = 0
    cont = 0
    while cont < 5:
        if (num1 % 2 == 0):
            soma += num1
            num1 += 1
            cont += 1
        else:
            num1 += 1
    result.append(soma)
    num1 = int(input())
for i in result:
    print("%d"%i)