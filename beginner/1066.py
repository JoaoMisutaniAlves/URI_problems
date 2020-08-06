# -*- coding: utf-8 -*-

even = 0
odd = 0
positive = 0
negative = 0
for i in range(5):
    A = float(input())
    if (A % 2) == 0:
        even +=1
    elif (A%2) != 0 and A != 0:
        odd+=1
    if A > 0:
        positive +=1
    elif A < 0:
        negative +=1
print("%i valor(es) par(es)"%even)
print("%i valor(es) impar(es)"%odd)
print("%i valor(es) positivo(s)"%positive)
print("%i valor(es) negativo(s)"%negative)
