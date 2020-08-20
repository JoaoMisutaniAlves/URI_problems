# -*- coding: utf-8 -*-

result = []
for i in range(10):
    a = int(input())
    if a <= 0:
        result.append("X[%i] = 1"%i)
    else:
        result.append("X[%i] = %i"%(i, a))
for i in result:
    print(i)