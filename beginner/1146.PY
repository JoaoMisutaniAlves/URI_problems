# -*- coding: utf-8 -*-

A = int(input())
result = []
while A != 0:
    line = ""
    for i in range(A):
        if i + 1 == A:
            line+= str( i + 1 )
        else:
            line+= str( i + 1 ) + " "
    result.append(line)
    A = int(input())
for i in result:
    print(i)