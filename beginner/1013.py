# -*- coding: utf-8 -*-

VALUES = input().split(" ")
A, B, C = VALUES
MAIOR_AB = ( int(A) + int(B) + abs( int(A) - int(B) ) ) / 2
RESULT = ( MAIOR_AB + int(C) + abs( MAIOR_AB - int(C) ) ) / 2
print ("%i eh o maior"%RESULT)