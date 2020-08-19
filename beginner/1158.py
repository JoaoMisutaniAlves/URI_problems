# -*- coding: utf-8 -*-

casos = int(input())
result = []
for i in range(casos):
    num1, num2 = input().split(" ")
    num1 = int(num1)
    num2 = int(num2)
    soma = 0
    cont = 0
    while cont < num2:
        if (num1 % 2 != 0):
            soma += num1
            num1 += 1
            cont += 1
        else:
            num1 += 1
    result.append(soma)
for i in result:
    print("%d"%i)