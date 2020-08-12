# -*- coding: utf-8 -*-

X = int(input())
Y = int(input())
S = 0
if X > Y:
    R = range( Y, X + 1 )
else:
    R = range( X, Y + 1 )
for I in R:
    if I % 13 != 0:
        S += I
print(S)