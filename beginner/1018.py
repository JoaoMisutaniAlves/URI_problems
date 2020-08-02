# -*- coding: utf-8 -*-

value = int(input())
print ("%d"%value)
banknote_100 = value/100
decompose = value%100
print ("%d nota(s) de R$ 100,00"%banknote_100)
banknote_50 = decompose/50
decompose = decompose%50
print ("%d nota(s) de R$ 50,00"%banknote_50)
banknote_20 = decompose/20
decompose = decompose%20
print ("%d nota(s) de R$ 20,00"%banknote_20)
banknote_10 = decompose/10
decompose = decompose%10
print ("%d nota(s) de R$ 10,00"%banknote_10)
banknote_5 = decompose/5
decompose = decompose%5
print ("%d nota(s) de R$ 5,00"%banknote_5)
banknote_2 = decompose/2
decompose = decompose%2
print ("%d nota(s) de R$ 2,00"%banknote_2)
banknote_1 = decompose/1
decompose = decompose%1
print ("%d nota(s) de R$ 1,00"%banknote_1)