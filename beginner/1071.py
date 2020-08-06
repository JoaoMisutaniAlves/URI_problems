# -*- coding: utf-8 -*-

A = int(input())
B = int(input())
count = 0
if A != B:
    if A > B:
        if (B%2) != 0:
            B+=1
        list = range(B, A)
    else:
        if (A%2) != 0:
            A+=1
        list = range(A, B)
    for i in list:
        if i % 2 != 0:
            count+=i
else:
    pass
print("%i"%count)