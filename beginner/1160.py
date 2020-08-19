# -*- coding: utf-8 -*-

casos = int(input())
result = []
for i in range(casos):
    num1, num2, indice1, indice2 = input().split(" ")
    num1 = int(num1)
    num2 = int(num2)
    indice1 = float(indice1)
    indice2 = float(indice2)
    anos = 0
    while num1 <= num2:
        num1 += int(num1*indice1/100)
        num2 += int(num2*indice2/100)
        anos +=1
        if anos > 100:
            result.append('Mais de 1 seculo.')
            break
    if anos <= 100:
        result.append('{} anos.'.format(anos))
for i in result:
    print(i)