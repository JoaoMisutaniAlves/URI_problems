# -*- coding: utf-8 -*-

result = []
a = int(input())
result.append("N[0] = %i"%a)
for i in range(1, 10):
    a = a*2
    result.append("N[%i] = %i"%(i, a))
for i in result:
    print(i)