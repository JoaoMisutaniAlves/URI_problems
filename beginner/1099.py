# -*- coding: utf-8 -*-

list_sum = []
for i in range(int(input())):
    A, B = input().split(" ")
    A = int(A)
    B = int(B)
    sum = 0
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
                sum+=i
    else:
        pass
    list_sum.append(sum)
for i in list_sum:
    print("%i"%i)