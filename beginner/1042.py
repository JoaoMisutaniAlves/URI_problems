# -*- coding: utf-8 -*-

x = input().split(" ")
N1, N2, N3 = x
N1 = int(N1)
N2 = int(N2)
N3 = int(N3)
list=[N1,N2,N3]
list.sort()
for N in list:
    print (N)
print("")
for N in x:
    print (N)