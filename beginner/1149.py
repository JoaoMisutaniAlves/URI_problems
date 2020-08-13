# -*- coding: utf-8 -*-

value = input().split(" ")
result = 0
A = int(value[0])
B = int(value[1])
cont = 1
while B <= 0 :
    cont += 1
    B = int(value[cont])
cont = 0
while cont < B:
    result += A
    A += 1
    cont += 1
print(result)