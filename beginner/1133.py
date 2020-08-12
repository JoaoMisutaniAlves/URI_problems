# -*- coding: utf-8 -*-

X = int(input())
Y = int(input())
S = []
if X > Y:
    R = range( Y + 1 , X )
else:
    R = range( X + 1 , Y )
for I in R:
    if I % 5 == 2 or I % 5 == 3:
        S.append(I)
for I in S:
    print(I)